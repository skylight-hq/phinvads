## PHIN VADS REST API

### Introduction
The PHIN VADS REST API offers a proof-of-concept service for users to query the CDC PHIN VADS system via a REST API. 
    
PHIN VADS is a web-based enterprise vocabulary system for accessing, searching, and distributing vocabularies used in public health and clinical care practice. It promotes the use of standards-based vocabulary to support the exchange of consistent information among public health partners. Currently, there are 215 code systems, 1,944 value sets, 103 views and more than 5 million concepts in PHIN VADS based on the code system/domain recommendations and value set recommendations from Health Information Technology Standards Panel (HITSP) C80 specification (retired April 2010). Users can access and view vocabularies in the context of public health with file download options for Value Sets, Value Set Concepts, Views and Groups available in a tab-delimited text format and also in Microsoft Excel format (additional download file formats are scheduled for a future release of PHIN VADS). The main purpose of PHIN VADS is to distribute the value sets associated with HL7® message implementation guides.  
  
PHIN VADS currently provides a web service based on the [Hessian](https://en.wikipedia.org/wiki/Hessian_(Web_service_protocol)) web service protocol. This project creates a REST API wrapper around that web service using [FastAPI](https://fastapi.tiangolo.com/).

### Project structure

#### dibbs
This contains a Python package that provides a FastAPI `BaseService`. It comes from the DIBBs team's [phdi repo](https://github.com/CDCgov/phdi/tree/main/containers/dibbs).

#### phinvads
This contains the actual FastAPI code which interacts with the Hessian web service and reformats the responses into JSON.

####
This is a slight alteration of the [python-hessian](https://github.com/theatlantic/python-hessian) package that fixes an HTTPSConnection error that was popping up with the PyPI package.

### Example Queries
Get a list of all value sets in PHIN VADS:

`GET localhost:8080/value-sets`