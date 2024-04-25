**# PHIN VADS
 Web Service Interface API**

### Version 2.1

**Table of Contents**

**[PHIN VADS Web Service Interface API 1](# __RefHeading___ Toc292177149)**

[Version 2.1 1](# __RefHeading___ Toc292177150)

**[Domain Objects 1](# __RefHeading___ Toc292177151)**

[Authority 1](# __RefHeading___ Toc292177152)

[CodeSystem 1](# __RefHeading___ Toc292177153)

[CodeSystemConcept 2](# __RefHeading___ Toc292177154)

[CodeSystemConceptAltDesignation 3](# __RefHeading___ Toc292177155)

[CodeSystemConceptPropertyValue 3](# __RefHeading___ Toc292177156)

[CodeSystemPropertyDefinition 4](# __RefHeading___ Toc292177157)

[ConceptRelationship 4](# __RefHeading___ Toc292177158)

[Group 5](# __RefHeading___ Toc292177159)

[Source 5](# __RefHeading___ Toc292177160)

[RelationshipType 5](# __RefHeading___ Toc292177161)

[ValueSet 6](# __RefHeading___ Toc292177162)

[ValueSetConcept 6](# __RefHeading___ Toc292177163)

[ValueSetVersion 7](# __RefHeading___ Toc292177164)

[View 8](# __RefHeading___ Toc292177165)

[ViewVersion 8](# __RefHeading___ Toc292177166)

**[Lookup Constants 9](# __RefHeading___ Toc292177167)**

[SearchTypes 9](# __RefHeading___ Toc292177168)

[VersionOptions 9](# __RefHeading___ Toc292177169)

[CustomMethods 9](# __RefHeading___ Toc292177170)

**[Input DTO Objects 10](# __RefHeading___ Toc292177171)**

[CodeSystemConceptSearchCriteriaDto 10](# __RefHeading___ Toc292177172)

[CodeSystemSearchCriteriaDto 10](# __RefHeading___ Toc292177173)

[GroupSearchCriteriaDto 11](# __RefHeading___ Toc292177174)

[ValueSetConceptSearchCriteriaDto 11](# __RefHeading___ Toc292177175)

[ValueSetSearchCriteriaDto 12](# __RefHeading___ Toc292177176)

[ValueSetVersionSearchCriteriaDto 12](# __RefHeading___ Toc292177177)

[ViewSearchCriteriaDto 13](# __RefHeading___ Toc292177178)

[ViewVersionSearchCriteriaDto 13](# __RefHeading___ Toc292177179)

**[Output DTO Objects 15](# __RefHeading___ Toc292177180)**

[AuthorityResultDto 15](# __RefHeading___ Toc292177181)

[CodeSystemConceptAltDesignationResultDto 15](# __RefHeading___ Toc292177182)

[CodeSystemConceptPropertyValueResultDto 15](# __RefHeading___ Toc292177183)

[CodeSystemConceptResultDto 16](# __RefHeading___ Toc292177184)

[CodeSystemPropertyDefinitionResultDto 16](# __RefHeading___ Toc292177185)

[CodeSystemResultDto 16](# __RefHeading___ Toc292177186)

[CustomResultDto 17](# __RefHeading___ Toc292177187)

[FileImageResultDto 17](# __RefHeading___ Toc292177188)

[GroupResultDto 17](# __RefHeading___ Toc292177189)

[IdResultDto 17](# __RefHeading___ Toc292177190)

[ServiceInfoResultDto 18](# __RefHeading___ Toc292177191)

[SourceResultDto 18](# __RefHeading___ Toc292177192)

[ValidateResultDto 18](# __RefHeading___ Toc292177193)

[ValueSetConceptResultDto 18](# __RefHeading___ Toc292177194)

[ValueSetResultDto 19](# __RefHeading___ Toc292177195)

[ValueSetVersionResultDto 19](# __RefHeading___ Toc292177196)

[ViewResultDto 19](# __RefHeading___ Toc292177197)

[ViewVersionResultDto 20](# __RefHeading___ Toc292177198)

[VocabObjectCountResultDto 20](# __RefHeading___ Toc292177199)

**[Web Service Methods 21](# __RefHeading___ Toc292177200)**

[Bulk Retrieval Methods 21](# __RefHeading___ Toc292177201)

[Search Methods 21](# __RefHeading___ Toc292177202)

[Direct Object Retrieval Methods 23](# __RefHeading___ Toc292177203)

[Related Object Retrieval Methods 24](# __RefHeading___ Toc292177204)

[Validation Methods 26](# __RefHeading___ Toc292177205)

[Miscellaneous Methods 26](# __RefHeading___ Toc292177206)

[Custom Methods 27](# __RefHeading___ Toc292177207)

#


#
## Domain Objects

The domain objects represent the VADS System data.

## Authority

_Represents an assigning authority for a code system_

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| String | id | The GUID identifier for this Authority object. |
| String | name | The name of the authority that develops and maintains the code system or value set. |
| String | description | The description of the authority that develops and maintains the coding system or value set. |
| String | url | Web URL for the Authority. |
| String | contactInformation | Contact information for the person or organization that can be contacted to provide more information on the coding system or value set. |

## CodeSystem

_Represents a vocabulary code system_

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| String | oid | The OID that identifies this Code System object. |
| String | id | The GUID identifier for this Code System object. |
| String | name | The name of the Code System. |
| String | definitionText | A statement of the meaning or purpose of the Code System. |
| String | status | Text that specifies the current state of this Code System. Valid values are [Un-Published, Published, Retired]. |
| Date | statusDate | The date that the status was changed or updated. |
| String | version | The version number of this Code System |
| String | versionDescription | The description of this version of the Code System. |
| Date | acquiredDate | The date that this Code System was acquired |
| Date | effectiveDate | The date that this Code System became effective. |
| Date | expiryDate | The date that this Code System expired. |
| String | assigningAuthorityVersionName | The version of the coding system according to the assigning authority. |
| Date | assigningAuthorityReleaseDate | The date the coding system was released for use by the assigning authority. |
| String | distributionSourceVersionName | Version of the coding system according to the distribution source. |
| Date | distributionSourceReleaseDate | Date the coding system was released for use by the source. |
| String | distributionSourceId | The GUID identifier that represents a Source domain object that corresponds to this Code System. |
| Date | sdoCreateDate | Date the code system is Created by the SDO. |
| Date | lastRevisionDate | Date the code system is last revised by the SDO. |
| Date | sdoReleaseDate | The date that this Code System was released for use. |
| String | assigningAuthorityId | The GUID identifier that represents an Authority domain object that corresponds to this Code System. |
| String | codeSystemCode | An unique code which identifies the CodeSystem for use in specific data exchange context. |
| String | sourceUrl | URL of the distribution source where the coding system can be retrieved. |
| String | hl70396Identifier | An HL7 unique identifier for this Code System. |

## CodeSystemConcept

_Represents a concept that is contained within a code system_

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| String | id | The GUID identifier for this CodeSystemConcept object. |
| String | name | The name of the concept. |
| String | codeSystemOid | The OID that identifies the CodeSystem domain object of which this concept is a member. |
| String | conceptCode | A text code that uniquely identifies this CodeSystemConcept object within the Coding System. |
| String | sdoPreferredDesignation | The "preferred term", the designation the SDO believes is most desired for use when representing the concept. |
| String | definitionText | Miscellaneous text that defines and/or describes this CodeSystemConcept in further detail. |
| String | preCoordinatedFlag | Identifies if the code system concept is pre-coordinated. |
| String | preCoordinatedConceptNote | Describes the general approach and purpose/goal of the pre-coordination of component concepts. |
| Date | sdoConceptCreatedDate | Date the code system concept is Created by the SDO. |
| Date | sdoConceptRevisionDate | Date the code system concept is last revised by the SDO. |
| String | status | A code value which specifies the current state of a vocabulary object. Valid values are [Un-Published, Published, Retired]. |
| Date | statusDate | The date that the status was changed or updated. |
| String | sdoConceptStatus | State of the concept as specified by the Code System SDO. |
| Date | sdoConceptStatusDate | Date the code system concept status is changed by the SDO. |
| String | supersededByCodeSystemConceptId | The unique resource name of the specific instance of Code System Concept that replaces this concept. |
| String | umlsCui | Concept Unique Identifier assigned by UMLS. |
| String | umlsAui | Atom Unique Identifier assigned by UMLS; identifies the occurrence of the concept (atomic unit of work) within the entire UMLS meta thesaurus. |
| Boolean | isRootFlag | If the concept is part of a concept relationship (hierarchy) this indicator determines if the concept is the parent node. |
| Boolean | isConceptFlag | This flag determines if the concept is valid to use in messaging. For example the concept can be a place holder in a concept hierarchy and not a concept that can be sent via a message. |
| Integer | sequence | An ordinal specifier of the sequence in which the Code System Concept should be displayed in the VADS application. |

## CodeSystemConceptAltDesignation

Represents an alternate designation for a CodeSystemConcept

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| String | id | The GUID identifier for this CodeSystemConceptAltDesignation object. |
| String | codeSystemOid | The OID that identifies the CodeSystem domain object with which this object is associated.
 |
| String | conceptCode | The conceptCode that identifies the CodeSystemConcept domain object with which this object is associated. |
| String | sdoDesignationId | The identifier assigned to this designation (i.e. description, alternative name) by the SDO. |
| String | conceptDesignationText | The text representing the alternate designation for the CodeSystemConcept object with which this object is associated. |
| Boolean | phinPreferredTerm | A binary indicator signifying that this designation has been identified by PHIN (Vocabulary Services) as the preferred (linguistic) designation for this concept. |
| Boolean | code | A binary indicator signifying that this designation has been identified by PHIN (Vocabulary Services) as a code. |
| String | sdoDesignationStatus | A code value which specifies the current state of a vocabulary object. Valid values are [Un-Published, Published, Retired]. |
| String | designationType | A code value which specifies the type of concept alternate designation. Example values are "Synonym", "Fully Specified Name". |

## CodeSystemConceptPropertyValue

_Represents a value for a CodeSystem-defined extended property_

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| String | id | The GUID identifier for this CodeSystemConceptPropertyValueobject. |
| String | codeSystemOid | The OID that identifies the CodeSystem domain object with which this object is associated. |
| String | codeSystemConceptCode | The conceptCode that identifies the CodeSystemConcept domain object with which this object is associated. |
| int | sequenceNumber | The unique identifier for this object when paired with the codeSystemOid and the codeSystemConceptCode |
| String | propertyName | The name of this property. |
| String | definitionText | The description or extra information describing this property value object |
| String | valueType | The string that represents the type of data contained within this property. Possible options are: "string", "numeric", "boolean", "date". |
| String | stringValue | The string value of this extended property. Should be checked if valueType = "string". |
| double | numericValue | The numeric value of this extended property. Should be checked if valueType = "numeric." |
| Boolean | booleanValue | The Boolean value of this extended property. Should be checked if valueType = "Boolean". |
| Date | dateValue | The date value of this extended property. Should be checked if valueType = "date". |

## CodeSystemPropertyDefinition

Represents an extended property for Code System Concepts as defined by a Code System

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| String | id | The GUID identifier for this CodeSystemPropertyDefinitionobject. |
| String | codeSystemOid | The OID that identifies the CodeSystem domain object with which this object is associated. |
| int | sequenceNumber | The unique identifier for this object when paired with the codeSystemOid. |
| String | name | The name of this extended property. |
| String | definitionText | The description or extra information describing this property object |
| String | dataType | The data type of this property: "Numeric", "String", "DateTime", "Boolean". |
| int | maxLength | The maximum length for this property if it has a dataType of "String". |
| Boolean | required | Indicates whether or not this property is required. |

## ConceptRelationship

_Represents a Concept to Concept or Concept to Value Set Relationship_

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| String | id | The GUID identifier for this ConceptRelationshipobject. |
| String | type | The relationshipType code that indicates what type of relationship this object represents |
| String | codeSystemOid1 | The code system oid of the parent object |
| String | conceptCode1 | The concept code of the parent object |
| String | conceptName1 | The concept name of the parent object |
| String | codeSystemOid2 | The code system oid of the child object |
| String | conceptCode2 | The concept code of the child object |
| String | conceptName2 | The concept name of the child object |
| String | valueSetOid | The value set oid of the child object |
| String | status | The relationship publish status |
| Date | statusDate | The date of the relationship publish status |

## Group

_Represents a V_ocabulary Group

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| String | id | The GUID identifier for this Group object. |
| String | name | The name of the Group. |
| String | descriptionText | A free-form, textual discourse of the nature and or purpose of the PHIN Vocabulary Domain instance. |
| String | status | A code value which specifies the current state of a vocabulary object. Valid values are [Un-Published, Published, Retired]. |
| Date | statusDate | The date that the status was changed or updated. |
| String | groupNotes | VADS team internal notes that may be entered for the group. |

## Source

Represents the distribution source for a code system

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| String | id | The GUID identifier for this Source object. |
| String | name | The name of this Source. |
| String | description | The description of this Source. |
| String | url | The web URL of this Source. |
| String | contactInformation | Contact information for the person or organization that can be contacted to provide more information on the coding system. |

## RelationshipType

_Represents a concept relationship type such as parent/child._

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| String | relationshipTypeCode | The code that identifies this RelationshipType |
| String | name | The name of this RelatioshipType. |
| String | definitionText | The description of this RelationshipType. |

## ValueSet

_Represents a vocabulary Value Set_

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| String | id | The GUID identifier for this ValueSet object. |
| String | oid | The OID that uniquely identifies this ValueSet object. |
| String | name | The name of the ValueSet. |
| String | code | The code that uniquely identifies this ValueSet object. |
| String | status | Current state of this value set. Valid values are [under development, active, retired]. |
| Date | statusDate | The date that the status was last modified. |
| String | definitionText | Definition of the specific value set [NOTE: Value Set Definition is set at the Value Set level and is universal to all versions of that value set; differential descriptions are maintained at the Value Set Version level]. |
| String | scopeNoteText | A note which defines or clarifies the purpose of the value set as it is intended to be used in PHIN information exchange and data governance validations. |
| String | assigningAuthorityId | The GUID identifier for the AssigningAuthority domain object that is associated with this ValueSet. |
| Date | valueSetCreatedDate | The date that this ValueSet was created. |
| Date | valueSetLastRevisionDate | The date that this ValueSet was last modified. |

## ValueSetConcept

_Represents a Concept defined by a Value Set_

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| String | id | The GUID identifier for this ValueSetConcept object. |
| String | codeSystemOid | The OID that identifies the CodeSystem with which this ValueSetConcept is associated. |
| String | valueSetVersionId | The GUID that identifies the ValueSetVersion with which this ValueSetConcept is associated. |
| String | conceptCode | The conceptCode text that uniquely identifies this ValueSetConcept within a ValueSetVersion or a CodeSystem. |
| String | scopeNoteText | The text that describes the scope of this ValueSetConcept |
| String | status | A code value which specifies the current state of a vocabulary object. Valid values are [Un-Published, Published, Retired]. |
| Date | statusDate | The date that the status was last modified. |
| String | cdcPreferredDesignation | The "preferred term", the designation the CDC believes is most desired for use when representing the concept. |
| String | preferredAlternateCode | Actual description or synonym name or text provided by SDO for this Concept where the Alternate Designation is defined as a Code and is the PHIN Preferred Term for this Concept. |
| String | definitionText | The description or extra information describing this ValueSetConcept object |
| String | codeSystemConceptName | The Name of the CodeSystemConcept which was used as the source for this ValueSetConcept. |

## ValueSetVersion

_Represents a defined instance, or version, for a specific Value Set_

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| String | id | The GUID identifier for this ValueSetVersion object. |
| String | valueSetOid | The OID that identifies the ValueSet domain object with which this object is associated. |
| int | versionNumber | The version number of this ValueSetVersion. |
| String | description | The text that describes this ValueSetVersion. |
| String | status | A code value which specifies the current state of this value set version object. Valid values are [Un-Published, Published, Retired]. |
| Date | statusDate | The date that the status was last modified. |
| String | assigningAuthorityText | Used to label a version of the value set. Defines the requirement to create a new version of the value set. |
| Date | assigningAuthorityReleaseDate | The date the value set is released by the assigning authority. |
| String | noteText | Used to document information of interest. This metadata property can be used to document information on how the value set is created such as if the value set is an enumeration of a coding system, and the root concept for the enumeration. |
| Date | effectiveDate | The date that this ValueSetVersion is effective. |
| Date | expiryDate | The date that this ValueSetVersion is set to expire. |

##

## View

_Represents a Vocabulary View_

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| String | id | The GUID identifier for this View object. |
| String | name | The name of this View object. |
| String | descriptionText | The description of this View. |
| String | status | A code value which specifies the current state of this view object. Valid values are [Un-Published, Published, Retired]. |
| Date | statusDate | The date that the status was last modified. |
| String | viewNotes | Detailed notes about this view and its contents. |

## ViewVersion

Represents the distribution source for a code system

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| String | id | The GUID identifier for this Source object. |
| String | viewId | The GUID identifier of the View object with which this viewVersion is associated. |
| int | versionNumber | The version number of this object. |
| String | reason | The reason why this viewVersion was created. |
| String | status | A code value which specifies the current state of this view version object. Valid values are [Un-Published, Published, Retired]. |
| Date | statusDate | The date that the status was last modified. |

#
## Lookup Constants

The lookup constants contain valid input values for certain Input DTO parameters

## SearchTypes

_Represents the valid options for the searchType field, referenced from SearchCriteriaInputDTO objects_

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| int | FULL\_TEXT | Value = 1 |
| int | CONTAINS | Value = 2 |
| int | BEGINS\_WITH | Value = 3 |
| int | ENDS\_WITH | Value = 4 |

## VersionOptions

Represents the valid options for the versionOption field, referenced from searchCriteriaInputDTO objects

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| int | ALL | Value = 1 |
| int | AS\_OF\_DATE | Value = 2 |
| int | CURRENT | Value = 3 |

## CustomMethods

_Represents the valid options for themethodId field that is passed into the invokeCustomMethod web service method, referenced as the methodId parameter on the invokeCustomMethod web method_

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| int | CODE\_SYSTEM\_CONCEPT\_QUICKSEARCH | Value = 1 |
| int | CODE\_SYSTEM\_QUICKSEARCH | Value = 2 |

#
## Input DTO Objects

The Input DTO objects are Data Transfer Objects that are passed into the VADS Web Service

**(\*)Indicates Required Field**

**(\*\*)Indicates conditionally required field**

## CodeSystemConceptSearchCriteriaDto

_Represents the search criteria options used to find Code System Concepts_

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| boolean | codeSearch | Indicates whether the search text field should be compared against the Code System Concept's code property. |
| boolean | nameSearch | Indicates whether the search text field should be compared against the Code System Concept's name property. |
| boolean | preferredNameSearch | Indicates whether the search text field should be compared against the Code System Concept's preferredName property. |
| boolean | definitionSearch | Indicates whether the search text field should be compared against the Code System Concept's definition property. |
| boolean | alternateNameSearch | Indicates whether the search text field should be compared against the Code System Concept's alternateName property. |
| boolean | filterByCodeSystems | Indicates whether the CodeSystemConcept results should be restricted to a specific set of Code Systems. |
| List\<String\> | codeSystemOids | The OIDs representing the CodeSystems to which the CodeSystemConcept results should be restricted. |
| **String**| **\*searchText**| The text that is compared to the selected search fields. |
| **int**| **\*searchType**| Determines the type of matching that is performed against the searchText. Possible Values: (1) Full Word, (2) Contains, (3) Begins With, (4) Ends With._(SearchTypes constant may be used here)_ |

## CodeSystemSearchCriteriaDto

_Represents the search criteria options used to find code systems_

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| boolean | codeSearch | Indicates whether the search text field should be compared against the Code System's code property. |
| boolean | nameSearch | Indicates whether the search text field should be compared against the Code System's name property. |
| boolean | oidSearch | Indicates whether the search text field should be compared against the Code System's OID property. |
| boolean | definitionSearch | Indicates whether the search text field should be compared against the Code System's definition property. |
| boolean | assigningAuthoritySearch | Indicates whether the search text field should be compared against the name of the Assigning Authority. |
| boolean | table396Search | Indicates whether the search text field should be compared against the Code System's HL7 identifier. |
| **String**| **\*searchText**| The text that is compared to the selected search fields. |
| **int**| **\*searchType**| Determines the type of matching that is performed against the searchText. Possible Values: (1) Exact match/Full Text, (2) Contains, (3) Begins With, (4) Ends With._(SearchTypes constant may be used here)_ |

## GroupSearchCriteriaDto

_Represents the search criteria options used to find groups_

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| Boolean | nameSearch | Indicates whether the search text field should be compared against the Group's name property. |
| Boolean | definitionSearch | Indicates whether the search text field should be compared against the Group's definition property. |
| **String**| **\*searchText**| The text that is compared to the selected search fields. |
| **int**| **\*searchType**| Determines the type of matching that is performed against the searchText. Possible Values: (1) Exact match/Full Text, (2) Contains, (3) Begins With, (4) Ends With._(SearchTypes constant may be used here)_ |

## ValueSetConceptSearchCriteriaDto

_Represents the search criteria options used to find code systems_

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| boolean | conceptNameSearch | Indicates whether the search text field should be compared against the Value Set Concept's name property. |
| boolean | conceptCodeSearch | Indicates whether the search text field should be compared against the Value Set Concept's conceptCode property. |
| boolean | preferredNameSearch | Indicates whether the search text field should be compared against the Value Set Concept's preferredName property. |
| boolean | alternateNameSearch | Indicates whether the search text field should be compared against the Value Set Concept's alternateName property. |
| boolean | filterByViews | Indicates whether the ValueSetConcept results should be restricted to a specific set of Views. |
| List\<String\> | viewIds | The GUIDs representing the Views to which the ValueSetConcept results should be restricted. |
| boolean | filterByGroups | Indicates whether the ValueSetConcept results should be restricted to a specific set of Groups. |
| List\<String\> | groupIds | The GUIDs representing the Groups to which the ValueSetConcept results should be restricted. |
| boolean | filterByValueSets | Indicates whether the ValueSetConcept results should be restricted to a specific set of ValueSets. |
| List\<String\> | valueSetOids | The OIDs representing the Value Sets to which the ValueSetConcept results should be restricted. |
| boolean | filterByCodeSystems | Indicates whether the ValueSetConcept results should be restricted to a specific set of Code Systems. |
| List\<String\> | codeSystemOids | The OIDs representing the CodeSystems to which the ValueSetConcept results should be restricted. |
| **String**| **\*searchText**| The text that is compared to the selected search fields. |
| **int**| **\*searchType**| Determines the type of matching that is performed against the searchText. Possible Values: (1) Exact match/Full Text, (2) Contains, (3) Begins With, (4) Ends With._(SearchTypes constant may be used here)_ |
| **int**| **\*versionOption**| Determines whether the search will return the latest version of a found Value Set Concept or whether to return the Value Set Concept that was current as of a particular date, or all. Possible Values: (1) All, (2) As Of the date contained in the versionDate searchCriteria field, (3) Latest. |
| **Date**| **\*\*versionDate**| The date that specifies the search to return a Value Set Concept that was active on this date if the versionOption searchCriteria field has a value of (2). |

## ValueSetSearchCriteriaDto

_Represents the search criteria options used to find value set versions_

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| boolean | codeSearch | Indicates whether the search text field should be compared against the Value Set Version's code property. |
| boolean | nameSearch | Indicates whether the search text field should be compared against the Value Set Version's name property. |
| boolean | oidSearch | Indicates whether the search text field should be compared against the Value Set Version's oid property. |
| boolean | definitionSearch | Indicates whether the search text field should be compared against the Value Set Version's definition property. |
| boolean | filterByViews | Indicates whether the ValueSetConcept results should be restricted to a specific set of Views. |
| List\<String\> | viewIds | The GUIDs representing the Views to which the Value Set Version results should be restricted. |
| boolean | filterByGroups | Indicates whether the Value Set Version results should be restricted to a specific set of Groups. |
| List\<String\> | groupIds | The GUIDs representing the Groups to which the ValueSetConcept results should be restricted. |
| **String**| **\*searchText**| The text that is compared to the selected search fields. |
| **int**| **\*searchType**| Determines the type of matching that is performed against the searchText. Possible Values: (1) Exact match/Full Text, (2) Contains, (3) Begins With, (4) Ends With._(SearchTypes constant may be used here)_ |

## ValueSetVersionSearchCriteriaDto

_Represents the search criteria options used to find value set versions_

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| boolean | codeSearch | Indicates whether the search text field should be compared against the Value Set Version's code property. |
| boolean | nameSearch | Indicates whether the search text field should be compared against the Value Set Version's name property. |
| boolean | oidSearch | Indicates whether the search text field should be compared against the Value Set Version's oid property. |
| boolean | definitionSearch | Indicates whether the search text field should be compared against the Value Set Version's definition property. |
| boolean | filterByViews | Indicates whether the ValueSetConcept results should be restricted to a specific set of Views. |
| List\<String\> | viewIds | The GUIDs representing the Views to which the Value Set Version results should be restricted. |
| boolean | filterByGroups | Indicates whether the Value Set Version results should be restricted to a specific set of Groups. |
| List\<String\> | groupIds | The GUIDs representing the Groups to which the ValueSetConcept results should be restricted. |
| **String**| **\*searchText**| The text that is compared to the selected search fields. |
| **int**| **\*searchType**| Determines the type of matching that is performed against the searchText. Possible Values: (1) Exact match/Full Text, (2) Contains, (3) Begins With, (4) Ends With._(SearchTypes constant may be used here)_ |
| **int**| **\*versionOption**| Determines whether the search will return the latest version of a found Value Set Version or whether to return the Value Set Version that was current as of a particular date, or all. Possible Values: (1) All, (2) As Of the date contained in the versionDate searchCriteria field, (3) Latest. |
| **Date**| **\*\*versionDate**| The date that specifies the search to return a Value Set Version that was active on this date if the versionOption searchCriteria field has a value of (2). |

## ViewSearchCriteriaDto

Represents the search criteria options used to find views

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| **String**| **\*searchText**| The text that is compared to the selected search fields. |
| **int**| **\*searchType**| Determines the type of matching that is performed against the searchText. Possible Values: (1) Full Word, (2) Contains, (3) Begins With, (4) Ends With._(SearchTypes constant may be used here)_ |

## ViewVersionSearchCriteriaDto

Represents the search criteria options used to find view versions

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| **String**| **\*searchText**| The text that is compared to the selected search fields. |
| **int**| **\*searchType**| Determines the type of matching that is performed against the searchText. Possible Values: (1) Full Word, (2) Contains, (3) Begins With, (4) Ends With._(SearchTypes constant may be used here)_ |
| **int**| **\*versionOption**| Determines whether the search will return the latest version of a found Value Set Version or whether to return the Value Set Version that was current as of a particular date, or all. Possible Values: (1) All, (2) As Of the date contained in the versionDate searchCriteria field, (3) Latest. |
| **Date**| **\*\*versionDate**| The date that specifies the search to return a View Version that was active on this date of the versionOption searchCriteria field has a value of (2). |

#
## Output DTO Objects

The output DTO objects are data transfer objects that are returned from the VADS Web Service.

## AuthorityResultDto

Contains Authority data returned from the web service

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| List\<Authority\> | authorities | List of authority domain objects returned from the service call. |
| Int | totalResults | Total number of authority domain objects that can be retrieved from the service. "Find" methods are paginated, and the totalResults can contain a number that is larger than the size of the list that is returned. Get methods should have a totalSize that matches the list size. |
| String | errorText | A descriptive message that indicates a VADS error or a problem with input parameters. The value will be blank or null if no errors occurred. |

## CodeSystemConceptAltDesignationResultDto

Contains CodeSystemConceptAltDesignation data returned from the web service

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| List\<CodeSystemConceptAltDesignation\> | codeSystemConceptAltDesignations | List of CodeSystemConceptAltDesignation domain objects returned from the service call. |
| Int | totalResults | Total number of code system concept alt designation domain objects that can be retrieved from the service. "Find" methods are paginated, and the totalResults can contain a number that is larger than the size of the list that is returned. Get methods should have a totalSize that matches the list size. |
| String | errorText | A descriptive message that indicates a VADS error or a problem with input parameters. The value will be blank or null if no errors occurred. |

## CodeSystemConceptPropertyValueResultDto

Contains CodeSystemConceptPropertyValue data returned from the web service

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| List\<CodeSystemConceptPropertyValue\> | codeSystemConceptPropertyValues | List of codeSystemConceptPropertyValues domain objects returned from the service call. |
| Int | totalResults | Total number of code system concept property value domain objects that can be retrieved from the service. "Find" methods are paginated, and the totalResults can contain a number that is larger than the size of the list that is returned. Get methods should have a totalSize that matches the list size. |
| String | errorText | A descriptive message that indicates a VADS error or a problem with input parameters. The value will be blank or null if no errors occurred. |

## CodeSystemConceptResultDto

Contains Code System Concept data returned from the web service

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| List\<CodeSystemConcept\> | codeSystemConcepts | List of codeSystemConcept domain objects returned from the service call. |
| Int | totalResults | Total number of code system concept domain objects that can be retrieved from the service. "Find" methods are paginated, and the totalResults can contain a number that is larger than the size of the list that is returned. Get methods should have a totalSize that matches the list size. |
| String | errorText | A descriptive message that indicates a VADS error or a problem with input parameters. The value will be blank or null if no errors occurred. |

## CodeSystemPropertyDefinitionResultDto

Contains CodeSystemPropertyDefinitionResultDto data returned from the web service

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| List\<CodeSystemPropertyDefinition\> | codeSystemPropertyDefinitions | List of codeSystemPropertyDefinitions domain objects returned from the service call. |
| Int | totalResults | Total number of code system property definition domain objects that can be retrieved from the service. "Find" methods are paginated, and the totalResults can contain a number that is larger than the size of the list that is returned. Get methods should have a totalSize that matches the list size. |
| String | errorText | A descriptive message that indicates a VADS error or a problem with input parameters. The value will be blank or null if no errors occurred. |

## CodeSystemResultDto

Contains Code System data returned from the web service

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| List\<CodeSystem\> | codeSystems | List of codeSystem domain objects returned from the service call. |
| Int | totalResults | Total number of code system domain objects that can be retrieved from the service. "Find" methods are paginated, and the totalResults can contain a number that is larger than the size of the list that is returned. Get methods should have a totalSize that matches the list size. |
| String | errorText | A descriptive message that indicates a VADS error or a problem with input parameters. The value will be blank or null if no errors occurred. |

## CustomResultDto

Contains custom data returned from the web service

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| List\<Object\> | results | List of custom objects returned from the service call. These results are documented as needed per custom method. |
| Int | totalResults | Total number of custom objects that can be retrieved from the service. "Find" methods are paginated, and the totalResults can contain a number that is larger than the size of the list that is returned. Get methods should have a totalSize that matches the list size. |
| String | errorText | A descriptive message that indicates a VADS error or a problem with input parameters. The value will be blank or null if no errors occurred. |

## FileImageResultDto

Contains Group data returned from the web service

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| List\<byte[]\> | fileImages | List of file images returned from the service call. The files are represented as byte[] arrays. |
| Int | totalResults | Total number of file images that can be retrieved from the service. "Find" methods are paginated, and the totalResults can contain a number that is larger than the size of the list that is returned. Get methods should have a totalSize that matches the list size. |
| String | errorText | A descriptive message that indicates a VADS error or a problem with input parameters. The value will be blank or null if no errors occurred. |

## GroupResultDto

Contains Group data returned from the web service

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| List\<Group\> | groups | List of group domain objects returned from the service call. |
| Int | totalResults | Total number of group domain objects that can be retrieved from the service. "Find" methods are paginated, and the totalResults can contain a number that is larger than the size of the list that is returned. Get methods should have a totalSize that matches the list size. |
| String | errorText | A descriptive message that indicates a VADS error or a problem with input parameters. The value will be blank or null if no errors occurred. |

## IdResultDto

Contains Identifier data returned from the web service

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| List\<String\> | ids | List of ids returned from the service call. These ids can be oids, guids, or other ids depending on the web service method that was invoked. |
| Int | totalResults | Total number of ids that can be retrieved from the service. "Find" methods are paginated, and the totalResults can contain a number that is larger than the size of the list that is returned. Get methods should have a totalSize that matches the list size. |
| String | errorText | A descriptive message that indicates a VADS error or a problem with input parameters. The value will be blank or null if no errors occurred. |

## ServiceInfoResultDto

Contains information about the web service

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| Date | dateStarted | The date that the web service was started. |
| String | description | Text that describes the web service. |
| String | dbVersion | The version of the database that is supporting this web service. |
| Date | dbVersionDate | The date that the dbVersion was created. |
| String | contentVersion | The version of the database content that is supporting this web service. |
| Date | contentVersionDate | The date that the contentVersion was created. |
| String | serviceVersion | The version of this service. |
| ~~Date~~ | ~~serviceVersionDate~~ | ~~The date that the serviceVersion was created.~~ |
| Boolean | Deprecated | Indicates whether this version of the service being invoked is the latest version. Value will be true if this service is not the latest, false otherwise. |

## SourceResultDto

Contains Source data returned from the web service

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| List\<Source\> | sources | List of source domain objects returned from the service call. |
| Int | totalResults | Total number of source domain objects that can be retrieved from the service. "Find" methods are paginated, and the totalResults can contain a number that is larger than the size of the list that is returned. Get methods should have a totalSize that matches the list size. |
| String | errorText | A descriptive message that indicates a VADS error or a problem with input parameters. The value will be blank or null if no errors occurred. |

## ValidateResultDto

Contains the true/false validation result returned from the web service

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| boolean | valid | Indicates whether the validation method returned a successful response (true) or an unsuccessful response (false). |
| String | errorText | A descriptive message that indicates a VADS error or a problem with input parameters. The value will be blank or null if no errors occurred. |

## ValueSetConceptResultDto

Contains Value Set Concept data returned from the web service

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| List\<ValueSetConcept\> | valueSetConcepts | List of value set concept domain objects returned from the service call. |
| Int | totalResults | Total number of value set domain objects that can be retrieved from the service. "Find" methods are paginated, and the totalResults can contain a number that is larger than the size of the list that is returned. Get methods should have a totalSize that matches the list size. |
| String | errorText | A descriptive message that indicates a VADS error or a problem with input parameters. The value will be blank or null if no errors occurred. |

## ValueSetResultDto

Contains Value Set data returned from the web service

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| List\<ValueSet\> | valueSets | List of value set domain objects returned from the service call. |
| Int | totalResults | Total number of value set domain objects that can be retrieved from the service. "Find" methods are paginated, and the totalResults can contain a number that is larger than the size of the list that is returned. Get methods should have a totalSize that matches the list size. |
| String | errorText | A descriptive message that indicates a VADS error or a problem with input parameters. The value will be blank or null if no errors occurred. |

## ValueSetVersionResultDto

Contains Value Set Version data returned from the web service

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| List\<ValueSetVersion\> | valueSetVersions | List of value set version domain objects returned from the service call. |
| Int | totalResults | Total number of value set version domain objects that can be retrieved from the service. "Find" methods are paginated, and the totalResults can contain a number that is larger than the size of the list that is returned. Get methods should have a totalSize that matches the list size. |
| String | errorText | A descriptive message that indicates a VADS error or a problem with input parameters. The value will be blank or null if no errors occurred. |

## ViewResultDto

Contains View data returned from the web service

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| List\<View\> | views | List of view domain objects returned from the service call. |
| Int | totalResults | Total number of view domain objects that can be retrieved from the service. "Find" methods are paginated, and the totalResults can contain a number that is larger than the size of the list that is returned. Get methods should have a totalSize that matches the list size. |
| String | errorText | A descriptive message that indicates a VADS error or a problem with input parameters. The value will be blank or null if no errors occurred. |

## ViewVersionResultDto

Contains View Version data returned from the web service

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| List\<ViewVersion\> | viewVersions | List of view version domain objects returned from the service call. |
| Int | totalResults | Total number of view version domain objects that can be retrieved from the service. "Find" methods are paginated, and the totalResults can contain a number that is larger than the size of the list that is returned. Get methods should have a totalSize that matches the list size. |
| String | errorText | A descriptive message that indicates a VADS error or a problem with input parameters. The value will be blank or null if no errors occurred. |

## VocabObjectCountResultDto

_Contains hit counts for term that is searched across the entire vads data set. This DTO is_ returned from the web service

| **Data Type**| **Data Name**| **Data Description**|
| --- | --- | --- |
| Int | totalResults | Total number of records across all object types whose contents match the search term entered. |
| Int | valueSetCount | Total number of value set records whose contents match the processed search term. |
| Int | valueSetConceptCount | Total number of value set concept records whose contents match the processed search term. |
| Int | codeSystemCount | Total number of code system records whose contents match the processed search term. |
| Int | codeSystemConceptCount | Total number of code system concept records whose contents match the processed search term. |
| Int | viewCount | Total number of view records whose contents match the processed search term. |
| Int | groupCount | Total number of group records whose contents match the processed search term. |
| String | errorText | A descriptive message that indicates a VADS error or a problem with input parameters. The value will be blank or null if no errors occurred. |

# Web Service Methods

_The methods that can be invoked_

### Bulk Retrieval Methods

| **Method Name**| **Input**| **Output**| **Description**|
| --- | --- | --- | --- |
| getAllViews | None | ViewResultDto | Returns all Views. |
| getAllViewVersions | None | ViewVersionResultDto | Returns all View Versions. |
| getAllGroups | None | GroupResultDto | Returns all Groups. |
| getAllCodeSystems | None | CodeSystemResultDto | Returns all Code Systems |
| getAllValueSets | None | ValueSetResultDto | Returns all Value Sets. |
| getAllValueSetVersions | None | ValueSetVersionResultDto | Returns all Value Set Versions. |
| getAllSources | None | SourceResultDto | Returns all Sources. |
| getAllAuthorities | None | AuthorityResultDto | Returns all Authorities. |
| getAllCodeSystemPropertyDefinitions | None | CodeSystemPropertyDefinitionResultDto | Returns all Code System Property Definitions. |
| getAllRelationshipTypes | None | RelationshipTypeResultDto | Returns all available RelationshipTypes |

###

### Search Methods

| **Method Name**| **Input**| **Output**| **Description**|
| --- | --- | --- | --- |
| findValueSetIds |
1. ValueSetSearchCriteriaDto
2. int pageNumber
3. int pageSize
 | IdResultDto | Returns the Value Set OIDs associated with Value Sets that match the search criteria from parameter (1). This method is paginated. It will only return the number of objects specified by parameter (3). The next "page" of results can be retrieved by incrementing parameter (2) and re-invoking this method. |
| findValueSets | 1)ValueSetSearchCriteriaDto2)int pageNumber3)int pageSize | ValueSetResultDto | Returns the Value Sets that match the search criteria from parameter (1). This method is paginated. It will only return the number of objects specified by parameter (3). The next "page" of results can be retrieved by incrementing parameter (2) and re-invoking this method. |
| findValueSetVersionIds |
1. ValueSetVersionSearchCriteriaDto
2. int pageNumber
3. int pageSize
 | IdResultDto | Returns the Value Set Version IDs associated with Value Set Versions that match the search criteria from parameter (1). This method is paginated. It will only return the number of objects specified by parameter (3). The next "page" of results can be retrieved by incrementing parameter (2) and re-invoking this method. |
| findValueSetVersions | 1)ValueSetVersionSearchCriteriaDto2)int pageNumber3)int pageSize | ValueSetVersionResultDto | Returns the Value Set Versions that match the search criteria from parameter (1). This method is paginated. It will only return the number of objects specified by parameter (3). The next "page" of results can be retrieved by incrementing parameter (2) and re-invoking this method. |
| findCodeSystems | 1)CodeSystemSearchCriteriaDto2)int pageNumber3)int pageSize | CodeSystemResultDto | Returns the Code Systems that match the search criteria from parameter (1). This method is paginated. It will only return the number of objects specified by parameter (3). The next "page" of results can be retrieved by incrementing parameter (2) and re-invoking this method. |
| findCodeSystemIds | 1)CodeSystemSearchCriteriaDto2)int pageNumber3)int pageSize | IdResultDto | Returns the Code System IDs associated with Code Systems that match the search criteria from parameter (1). This method is paginated. It will only return the number of objects specified by parameter (3). The next "page" of results can be retrieved by incrementing parameter (2) and re-invoking this method. |
| findValueSetConcepts | 1)ValueSetConceptSearchCriteriaDto2)int pageNumber3)int pageSize | ValueSetConceptResultDto | Returns the Value Set Concepts that match the search criteria from parameter (1). This method is paginated. It will only return the number of objects specified by parameter (3). The next "page" of results can be retrieved by incrementing parameter (2) and re-invoking this method. |
| findCodeSystemConcepts | 1)CodeSystemConceptSearchCriteriaDto2)int pageNumber3)int pageSize | CodeSystemConceptResultDto | Returns the Code System Concepts that match the search criteria from parameter (1). This method is paginated. It will only return the number of objects specified by parameter (3). The next "page" of results can be retrieved by incrementing parameter (2) and re-invoking this method. |
| findGroups | 1)GroupSearchCriteriaDto2)int pageNumber3)int pageSize | GroupResultDto | Returns the Groups that match the search criteria from parameter (1). This method is paginated. It will only return the number of objects specified by parameter (3). The next "page" of results can be retrieved by incrementing parameter (2) and re-invoking this method. |
| findGroupIds | 1)GroupSearchCriteriaDto2)int pageNumber3)int pageSize | IdResultDto | Returns the Group IDs associated with Groups that match the search criteria from parameter (1). This method is paginated. It will only return the number of objects specified by parameter (3). The next "page" of results can be retrieved by incrementing parameter (2) and re-invoking this method. |
| findViews | 1)ViewSearchCriteriaDto2)int pageNumber3)int pageSize | ViewResultDto | Returns the Views that match the search criteria from parameter (1). This method is paginated. It will only return the number of objects specified by parameter (3). The next "page" of results can be retrieved by incrementing parameter (2) and re-invoking this method. |
| findViewIds | 1)ViewSearchCriteriaDto2)int pageNumber3)int pageSize | IdResultDto | Returns the View IDs associated with the View Versions that match the search criteria from parameter (1). This method is paginated. It will only return the number of objects specified by parameter (3). The next "page" of results can be retrieved by incrementing parameter (2) and re-invoking this method. |
| findViewVersions | 1)ViewVersionSearchCriteriaDto2)int pageNumber3)int pageSize | ViewVersionResultDto | Returns the View Versions that match the search criteria from parameter (1). This method is paginated. It will only return the number of objects specified by parameter (3). The next "page" of results can be retrieved by incrementing parameter (2) and re-invoking this method. |
| findViewVersionIds | 1)ViewVersionSearchCriteriaDto2)int pageNumber3)int pageSize | IdResultDto | Returns the View Version IDs associated with the View Versions that match the search criteria from parameter (1). This method is paginated. It will only return the number of objects specified by parameter (3). The next "page" of results can be retrieved by incrementing parameter (2) and re-invoking this method. |
| findVocabObjectCounts | 1)String searchText
 | VocabObjectCountResultDto | Returns a collection of domain object specific counts for the number of records that match the searchText parameter. This method is for searching for a specific term across Value Sets, Value Set Concepts, Code Systems, Code System Concepts, Views and Groups. |

### Direct Object Retrieval Methods

| **Method Name**| **Input**| **Output**| **Description**|
| --- | --- | --- | --- |
| getViewById | 1) String viewId | ViewResultDto | Returns the View that corresponds to the viewId input parameter. |
| getViewByName | 1) String name | ViewResultDto | Returns the View that corresponds to the name input parameter. |
| getViewVersionById | 1) String viewVersionId | ViewVersionResultDto | Returns the View Version that corresponds to the viewVersionId input parameter. |
| getViewVersionByViewNameAndVersionNumber | 1) String viewName2) Integer versionNumber | ViewVersionResultDto | Returns the View Version that corresponds to the viewName and versionNumber input parameters. If versionNumber is null, the most current viewVersion will be returned. |
| getGroupById | 1) String groupId | GroupResultDto | Returns the Group that corresponds to the groupId input parameter. |
| getGroupByName | 1) String name | GroupResultDto | Returns the Group whose name corresponds to the name input parameter. |
| getValueSetVersionById | 1) String valueSetVersionId | ValueSetVersionResultDto | Returns the Value Set Version that corresponds to the valueSetVersionId input parameter. |
| getValueSetVersionByValueSetOidAndVersionNumber | 1) String valueSetOid2) Integer versionNumber | ValueSetVersionResultDto | Returns the ValueSetVersion that corresponds to the valueSetOid and versionNumber input parameters. If versionNumber is null, the most current valueSetVersion will be returned. |
| getCodeSystemConceptByOidAndCode | 1) String codeSystemOid2) String conceptCode | CodeSystemConceptResultDto | Returns the Code System Concept that is contained within the Code System specified by the codeSystemOid parameter (1) which has the code identified by the conceptCode parameter(2) |
| getCodeSystemConceptById | 1) String codeSystemConceptId | CodeSystemConceptResultDto | Returns the Code System Concept that corresponds to the codeSystemConceptId input parameter. |
| getValueSetConceptById | 1) String valueSetConceptId | ValueSetConceptResultDto | Returns the Value Set Concept that corresponds to the valueSetConceptId input parameter. |
| getCodeSystemByOid | 1) String codesystemOid | CodeSystemResultDto | Returns the Code System that corresponds to the codesystemOid input parameter. |
| getAuthorityById | 1) String authorityId | AuthorityResultDto | Returns the Authority that corresponds to the authorityId input parameter. |
| getSourceById | 1) String sourceId | SourceResultDto | Returns the Source that corresponds to the sourceId input parameter. |
| getValueSetByOid | 1) String valueSetOid | ValueSetResultDto | Returns the ValueSet that corresponds to the valueSetOid input parameter. |

### Related Object Retrieval Methods

| **Method Name**| **Input**| **Output**| **Description**|
| --- | --- | --- | --- |
| getGroupsByValueSetOid | 1) String valueSetOid | GroupResultDto | Returns the Groups that contain the ValueSet that corresponds to the valueSetOid input parameter. |
| getGroupIdsByValueSetOid | 1) String valueSetOid | IdResultDto | Returns the Group IDs that are associated with the Groups that contain the ValueSet that corresponds to the valueSetOid input parameter. |
| getViewVersionsByValueSetVersionId | 1) String valueSetVersionId | ViewVersionResultDto | Returns the View Versions that contain the Value Set Version that corresponds to the valueSetVersionId input parameter. |
| getViewVersionIdsByValueSetVersionId | 1) String valueSetVersionId | IdResultDto | Returns the View Version IDs that are associated with the View Versions that contain the Value Set Version that corresponds to the valueSetVersionId input parameter. |
| getValueSetVersionsByValueSetOid | 1) String valueSetOid | ValueSetVersionResultDto | Returns the Value Set Versions that are associated with the Value Set that corresponds to the valueSetOid input parameter. |
| getValueSetVersionIdsByValueSetOid | 1) String valueSetOid | IdResultDto | Returns the Value Set Version IDs for the Value Set Versions that are associated with the Value Set that corresponds to the valueSetOid input parameter. |
| getValueSetConceptsByValueSetVersionId | 1)String valueSetVersionId2)int pageNumber3)int pageSize | ValueSetConceptResultDto | Returns the Value Set Concepts that are associated with the Value Set Version specified by parameter (1). This method is paginated. It will only return the number of objects specified by parameter (3). The next "page" of results can be retrieved by incrementing parameter (2) and re-invoking this method. |
| getCodeSystemConceptAltDesignationByOidAndCode | 1) String codeSystemOid2) String conceptCode | CodeSystemConceptAltDesignationResultDto | Returns the Code System Concept Alternate Designations for the Code System Concept that corresponds to the codeSystemOid and conceptCode input parameters. |
| ~~getParentCodeSystemConceptsByOidAndCode~~ | 1) String codeSystemOid2) String conceptCode | CodeSystemConceptResultDto | Returns the Parent Code System Concepts for the Code System Concept that corresponds to the codeSystemOid and conceptCode input parameters. |
| ~~getChildCodeSystemConceptsByOidAndCode~~ | 1) String codeSystemOid2) String conceptCode | CodeSystemConceptResultDto | Returns the Child Code System Concepts for the Code System Concept that corresponds to the codeSystemOid and conceptCode input parameters. |
| getChildCodeSystemConceptsByRelationshipType | 1) String codeSystemOid2) String conceptCode3) String relationshipType4) Integer pageNumber5) Integer pageSize | CodeSystemConceptResultDto | Returns child code system concepts for the code system concept that corresponds to the codeSystemOid and conceptCode input parameters. The child objects are of the relationshipType indicated by the relationshipType parameter. |
| getParentCodeSystemConceptsByRelationshipType | 1) String codeSystemOid2) String conceptCode3) String relationshipType
 | CodeSystemConceptResultDto | Returns parent code system concepts for the code system concept that corresponds to the codeSystemOid and conceptCode input parameters. The parent objects are of the relationshipType indicated by the relationshipType parameter. |
