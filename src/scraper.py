import concurrent.futures
import time
from datetime import datetime
from types import NoneType

import psycopg2
from psycopg2 import sql

from pyhessian.client import HessianProxy

###############################
## DATABASE HELPERS
###############################


def infer_sql_type(key, value):
    if isinstance(value, bool) or value in ["True", "False"] or key.endswith("Flag"):
        return "BOOLEAN"
    elif isinstance(value, int):
        return "INTEGER"
    elif isinstance(value, float):
        return "REAL"
    elif isinstance(value, datetime):
        return "TIMESTAMP"
    elif isinstance(value, str):
        try:
            datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
            return "TIMESTAMP"
        except ValueError:
            return "TEXT"
    elif type(value) == NoneType and key.endswith("Date"):
        return "TIMESTAMP"
    else:
        print(f"Unknown type for {key}: {value}, defaulting to TEXT")
        return "TEXT"


def generate_create_table_sql(table_name, example_dict):
    columns = [
        f"{key} {infer_sql_type(key, value)}" for key, value in example_dict.items()
    ]
    columns_sql = ", ".join(columns)
    return f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_sql});"


def create_table_from_dict(name: str, example_dict: dict, cur):
    create_table_sql = generate_create_table_sql(name, example_dict)
    cur.execute(create_table_sql)


def join_values(values):
    return ", ".join(
        [
            (
                "NULL"
                if value is None
                else f"'{str(value).replace("'", "''")}'"
                if isinstance(value, str)
                else f"'{str(value)}'"
                if isinstance(value, datetime)
                else str(value)
            )
            for value in values
        ]
    )


def insert_records(table_name, records, cur):
    for record in records:
        record_dict = record.__dict__
        columns = ", ".join(record_dict.keys())
        values = join_values(record_dict.values())
        insert_sql = sql.SQL("INSERT INTO {} ({}) VALUES ({});").format(
            sql.Identifier(table_name), sql.SQL(columns), sql.SQL(values)
        )
        cur.execute(insert_sql)


def request_without_timeout(timeout, method, *args):
    while True:
        tries = 0
        print(f"Requesting with args {args}")
        try:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                tries += 1
                if tries > 1:
                    print(f"Attempt {tries}...")
                future = executor.submit(method, *args)
                response = future.result(timeout=timeout)
                return response
        except concurrent.futures.TimeoutError:
            print(
                f"Request timed out after {timeout} seconds, retrying in {timeout} seconds"
            )
            time.sleep(timeout)
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(timeout)


###############################
## BUSINESS LOGIC
###############################


def load_entities(schema, cur):
    table_name = schema["table_name"]
    response = schema["service_method"]()
    entities = getattr(response, schema["response_attribute"])
    example_entity = entities[0].__dict__
    create_table_from_dict(table_name, example_entity, cur)
    insert_records(table_name, entities, cur)
    return [entity[schema["id_key"]] for entity in entities]


def load_concepts(
    schema,
    linked_table_ids,
    cur,
):
    # Read schema
    service_method = schema["service_method"]
    table_name = schema["table_name"]
    response_attribute_name = schema["response_attribute"]
    linked_table_id_name = schema["id_key"]

    # Get example concept and create table
    response = service_method(linked_table_ids[0], 1, 1)
    example_concept = getattr(response, response_attribute_name)[0].__dict__
    create_table_from_dict(table_name, example_concept, cur)

    # Load concepts
    page_size = 10000
    for linked_table_id in linked_table_ids:
        cur.execute(
            f"SELECT COUNT(*) FROM {table_name} WHERE {linked_table_id_name} = %s",
            (linked_table_id,),
        )
        count = cur.fetchone()[0]
        if count > 0:
            response = service_method(linked_table_id, 1, 1)
            if count == response.totalResults:
                print(
                    f"Concepts for {linked_table_id_name} {linked_table_id} already exist"
                )
                continue
            cur.execute(
                f"DELETE FROM {table_name} WHERE {linked_table_id_name} = %s",
                (linked_table_id,),
            )
            conn.commit()

        page_number = 1
        response = request_without_timeout(
            30, service_method, linked_table_id, page_number, page_size
        )
        concepts = getattr(response, response_attribute_name)
        total_concepts = response.totalResults
        print(
            f"Total concepts for {linked_table_id_name} {linked_table_id}: {total_concepts}"
        )
        if response.errorText or not concepts:
            print(f"Error text: {response.errorText}")
            continue

        while len(getattr(response, response_attribute_name)) == page_size:
            page_number += 1
            response = request_without_timeout(
                30, service_method, linked_table_id, page_number, page_size
            )
            concepts += getattr(response, response_attribute_name)

        insert_records(table_name, concepts, cur)
        print(
            f"Inserted {len(concepts)} concepts for {linked_table_id_name} {linked_table_id}"
        )
        conn.commit()


