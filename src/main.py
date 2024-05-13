from typing import List, Optional
from fastapi import FastAPI, Request
from pydantic import BaseModel, Field
from pyhessian.client import HessianProxy


# Instantiate FastAPI
app = FastAPI()

# URL of the PHIN VADS Hessian service
url = "https://phinvads.cdc.gov/vocabService/v2"

service = HessianProxy(url)


##### Input Search Objects #####


# Represents the search criteria options used to find Code System Concepts
class CodeSystemConceptSearchCriteria(BaseModel):
    codeSearch: bool = Field(
        description="Indicates whether the search text field should be compared against the Code System Concept's code property."
    )
    nameSearch: bool = Field(
        description="Indicates whether the search text field should be compared against the Code System Concept's name property."
    )
    preferredNameSearch: bool = Field(
        description="Indicates whether the search text field should be compared against the Code System Concept's preferredName property."
    )
    definitionSearch: bool = Field(
        description="Indicates whether the search text field should be compared against the Code System Concept's definition property."
    )
    alternateNameSearch: bool = Field(
        description="Indicates whether the search text field should be compared against the Code System Concept's alternateName property."
    )
    filterByCodeSystems: bool = Field(
        description="Indicates whether the CodeSystemConcept results should be restricted to a specific set of Code Systems."
    )
    codeSystemOids: List[str] = Field(
        description="The OIDs representing the CodeSystems to which the CodeSystemConcept results should be restricted."
    )
    searchText: str = Field(
        description="The text that is compared to the selected search fields."
    )
    searchType: int = Field(
        description="Determines the type of matching that is performed against the searchText."
    )


# Represents the search criteria options used to find code systems
class CodeSystemSearchCriteria(BaseModel):
    codeSearch: bool = Field(
        description="Indicates whether the search text field should be compared against the Code System's code property."
    )
    nameSearch: bool = Field(
        description="Indicates whether the search text field should be compared against the Code System's name property."
    )
    oidSearch: bool = Field(
        description="Indicates whether the search text field should be compared against the Code System's OID property."
    )
    definitionSearch: bool = Field(
        description="Indicates whether the search text field should be compared against the Code System's definition property."
    )
    assigningAuthoritySearch: bool = Field(
        description="Indicates whether the search text field should be compared against the name of the Assigning Authority."
    )
    table396Search: bool = Field(
        description="Indicates whether the search text field should be compared against the Code System's HL7 identifier."
    )
    searchText: str = Field(
        description="The text that is compared to the selected search fields."
    )
    searchType: int = Field(
        description="Determines the type of matching that is performed against the searchText."
    )


# Represents the search criteria options used to find groups
class GroupSearchCriteria(BaseModel):
    nameSearch: bool = Field(
        description="Indicates whether the search text field should be compared against the Group's name property."
    )
    definitionSearch: bool = Field(
        description="Indicates whether the search text field should be compared against the Group's definition property."
    )
    searchText: str = Field(
        description="The text that is compared to the selected search fields."
    )
    searchType: int = Field(
        description="Determines the type of matching that is performed against the searchText."
    )