| getCodeSystemPropertyDefinitionsByCodeSystemOid | 1)String codeSystemOid | CodeSystemPropertyDefinitionResultDto | Returns the Code System Property Definitions that are associated with the Code System that corresponds to the codeSystemOid input parameter. |
| getCodeSystemPropertyDefinitionIdsByCodeSystemOid | 1) String codeSystemOid | IdResultDto | Returns the Code System Property Definition IDs for the Code System Property Definitions that are associated with the Code System that corresponds to the codeSystemOid input parameter. |
| getValueSetVersionsByCodeSystemConceptOidAndCode | 1)String codeSystemOid2)String conceptCode | ValueSetVersionResultDto | Returns the Value Set Versions that contain the Code System Concept that corresponds to the codeSystemOid and conceptCode input parameters. |
| getValueSetVersionIdsByCodeSystemConceptOidAndCode | 1)String codeSystemOid2)String conceptCode | IdResultDto | Returns the Value Set Version IDs for the Value Set Versions that contain the Code System Concept that corresponds to the codeSystemOid and conceptCode input parameters. |
| getCodeSystemConceptPropertyValuesByOidAndCode | 1)String codeSystemOid2)String conceptCode | CodeSystemConceptPropertyValueResultDto | Returns the Code System Concept Property Values for the Code System Concept that corresponds to the codeSystemOid and conceptCode input parameters. |
| getCodeSystemConceptsByCodeSystemOid | 1)String codeSystemOid
 | CodeSystemConceptResultDto | Returns the Code System Concepts that are associated with the Code System that corresponds to the codeSystemOid input parameter. |
