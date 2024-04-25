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


##### Bulk Retrieval Methods #####


# Get all views
@app.get("/views")
async def get_views():
    response = service.getAllViews()

    # Iterate trhough the views and convert them to a dictionary
    views = []
    for view in response.views:
        views.append(view.__dict__)

    return {"views": views}


# Get all view versions
@app.get("/view-versions")
async def get_view_versions():
    response = service.getAllViewVersions()

    # Iterate trhough the view versions and convert them to a dictionary
    view_versions = []
    for view_version in response.viewVersions:
        view_versions.append(view_version.__dict__)

    return {"viewVersions": view_versions}


# Get all groups
@app.get("/groups")
async def get_groups():
    response = service.getAllGroups()

    # Iterate trhough the groups and convert them to a dictionary
    groups = []
    for group in response.groups:
        groups.append(group.__dict__)

    return {"groups": groups}


# Get all code systems
@app.get("/code-systems")
async def get_code_systems():
    response = service.getAllCodeSystems()

    # Iterate trhough the code systems and convert them to a dictionary
    code_systems = []
    for code_system in response.codeSystems:
        code_systems.append(code_system.__dict__)

    return {"codeSystems": code_systems}


# Get all value sets
@app.get("/value-sets")
async def get_value_sets():
    response = service.getAllValueSets()

    # Iterate trhough the value sets and convert them to a dictionary
    value_sets = []
    for value_set in response.valueSet:
        value_sets.append(value_set.__dict__)

    return {"valueSets": value_sets}


# Get all value set versions
@app.get("/value-set-versions")
async def get_value_set_versions():
    response = service.getAllValueSetVersions()

    # Iterate trhough the value set versions and convert them to a dictionary
    value_set_versions = []
    for value_set_version in response.valueSetVersions:
        value_set_versions.append(value_set_version.__dict__)

    return {"valueSetVersions": value_set_versions}


# Get all sources
@app.get("/sources")
async def get_sources():
    response = service.getAllSources()

    # Iterate trhough the sources and convert them to a dictionary
    sources = []
    for source in response.sources:
        sources.append(source.__dict__)

    return {"sources": sources}


# Get all authorities
@app.get("/authorities")
async def get_authorities():
    response = service.getAllAuthorities()

    # Iterate trhough the authorities and convert them to a dictionary
    authorities = []
    for authority in response.authorities:
        authorities.append(authority.__dict__)

    return {"authorities": authorities}


# Get all code system property definitions
@app.get("/code-system-property-definitions")
async def get_code_system_property_definitions():
    response = service.getAllCodeSystemPropertyDefinitions()

    # Iterate trhough the code system property definitions and convert them to a dictionary
    code_system_property_definitions = []
    for code_system_property_definition in response.codeSystemPropertyDefinitions:
        code_system_property_definitions.append(
            code_system_property_definition.__dict__
        )

    return {"codeSystemPropertyDefinitions": code_system_property_definitions}


# Get all relationship types
@app.get("/relationship-types")
async def get_relationship_types():
    response = service.getAllRelationshipTypes()

    # Iterate trhough the relationship types and convert them to a dictionary
    relationship_types = []
    for relationship_type in response.relationshipTypes:
        relationship_types.append(relationship_type.__dict__)

    return {"relationshipTypes": relationship_types}