# Represents the search criteria options used to find code systems
class ValueSetConceptSearchCriteria(BaseModel):
    conceptNameSearch: bool = Field(
        description="Indicates whether the search text field should be compared against the Value Set Concept's name property."
    )
    conceptCodeSearch: bool = Field(
        description="Indicates whether the search text field should be compared against the Value Set Concept's conceptCode property."
    )
    preferredNameSearch: bool = Field(
        description="Indicates whether the search text field should be compared against the Value Set Concept's preferredName property."
    )
    alternateNameSearch: bool = Field(
        description="Indicates whether the search text field should be compared against the Value Set Concept's alternateName property."
    )
    filterByViews: bool = Field(
        description="Indicates whether the ValueSetConcept results should be restricted to a specific set of Views."
    )
    viewIds: List[str] = Field(
        description="The GUIDs representing the Views to which the ValueSetConcept results should be restricted."
    )
    filterByGroups: bool = Field(
        description="Indicates whether the ValueSetConcept results should be restricted to a specific set of Groups."
    )
    groupIds: List[str] = Field(
        description="The GUIDs representing the Groups to which the ValueSetConcept results should be restricted."
    )
    filterByValueSets: bool = Field(
        description="Indicates whether the ValueSetConcept results should be restricted to a specific set of ValueSets."
    )
    valueSetOids: List[str] = Field(
        description="The OIDs representing the Value Sets to which the ValueSetConcept results should be restricted."
    )
    filterByCodeSystems: bool = Field(
        description="Indicates whether the ValueSetConcept results should be restricted to a specific set of Code Systems."
    )
    codeSystemOids: List[str] = Field(
        description="The OIDs representing the CodeSystems to which the ValueSetConcept results should be restricted."
    )
    searchText: str = Field(
        description="The text that is compared to the selected search fields."
    )
    searchType: int = Field(
        description="Determines the type of matching that is performed against the searchText."
    )
    versionOption: int = Field(
        description="Determines whether the search will return the latest version of a found Value Set Concept or whether to return the Value Set Concept that was current as of a particular date, or all."
    )
    versionDate: str = Field(
        description="The date that specifies the search to return a Value Set Concept that was active on this date if the versionOption searchCriteria field has a value of (2)."
    )


# Represents the search criteria options used to find value set versions
class ValueSetSearchCriteria(BaseModel):
    codeSearch: Optional[bool] = Field(
        default=None,
        description="Indicates whether the search text field should be compared against the Value Set's code property.",
    )
    nameSearch: Optional[bool] = Field(
        default=None,
        description="Indicates whether the search text field should be compared against the Value Set's name property.",
    )
    oidSearch: Optional[bool] = Field(
        default=None,
        description="Indicates whether the search text field should be compared against the Value Set's OID property.",
    )
    definitionSearch: Optional[bool] = Field(
        default=None,
        description="Indicates whether the search text field should be compared against the Value Set's definition property.",
    )
    filterByViews: Optional[bool] = Field(
        default=None,
        description="Indicates whether the ValueSet results should be restricted to a specific set of Views.",
    )
    viewIds: Optional[List[str]] = Field(
        default=None,
        description="The GUIDs representing the Views to which the ValueSet results should be restricted.",
    )
    filterByGroups: Optional[bool] = Field(
        default=None,
        description="Indicates whether the ValueSet results should be restricted to a specific set of Groups.",
    )
    groupIds: Optional[List[str]] = Field(
        default=None,
        description="The GUIDs representing the Groups to which the ValueSet results should be restricted.",
    )
    filterByValueSets: Optional[bool] = Field(
        default=None,
        description="Indicates whether the ValueSet results should be restricted to a specific set of ValueSets.",
    )
    valueSetOids: Optional[List[str]] = Field(
        default=None,
        description="The OIDs representing the Value Sets to which the ValueSet results should be restricted.",
    )
    filterByCodeSystems: Optional[bool] = Field(
        default=None,
        description="Indicates whether the ValueSet results should be restricted to a specific set of Code Systems.",
    )
    codeSystemOids: Optional[List[str]] = Field(
        default=None,
        description="The OIDs representing the CodeSystems to which the ValueSet results should be restricted.",
    )
    searchText: str = Field(
        description="The text that is compared to the selected search fields."
    )
    searchType: int = Field(
        description="Determines the type of matching that is performed against the searchText. Possible Values: (1) Exact match/Full Text, (2) Contains, (3) Begins With, (4) Ends With. (SearchTypes constant may be used here)"
    )