| getValueSetsByGroupId | 1) String groupId | ValueSetResultDto | Returns the Value Sets that are associated with the Group that corresponds to the groupId input parameter. |
| getValueSetsByGroupName | 1) String name | ValueSetResultDto | Returns the Value Sets that are associated with the Group whose name corresponds to the name input parameter. |
| getValueSetOidsByGroupId | 1) String groupId | IdResultDto | Returns the Value Set OIDs for the Value Sets that are associated with the Group that corresponds to the groupId input parameter. |
| getValueSetVersionsByViewVersionId | 1)String viewVersionId | ValueSetVersionResultDto | Returns the Value Set Versions that are associated with the View Version that corresponds to the viewVersionId input parameter. |
| getValueSetVersionIdsByViewVersionId | 1)String viewVersionId | IdResultDto | Returns the Value Set Version IDs for the Value Set Versions that are associated with the View Version that corresponds to the viewVersionId input parameter. |
| getViewVersionsByViewId | 1) String viewId | ViewVersionResultDto | Returns the View Versions that are associated with the View that corresponds to the viewId input parameter. |
| getViewVersionsByViewName | 1) String name | ViewVersionResultDto | Returns the View Versions that are associated with the View whose name corresponds to the name input parameter. |
| getViewVersionIdsByViewId | 1) String viewId | IdResultDto | Returns the View Version IDs for the View Versions that are associated with the View that corresponds to the viewId input parameter. |
| getValueSetsByCodeSystemConceptOidAndCode | 1) String codeSystemOid2) String conceptCode | ValueSetResultDto | Returns the Value Sets that contain concepts that reference the concept that is contained within the code system that corresponds to the codeSystemOid parameter (1) and whose code corresponds to the conceptCode parameter (2). |

