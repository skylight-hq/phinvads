import traceback
from dibbs.base_service import BaseService
from pathlib import Path
from pyhessian.client import HessianProxy

# Instantiate FastAPI via DIBBs' BaseService class
app = BaseService(
    service_name="PHIN VADS REST API",
    service_path="/phinvads",
    description_path=Path(__file__).parent.parent / "description.md",
    include_health_check_endpoint=True,
).start()

# URL of the PHIN VADS Hessian service
url = "https://phinvads.cdc.gov/vocabService/v2"

service = HessianProxy(url)


# Get all value sets
@app.get("/value-sets")
async def get_value_sets():
    response = service.getAllValueSets()

    # Iterate trhough the value sets and convert them to a dictionary
    value_sets = []
    for value_set in response.valueSet:
        value_sets.append(value_set.__dict__)

    return {"valueSets": value_sets}


# Get a value set by OID
@app.get("/value-sets/{value_set_oid}")
async def get_value_set(value_set_oid: str):
    response = service.getValueSetByOid(value_set_oid)
    value_set = response.__dict__.get("valueSet")[0]

    return {"valueSet": value_set}