# Represents the search criteria options used to find value set versions
class ValueSetVersionSearchCriteria(BaseModel):
    codeSearch: bool = Field(
        description="Indicates whether the search text field should be compared against the Value Set Version's code property."
    )
    nameSearch: bool = Field(
        description="Indicates whether the search text field should be compared against the Value Set Version's name property."
    )
    oidSearch: bool = Field(
        description="Indicates whether the search text field should be compared against the Value Set Version's oid property."
    )
    definitionSearch: bool = Field(
        description="Indicates whether the search text field should be compared against the Value Set Version's definition property."
    )
    filterByViews: bool = Field(
        description="Indicates whether the ValueSetConcept results should be restricted to a specific set of Views."
    )
    viewIds: List[str] = Field(
        description="The GUIDs representing the Views to which the Value Set Version results should be restricted."
    )
    filterByGroups: bool = Field(
        description="Indicates whether the Value Set Version results should be restricted to a specific set of Groups."
    )
    groupIds: List[str] = Field(
        description="The GUIDs representing the Groups to which the ValueSetConcept results should be restricted."
    )
    searchText: str = Field(
        description="The text that is compared to the selected search fields."
    )
    searchType: int = Field(
        description="Determines the type of matching that is performed against the searchText."
    )
    versionOption: int = Field(
        description="Determines whether the search will return the latest version of a found Value Set Version or whether to return the Value Set Version that was current as of a particular date, or all."
    )
    versionDate: str = Field(
        description="The date that specifies the search to return a Value Set Version that was active on this date if the versionOption searchCriteria field has a value of (2)."
    )


# Represents the search criteria options used to find views
class ViewSearchCriteria(BaseModel):
    searchText: str = Field(
        description="The text that is compared to the selected search fields."
    )
    searchType: int = Field(
        description="Determines the type of matching that is performed against the searchText."
    )


