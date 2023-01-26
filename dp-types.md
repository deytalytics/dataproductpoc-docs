# Data Product Types
In our PoC, we are mainly concentrating on REST APIs, with some work also being carried out for GraphQL APIs

The Data Product Type is API and the Data Product Subtypes for our PoC are REST and GraphQL

There are other potential data product types that have yet to be explored. 

It is important to identify data product types and subtypes as:- 
* From a data consumers perspective, being able to differentiate between types of data products on the data marketplace would be useful
* The technical mechanism for handling performance and security will tend to differ between different data product types

## Request-Response
APIs are used for Request-Response type scenarios 
i.e where a consumer or application wants a dataset and the API responds by providing the dataset.
Request-Response calls can either be single calls to an API or batched.

## Near Realtime Data Push Updates
Another common scenario is where an application service needs real time updates of changes of data from source. 
For example, an application service could be written that emails a new customer. 
The new customer could be initially registered on a sales system e.g. Salesforce 
and the sales system then pushes notifications of new customers via a stream or queue to the email application service

This data product type could be called Push with data product subtypes of Stream and Queue

## Files
Another scenario might be where a data consumer simply wants to access a File on cloud storage. This differs from API access in that there is no desire to filter records in the dataset prior to download.
This data product type could simply be called File with a Null data product subtype.