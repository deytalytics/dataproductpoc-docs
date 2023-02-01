# Data Product Types

| Data Product Category | Data Product Type | Data Product Subtype | 
|:----------------------|:------------------|:--------------------:|
| Pull                  | API               |         REST         |
| Pull                  | API               |       GraphQL        |
| Pull                  | Streaming         |    Message Queue     |  


Data Products can be broadly grouped into categories that describe how a data consumer wishes to access the data

## Request-Response
APIs are used for Request-Response type scenarios 
i.e where a data consumer (user or application) wants a dataset and the API responds by providing the dataset.
Request-Response calls can either be single calls to an API or batched.

## Near Realtime Data Updates
Another common scenario is where an application service needs real time updates of changes of data from source. 
For example, an application service could be written that emails a new customer. 
The new customer could be initially registered on a sales system e.g. Salesforce 
and the sales system then pushes notifications of new customers via a stream or queue to the email application service

### Why cannot data products be categorised on the way they are sourced?
A data product can source and combine data from a variety of data source types.