# Represents the search criteria options used to find view versions
class ViewVersionSearchCriteria(BaseModel):
    searchText: str = Field(
        description="The text that is compared to the selected search fields."
    )
    searchType: int = Field(
        description="Determines the type of matching that is performed against the searchText."
    )
    versionOption: int = Field(
        description="Determines whether the search will return the latest version of a found Value Set Version or whether to return the Value Set Version that was current as of a particular date, or all."
    )
    versionDate: str = Field(
        description="The date that specifies the search to return a View Version that was active on this date of the versionOption searchCriteria field has a value of (2)."
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


##### Search Methods #####
# | **Method Name**| **Input**| **Output**| **Description**|
# | --- | --- | --- | --- |
# | findValueSetIds |
# 1. ValueSetSearchCriteriaDto
# 2. int pageNumber
# 3. int pageSize
#  | IdResultDto | Returns the Value Set OIDs associated with Value Sets that match the search criteria from parameter (1). This method is paginated. It will only return the number of objects specified by parameter (3). The next "page" of results can be retrieved by incrementing parameter (2) and re-invoking this method. |
# | findValueSets | 1)ValueSetSearchCriteriaDto2)int pageNumber3)int pageSize | ValueSetResultDto | Returns the Value Sets that match the search criteria from parameter (1). This method is paginated. It will only return the number of objects specified by parameter (3). The next "page" of results can be retrieved by incrementing parameter (2) and re-invoking this method. |
# | findValueSetVersionIds |
# 1. ValueSetVersionSearchCriteriaDto
# 2. int pageNumber
# 3. int pageSize
#  | IdResultDto | Returns the Value Set Version IDs associated with Value Set Versions that match the search criteria from parameter (1). This method is paginated. It will only return the number of objects specified by parameter (3). The next "page" of results can be retrieved by incrementing parameter (2) and re-invoking this method. |
# | findValueSetVersions | 1)ValueSetVersionSearchCriteriaDto2)int pageNumber3)int pageSize | ValueSetVersionResultDto | Returns the Value Set Versions that match the search criteria from parameter (1). This method is paginated. It will only return the number of objects specified by parameter (3). The next "page" of results can be retrieved by incrementing parameter (2) and re-invoking this method. |
# | findCodeSystems | 1)CodeSystemSearchCriteriaDto2)int pageNumber3)int pageSize | CodeSystemResultDto | Returns the Code Systems that match the search criteria from parameter (1). This method is paginated. It will only return the number of objects specified by parameter (3). The next "page" of results can be retrieved by incrementing parameter (2) and re-invoking this method. |
# | findCodeSystemIds | 1)CodeSystemSearchCriteriaDto2)int pageNumber3)int pageSize | IdResultDto | Returns the Code System IDs associated with Code Systems that match the search criteria from parameter (1). This method is paginated. It will only return the number of objects specified by parameter (3). The next "page" of results can be retrieved by incrementing parameter (2) and re-invoking this method. |
# | findValueSetConcepts | 1)ValueSetConceptSearchCriteriaDto2)int pageNumber3)int pageSize | ValueSetConceptResultDto | Returns the Value Set Concepts that match the search criteria from parameter (1). This method is paginated. It will only return the number of objects specified by parameter (3). The next "page" of results can be retrieved by incrementing parameter (2) and re-invoking this method. |
# | findCodeSystemConcepts | 1)CodeSystemConceptSearchCriteriaDto2)int pageNumber3)int pageSize | CodeSystemConceptResultDto | Returns the Code System Concepts that match the search criteria from parameter (1). This method is paginated. It will only return the number of objects specified by parameter (3). The next "page" of results can be retrieved by incrementing parameter (2) and re-invoking this method. |
# | findGroups | 1)GroupSearchCriteriaDto2)int pageNumber3)int pageSize | GroupResultDto | Returns the Groups that match the search criteria from parameter (1). This method is paginated. It will only return the number of objects specified by parameter (3). The next "page" of results can be retrieved by incrementing parameter (2) and re-invoking this method. |
# | findGroupIds | 1)GroupSearchCriteriaDto2)int pageNumber3)int pageSize | IdResultDto | Returns the Group IDs associated with Groups that match the search criteria from parameter (1). This method is paginated. It will only return the number of objects specified by parameter (3). The next "page" of results can be retrieved by incrementing parameter (2) and re-invoking this method. |
# | findViews | 1)ViewSearchCriteriaDto2)int pageNumber3)int pageSize | ViewResultDto | Returns the Views that match the search criteria from parameter (1). This method is paginated. It will only return the number of objects specified by parameter (3). The next "page" of results can be retrieved by incrementing parameter (2) and re-invoking this method. |
# | findViewIds | 1)ViewSearchCriteriaDto2)int pageNumber3)int pageSize | IdResultDto | Returns the View IDs associated with the View Versions that match the search criteria from parameter (1). This method is paginated. It will only return the number of objects specified by parameter (3). The next "page" of results can be retrieved by incrementing parameter (2) and re-invoking this method. |
# | findViewVersions | 1)ViewVersionSearchCriteriaDto2)int pageNumber3)int pageSize | ViewVersionResultDto | Returns the View Versions that match the search criteria from parameter (1). This method is paginated. It will only return the number of objects specified by parameter (3). The next "page" of results can be retrieved by incrementing parameter (2) and re-invoking this method. |
# | findViewVersionIds | 1)ViewVersionSearchCriteriaDto2)int pageNumber3)int pageSize | IdResultDto | Returns the View Version IDs associated with the View Versions that match the search criteria from parameter (1). This method is paginated. It will only return the number of objects specified by parameter (3). The next "page" of results can be retrieved by incrementing parameter (2) and re-invoking this method. |
# | findVocabObjectCounts | 1)String searchText
#  | VocabObjectCountResultDto | Returns a collection of domain object specific counts for the number of records that match the searchText parameter. This method is for searching for a specific term across Value Sets, Value Set Concepts, Code Systems, Code System Concepts, Views and Groups. |


# Find value set IDs
@app.post("/find-value-set-ids")
async def find_value_set_ids(
    input: ValueSetSearchCriteria, page_number: int, page_size: int
):
    response = service.findValueSetIds(input, page_number, page_size)

    return {"valueSetIds": response}


# Find value sets
@app.post("/find-value-sets")
async def find_value_sets(
    input: ValueSetSearchCriteria,
    page_number: int = 0,
    page_size: int = 10,
):
    response = service.findValueSets(input.model_dump(), page_number, page_size)

    # Iterate through the value sets and convert them to a dictionary
    value_sets = []
    for value_set in response.valueSet:
        value_sets.append(value_set.__dict__)

    return {"valueSets": value_sets}


##### Single Retrieval Methods #####


# Get a value set by OID
@app.get("/value-sets/{value_set_oid}")
async def get_value_set(value_set_oid: str):
    response = service.getValueSetByOid(value_set_oid)
    value_set = response.__dict__.get("valueSet")[0]

    return {"valueSet": value_set}
