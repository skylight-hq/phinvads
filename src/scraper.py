import concurrent.futures
import time
from datetime import datetime
from types import NoneType

import psycopg2
from psycopg2 import sql

from pyhessian.client import HessianProxy

# URL of the PHIN VADS Hessian service
url = "https://phinvads.cdc.gov/vocabService/v2"
service = HessianProxy(url)


# Function to infer SQL data types from Python types
def infer_sql_type(key, value):
    if (
        isinstance(value, bool)
        or value == "True"
        or value == "False"
        or key.endswith("Flag")
    ):
        return "BOOLEAN"
    elif isinstance(value, int):
        return "INTEGER"
    elif isinstance(value, float):
        return "REAL"
    elif isinstance(value, datetime):
        return "TIMESTAMP"
    elif isinstance(value, str):
        # Handle datetime strings separately if needed
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


# Function to generate the SQL create table statement
def generate_create_table_sql(table_name, example_dict):
    columns = []
    for key, value in example_dict.items():
        column_type = infer_sql_type(key, value)
        columns.append(f"{key} {column_type}")

    columns_sql = ", ".join(columns)
    create_table_sql = f"CREATE TABLE IF NOT EXISTS {
        table_name} ({columns_sql});"
    return create_table_sql


def request_without_timeout(timeout, method, *args):
    while True:
        try:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(method, *args)
                response = future.result(timeout=timeout)
                return response
        except concurrent.futures.TimeoutError:
            print("The request timed out")
            time.sleep(timeout)
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(timeout)


# Join values, replacing None with NULL and escaping strings with single or double quotes


def join_values(values):
    return ", ".join(
        [
            (
                f"NULL"
                if value is None
                else (
                    f"'{str(value).replace("'", "''")}'"
                    if isinstance(value, str)
                    else (
                        f"'{str(value)}'" if isinstance(value, datetime) else str(value)
                    )
                )
            )
            for value in values
        ]
    )


def load_code_systems():
    # Get all code systems
    response = service.getAllCodeSystems()
    code_systems = response.codeSystems

    # Create a table for code systems
    code_system_example = code_systems[0].__dict__
    create_table_sql = generate_create_table_sql("code_system", code_system_example)
    print(create_table_sql)
    cur.execute(create_table_sql)

    # Drop all rows from the table
    cur.execute("DELETE FROM code_system;")

    # Insert code systems into the table
    for code_system in code_systems:
        code_system_dict = code_system.__dict__
        columns = code_system_dict.keys()
        values = code_system_dict.values()
        # Join column names and values with commas
        columns = ", ".join(columns)
        values = join_values(values)
        insert_sql = sql.SQL("INSERT INTO code_system ({}) VALUES ({});").format(
            sql.SQL(columns), sql.SQL(values)
        )
        cur.execute(insert_sql)


def load_code_system_concepts():
    # Get all code systems
    # response = service.getAllCodeSystems()
    code_system_oids = [
        # "2.16.840.1.114222.4.5.331",
        # "2.16.840.1.113883.12.206",
        # "2.16.840.1.113883.6.96",
        # "2.16.840.1.114222.4.5.332",
        # "2.16.840.1.113883.3.26.1.5",
        # "2.16.840.1.113883.3.5.14.4",
        # "2.16.840.1.113883.6.1",
        # "2.16.840.1.114222.4.5.232",
        # "2.16.840.1.113883.5.88",
        # "2.16.840.1.113883.6.90",
        # "2.16.840.1.113883.4.291",
    ]
    # Delete rows from code_system_concept table with these code system OIDs
    delete_sql = sql.SQL(
        "DELETE FROM code_system_concept WHERE codesystemoid IN ({})"
    ).format(sql.SQL(", ").join(map(sql.Literal, code_system_oids)))
    cur.execute(delete_sql)
    table_created = True
    page_number = 1
    page_size = 10000

    for code_system_oid in code_system_oids:
        # Get first page of code system concepts
        response = request_without_timeout(
            30,
            service.getCodeSystemConceptsByCodeSystemOid,
            code_system_oid,
            page_number,
            page_size,
        )

        code_system_concepts = response.codeSystemConcepts
        total_code_system_concepts = response.totalResults
        print(f"Total code system concepts for code system {
              code_system_oid}: {total_code_system_concepts}")
        if response.errorText is not None or len(code_system_concepts) == 0:
            print(f"Error text: {response.errorText}")
            continue

        # Loop through all pages of code system concepts
        while len(response.codeSystemConcepts) == page_size:
            page_number += 1
            response = request_without_timeout(
                30,
                service.getCodeSystemConceptsByCodeSystemOid,
                code_system_oid,
                page_number,
                page_size,
            )
            code_system_concepts += response.codeSystemConcepts
            time.sleep(5)

        # Create a table for code system concepts
        if not table_created:
            code_system_concept_example = code_system_concepts[0].__dict__
            print(code_system_concept_example)
            create_table_sql = generate_create_table_sql(
                "code_system_concept", code_system_concept_example
            )
            print(create_table_sql)
            cur.execute(create_table_sql)
            table_created = True
            # Drop all rows from the table
            cur.execute("DELETE FROM code_system_concept;")

        # Insert code system concepts into the table
        for code_system_concept in code_system_concepts:
            code_system_concept_dict = code_system_concept.__dict__
            columns = code_system_concept_dict.keys()
            values = code_system_concept_dict.values()
            # Join column names and values with commas
            columns = ", ".join(columns)
            values = join_values(values)
            insert_sql = sql.SQL(
                "INSERT INTO code_system_concept ({}) VALUES ({});"
            ).format(sql.SQL(columns), sql.SQL(values))
            cur.execute(insert_sql)

        print(f"Inserted {len(code_system_concepts)
                          } code system concepts for code system {code_system_oid}")
        conn.commit()
        time.sleep(5)


def check_code_system_concept_count():
    # Get counts from the database
    cur.execute(
        "SELECT codesystemoid, COUNT(*) FROM code_system_concept GROUP BY codesystemoid;"
    )
    counts_in_db = dict(cur.fetchall())

    counts_from_api = {}
    mismatched_counts = []

    for code_system_oid, count in counts_in_db.items():
        response = request_without_timeout(
            15, service.getCodeSystemConceptsByCodeSystemOid, code_system_oid, 1, 1
        )
        expected_count = response.totalResults
        counts_from_api[code_system_oid] = expected_count
        if expected_count != count:
            print("MISMATCH!!!")
            print(
                f"Expected count for code system {code_system_oid}: {expected_count}, actual count: {count}"
            )
            mismatched_counts.append(code_system_oid)

    if len(mismatched_counts) == 0:
        print("All counts match")
    else:
        print("Mismatched counts: ", mismatched_counts)


# Connect to the database
conn = psycopg2.connect("dbname=phinvads user=postgres password=cdc host=db")
cur = conn.cursor()

# load_code_systems()
# load_code_system_concepts()
check_code_system_concept_count()

# Close communication with the database
conn.commit()
cur.close()
conn.close()
