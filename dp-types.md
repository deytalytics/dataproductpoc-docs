# Data Product Types

| Data Product Category | Data Product Type | Data Product Subtype | 
|:----------------------|:------------------|:--------------------:|
| Request-Response      | API               |         REST         |
| Request-Response      | API               |       GraphQL        |
| Request-Response      | Query             |         SQL          |
| Request-Response      | Storage           |         File         |
| Streaming             | Queue             |       Message        |  


Data Products can be broadly grouped into categories that describe how a data consumer wishes to access the data

## Request-Response
APIs are used for Request-Response type scenarios 
i.e where a data consumer (user or application) wants a dataset and the API responds by providing the dataset.
Request-Response calls can either be single calls to an API or batched.

### REST API
A REST API is the best known method for a consuming application to request data synchronously from a backend service.
This typically works well for small datasets. Query & Field parameters can be defined to filter on data that is returned.

### GraphQL
A GraphQL API is an attempt to overcome some of the limitations in REST API in that a REST API developer has to code lots of filters to provide 
desired functionality from a consuming application. That means re-work and may affect downstream systems. 
GraphQL allows the consuming application to POST a query message which allows for selection of a subset of data and filters to be applied.

### SQL Queries
Another type of Request-Response tech are SQL queries being issued to a backend relational database, warehouse or SQL endpoint for a data lake. 
In this scenario, the SQL Query generator posts the sql query via a Native/ODBC/JDBC driver and waits for a dataset to be returned as a result.
The significant advantage over the API approach is simply that SQL is much better known than GraphQL and is more powerful in that you can group, sort, filter, join freely

### Files
In a scenario where a data consumer simply wants to retrieve a file, this is also typically achieved via a http GET request followed by the file sent back as a reponse. Other technologies e.g. ftp or tcp can also be used. 

## Streaming
Another common scenario is where an application service needs real time updates of changes of data from source. 
For example, an application service could be written that emails a new customer. 
The new customer could be initially registered on a sales system e.g. Salesforce 
and the sales system then pushes notifications of new customers via a stream or queue to the email application service

### Queues
Queues allow near real-time data updates to be provided by a data producer and consumed <strong>asynchronously</strong> by a data consumer. 
Queues differentiate from REST APIs in that they:-
1. Provide asynchronous delivery i.e. a data consumer can fetch data when they want.
2. Buffer data
3. Use TCP rather than HTTP as the underlying transport protocol

Apache Kafka is the best known streaming technology that provides this functionality. 
It was originally developed for the Hadoop platform and is open source, but most organisations will use a cloud hosted version of Kafka because:-
1. Kafka is difficult to setup and administer
2. Hosted kafka solutions will provide clustering, security and resiliency.

### Why cannot data products be categorised on the way they are sourced?
A data product can source and combine data from a variety of data source types. 