def check_concept_count(schema, cur):
    # Read schema
    table_name = schema["table_name"]
    linked_table_id_name = schema["id_key"]
    service_method = schema["service_method"]

    # Check counts in DB
    cur.execute(
        f"SELECT {linked_table_id_name}, COUNT(*) FROM {table_name} GROUP BY {linked_table_id_name};"
    )
    counts_in_db = dict(cur.fetchall())

    # Check counts in service and compare
    mismatched_counts = []
    for linked_table_id, count in counts_in_db.items():
        response = request_without_timeout(15, service_method, linked_table_id, 1, 1)
        expected_count = response.totalResults
        if expected_count != count:
            print(
                f"MISMATCH!!! Expected count for {linked_table_id_name} {linked_table_id}: {expected_count}, actual count: {count}"
            )
            mismatched_counts.append(linked_table_id)

    if not mismatched_counts:
        print("All counts match")
    else:
        print("Mismatched counts: ", mismatched_counts)


###############################
## MAIN
###############################

# Initialize Hessian client and DB connection
url = "https://phinvads.cdc.gov/vocabService/v2"
service = HessianProxy(url)
conn = psycopg2.connect("dbname=phinvads user=postgres password=cdc host=db")
cur = conn.cursor()

# Define object schema
object_schema = {
    "code_system": {
        "table_name": "code_system",
        "service_method": service.getAllCodeSystems,
        "response_attribute": "codeSystems",
        "id_key": "oid",
    },
    "code_system_concept": {
        "table_name": "code_system_concept",
        "service_method": service.getCodeSystemConceptsByCodeSystemOid,
        "response_attribute": "codeSystemConcepts",
        "id_key": "codesystemoid",
    },
    "value_set": {
        "table_name": "value_set",
        "service_method": service.getAllValueSets,
        "response_attribute": "valueSet",
        "id_key": "oid",
    },
    "value_set_version": {
        "table_name": "value_set_version",
        "service_method": service.getAllValueSetVersions,
        "response_attribute": "valueSetVersions",
        "id_key": "id",
    },
    "value_set_concept": {
        "table_name": "value_set_concept",
        "service_method": service.getValueSetConceptsByValueSetVersionId,
        "response_attribute": "valueSetConcepts",
        "id_key": "valuesetversionid",
    },
}

# Load code systems and code system concepts
code_system_oids = load_entities(object_schema["code_system"], cur)
load_concepts(
    object_schema["code_system_concept"],
    code_system_oids,
    cur,
)
check_concept_count(
    object_schema["code_system_concept"],
    cur,
)

# Load value sets, value set versions, and value set concepts
value_set_oids = load_entities(object_schema["value_set"], cur)
value_set_version_ids = load_entities(object_schema["value_set_version"], cur)
load_concepts(
    object_schema["value_set_concept"],
    value_set_version_ids,
    cur,
)
check_concept_count(
    object_schema["value_set_concept"],
    cur,
)

# Close DB connection
conn.commit()
cur.close()
conn.close()
