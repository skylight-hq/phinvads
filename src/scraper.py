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
    if isinstance(value, bool) or value == "True" or value == "False":
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
    elif key.endswith("Name") or key.endswith("Description"):
        return "TEXT"
    else:
        raise TypeError(f"Unsupported type: {type(value)}, Key: {key}")


# Function to generate the SQL create table statement
def generate_create_table_sql(table_name, example_dict):
    columns = []
    for key, value in example_dict.items():
        column_type = infer_sql_type(key, value)
        columns.append(f"{key} {column_type}")

    columns_sql = ", ".join(columns)
    create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_sql});"
    return create_table_sql

def load_code_systems():
    # Get all code systems
    response = service.getAllCodeSystems()
    code_systems = response.codeSystems

    # Create a table for code systems
    code_system_example = code_systems[0].__dict__
    create_table_sql = generate_create_table_sql("code_system", code_system_example)
    print(create_table_sql)
    cur.execute(create_table_sql)

    # Insert code systems into the table
    for code_system in code_systems:
        code_system_dict = code_system.__dict__
        columns = code_system_dict.keys()
        values = code_system_dict.values()
        # Join column names and values with commas
        columns = ", ".join(columns)
        # Join values, replacing None with NULL and escaping strings with single or double quotes
        values = ", ".join(
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
        insert_sql = sql.SQL("INSERT INTO code_system ({}) VALUES ({});").format(
            sql.SQL(columns), sql.SQL(values)
        )
        cur.execute(insert_sql)

# Connect to the database
conn = psycopg2.connect("dbname=phinvads user=postgres password=cdc host=db")
cur = conn.cursor()



# Close communication with the database
conn.commit()
cur.close()
conn.close()
