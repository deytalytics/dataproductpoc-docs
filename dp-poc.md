# Data Product Proof of Concept (PoC)

The aim of the PoC is to be able to deduce a viable set of architectural standards by proving that the concepts are feasible in practice.

## What will be proved?

For our PoC we have decided to concentrate on a REST API as the easiest data product type to try to build first.
There is also some work done on producing a GraphQL API as well as, but less has currently been implemented. 

That a REST API can be:-
1. Deployed to a cloud platform (Azure App Service)
2. Can provide metadata & docs via a discovery port
3. Can accept source files in both CSV & JSON format into an input data port
4. Can accept a data dictionary (aka schema) that defines the source files into an input data port
5. Can transform the source files into datasets stored in a relational database
6. Can provide those datasets in more than 1 format (JSON or CSV) to the output data port
7. Can be secured via basic authentication and authorisation also be imposed to prevent authenticated users who don't have permission to access a particular data set from doing so.
8. That the data set provided by the REST API can be consumed by a client application e.g Power BI

This should be sufficient to prove the concept. 

## Out of Scope for the PoC
There are other items that are not being proved but can utilise similar techniques as demonstrated above:-
For example:- 
* Accepting a Data Quality technical rules file via a control port would work in a similar fashion to item 3 in the list above.
* Storing metrics for audit purposes is simply capturing http info in the request and saving to a relational table and making the contents available via the Control Output Port. This is similar in concept to item 6. above.

Other factors aren't being demonstrated simply because solutions for these are already known. For example, the following docs/metadata can be linked to the data product using URLs:-
* Data Lineage diagrams can be generated in Collibra
* Data models in PowerDesigner 
* Data Sharing Agreements can be stored in Word docs on Sharepoint

<strong>Note: For demonstration to the business, those items as well as a [Data Marketplace](data-marketplace.md) will be mocked up.</strong>

Other factors aren't being demonstrated because they are more relevant for production than for a proof of concept e.g.
* Creating the app build and app deploy containers to allow a data product to be built and deployed to any major cloud platform 
* The API Gateway
* Linking to the enterprise authentication and authorisation systems. 

<strong>Note: Integrating an application into an enterprise authentication & authorisation system is non-trivial, typically taking months so is out of scope for the PoC.</strong>


 
## What tooling will be used in the PoC?

The choices made were for speed of delivery. Every organisation's delivery teams will undoubtedly have different tool choices in most cases, but it's a Proof of Concept, so tools can easily be swapped out so long as they provide the same functionality.

### Coding 
* Coding Language - [Python](https://www.python.org/). This will be used for Front end (using the [Python Flask](https://en.wikipedia.org/wiki/Flask_(web_framework)) module) and Back end  development simply due to familiarity with this language. 

<strong>Note: Most delivery teams will have their own preference for front end work, but the PoC is just demonstrating a concept.</strong>
* Integrated Development Environment (IDE) - [PyCharm](https://www.jetbrains.com/pycharm/) will be used to allow rapid coding of a REST API
* REST/GraphQL API module - [FastAPI](https://fastapi.tiangolo.com/) chosen because it's a Python module and is a fully featured API builder 

* Code Version Control Repository - [GitHub Repo](https://github.com/deytalytics/DataProductPoC)

### Data
* Relational Database - [SQLite](https://www.sqlite.org/index.html) - chosen because it's integrated into Python but can be built using Data Definition Language (DDL) scripts and data saved in relational tables using ANSI SQL

### Security
* Authentication & Authorisation - handwritten in Python, basic authentication only.

### Infrastructure 
* Cloud Platform - [Microsoft Azure](https://portal.azure.com)
* Cloud Platform Service - [Azure App Service](https://portal.azure.com/#@ShellCorp.onmicrosoft.com/resource/subscriptions/900a266e-8e11-47e1-a8e8-ba3ccfa9f292/resourceGroups/sbox-dataproduct-dev-rg/providers/Microsoft.Web/sites/t-and-s-dp-poc/appServices) 

<strong>Note: In production, a more sophisticated service solution e.g. [Azure Kubernetes Service (AKS)](https://azure.microsoft.com/en-us/products/kubernetes-service/) might be preferred.</strong>

## What data will be used in the PoC?

### Input Data
For simplicity, we will be using 2 CSV files as input:-
* Countries.csv
* Continents.csv

These will be uploaded to the input data port. 

### Transformation
Data pipelining sql can also be uploaded via the input data port which will fire transformation which will merge the data into a continents and countries dataset which will be saved in a relational database in the abstraction layer. 

### Output Data
This abstracted dataset will then be further transformed to json and csv files which will be made available to the data consumer from the output data port 

## What docs/metadata will be available in the PoC?
The REST API will provide standard OpenAPI docs via the /docs discovery endpoint. 
The description information will also include extra [data product metadata](dp-docs_and_metadata.md)

## How will the data consumer be able to consume the data product data?
* For a web application developer, the technical demo will demonstrate how to send http POST & GET requests to the REST API endpoints to obtain back responses with data and metadata.
* For a business user, the demo will demonstrate how a web application that they can access the [docs and metadata](dp-docs_and_metadata.md) about data products from a [data marketplace](data-marketplace.md) and securely access data by logging in from a web application and/or via Power BI.