### Validation Methods

| **Method Name**| **Input**| **Output**| **Description**|
| --- | --- | --- | --- |
| validateCodeSystem | 1) String codeSystemOid
 | ValidateResultDto | Returns true if the codeSystemOid parameter corresponds to a CodeSystem within the system, false otherwise. |
| validateValueSet | 1) String valueSetOid
 | ValidateResultDto | Returns true if the valueSetOid parameter corresponds to a ValueSet within the system, false otherwise. |
| validateConceptCodeSystemMembership | 1) String codeSystemOid2) conceptCode
 | ValidateResultDto | Returns true if the conceptCode corresponds to a CodeSystemConcept that is a member of the CodeSystem specified by the codeSystemOid parameter, false otherwise. |
| validateConceptValueSetMembership | 1) String codeSystemOid2) String conceptCode3) String valueSetOid4) Integer valueSetVersion
 | ValidateResultDto | Returns true if the CodeSystemConcept specified by the codeSystemOid and conceptCode parameters is a member of the ValueSetVersion specified by the valueSetOid and valueSetVersion parameters, false otherwise.If the valueSetVersion parameter is null, the system will check for membership against the most current version of the valueSet specified by the valueSetOid parameter. |

### Miscellaneous Methods

| **Method Name**| **Input**| **Output**| **Description**|
| --- | --- | --- | --- |
| getCodeSystemRepresentation | None | FileImageResultDto | Returns the file image that contains the code system representation documentation. |
| getReleaseNotes | None | FileImageResultDto | Returns the file image that contains the release notes for the PHIN Vads application suite. |
| getFile | 1) String filename | FileImageResultDto | Returns the file image that corresponds to the filename input parameter. |
| getServiceInfo | None | ServiceInfoResultDto | Returns information about the VADS Web Service. |
| invokeCustomMethod | 1) Integer methodId2) List\<Object\> params
 | CustomResultDto | Returns custom data that corresponds to the methodId (1) and params (2) that are passed in to the method. The methodId corresponds to a specific function that is implemented to support a priority need that is not available through the other methods on the service. Currently, there are no custom methods implemented. |

### Custom Methods

These are methods that can be invoked to access special-case functionality.

| **Method ID**| **Input**| **Output**| **Description**|
| --- | --- | --- | --- |
| 1CustomMethods.CODE\_SYSTEM\_CONCEPT\_QUICKSEARCH | 1) String codeSystemOid2) String searchText3) Page Number4) Page Size | CustomResultDto(contains CodeSystemConcepts) | Returns Code System Concepts that are members of the specified Code System (1) whose code or name matches the searchText (2). This call is paginated and results will be returned according to the page number (3) and page size (4) input variables. This method has much faster performance than the findCodeSystems() method. |
| 2CustomMethods.CODE\_SYSTEM\_QUICKSEARCH | 1) String searchText2) Page Number3) Page Size | CustomResultDto(contains CodeSystems) | Returns Code Systems whose names matches the searchText (1). This call is paginated and results will be returned according to the page number (2) and page size (3) input variables. This method has much faster performance than the findCodeSystems() method. |
