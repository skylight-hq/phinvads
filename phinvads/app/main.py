import traceback
from dibbs.base_service import BaseService
from pathlib import Path
from pydantic import BaseModel, Field
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


##### Domain Objects #####


# Authority
# Represents an assigning authority for a code system
# | **Data Type**| **Data Name**| **Data Description**|
# | --- | --- | --- |
# | String | id | The GUID identifier for this Authority object. |
# | String | name | The name of the authority that develops and maintains the code system or value set. |
# | String | description | The description of the authority that develops and maintains the coding system or value set. |
# | String | url | Web URL for the Authority. |
# | String | contactInformation | Contact information for the person or organization that can be contacted to provide more information on the coding system or value set. |
class Authority(BaseModel):
    id: str = Field(description="The GUID identifier for this Authority object.")
    name: str = Field(
        description="The name of the authority that develops and maintains the code system or value set."
    )
    description: str = Field(
        description="The description of the authority that develops and maintains the coding system or value set."
    )
    url: str = Field(description="Web URL for the Authority.")
    contactInformation: str = Field(
        description="Contact information for the person or organization that can be contacted to provide more information on the coding system or value set."
    )


# Code System
# Represents a vocabulary code system
# | **Data Type**| **Data Name**| **Data Description**|
# | --- | --- | --- |
# | String | oid | The OID that identifies this Code System object. |
# | String | id | The GUID identifier for this Code System object. |
# | String | name | The name of the Code System. |
# | String | definitionText | A statement of the meaning or purpose of the Code System. |
# | String | status | Text that specifies the current state of this Code System. Valid values are [Un-Published, Published, Retired]. |
# | Date | statusDate | The date that the status was changed or updated. |
# | String | version | The version number of this Code System |
# | String | versionDescription | The description of this version of the Code System. |
# | Date | acquiredDate | The date that this Code System was acquired |
# | Date | effectiveDate | The date that this Code System became effective. |
# | Date | expiryDate | The date that this Code System expired. |
# | String | assigningAuthorityVersionName | The version of the coding system according to the assigning authority. |
# | Date | assigningAuthorityReleaseDate | The date the coding system was released for use by the assigning authority. |
# | String | distributionSourceVersionName | Version of the coding system according to the distribution source. |
# | Date | distributionSourceReleaseDate | Date the coding system was released for use by the source. |
# | String | distributionSourceId | The GUID identifier that represents a Source domain object that corresponds to this Code System. |
# | Date | sdoCreateDate | Date the code system is Created by the SDO. |
# | Date | lastRevisionDate | Date the code system is last revised by the SDO. |
# | Date | sdoReleaseDate | The date that this Code System was released for use. |
# | String | assigningAuthorityId | The GUID identifier that represents an Authority domain object that corresponds to this Code System. |
# | String | codeSystemCode | An unique code which identifies the CodeSystem for use in specific data exchange context. |
# | String | sourceUrl | URL of the distribution source where the coding system can be retrieved. |
# | String | hl70396Identifier | An HL7 unique identifier for this Code System. |
class CodeSystem(BaseModel):
    oid: str = Field(description="The OID that identifies this Code System object.")
    id: str = Field(description="The GUID identifier for this Code System object.")
    name: str = Field(description="The name of the Code System.")
    definitionText: str = Field(
        description="A statement of the meaning or purpose of the Code System."
    )
    status: str = Field(
        description="Text that specifies the current state of this Code System. Valid values are [Un-Published, Published, Retired]."
    )
    statusDate: str = Field(
        description="The date that the status was changed or updated."
    )
    version: str = Field(description="The version number of this Code System")
    versionDescription: str = Field(
        description="The description of this version of the Code System."
    )
    acquiredDate: str = Field(description="The date that this Code System was acquired")
    effectiveDate: str = Field(
        description="The date that this Code System became effective."
    )
    expiryDate: str = Field(description="The date that this Code System expired.")
    assigningAuthorityVersionName: str = Field(
        description="The version of the coding system according to the assigning authority."
    )
    assigningAuthorityReleaseDate: str = Field(
        description="The date the coding system was released for use by the assigning authority."
    )
    distributionSourceVersionName: str = Field(
        description="Version of the coding system according to the distribution source."
    )
    distributionSourceReleaseDate: str = Field(
        description="Date the coding system was released for use by the source."
    )
    distributionSourceId: str = Field(
        description="The GUID identifier that represents a Source domain object that corresponds to this Code System."
    )
    sdoCreateDate: str = Field(
        description="Date the code system is Created by the SDO."
    )
    lastRevisionDate: str = Field(
        description="Date the code system is last revised by the SDO."
    )
    sdoReleaseDate: str = Field(
        description="The date that this Code System was released for use."
    )
    assigningAuthorityId: str = Field(
        description="The GUID identifier that represents an Authority domain object that corresponds to this Code System."
    )
    codeSystemCode: str = Field(
        description="An unique code which identifies the CodeSystem for use in specific data exchange context."
    )
    sourceUrl: str = Field(
        description="URL of the distribution source where the coding system can be retrieved."
    )
    hl70396Identifier: str = Field(
        description="An HL7 unique identifier for this Code System."
    )


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


##### Single Retrieval Methods #####


# Get a value set by OID
@app.get("/value-sets/{value_set_oid}")
async def get_value_set(value_set_oid: str):
    response = service.getValueSetByOid(value_set_oid)
    value_set = response.__dict__.get("valueSet")[0]

    return {"valueSet": value_set}
