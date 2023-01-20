# Data Product - Discovery Endpoint

The purpose of a discovery endpoint is so that a human being and a machine should be able to discover information and documentation
about the data product from the data product itself. 

For human beings, the discovery endpoint needs to make the [documentation and metadata](dp-docs_and_metadata.md) available in HTML format.
For machines, the documentation and metadata should be obtainable from the discovery endpoint in JSON format 

## Documentation for specific data product types
### REST API
* REST API should follow the OpenAPI standard which presents a webpage from /docs to a developer with the following metadata :-
  * Name
  * Version
  * Query and field parameters
  
  The /docs webpage also allows a developer to test the REST API endpoints by authenticating and passing in query parameters

### GraphQL
  The GraphQL standard allows a developer to access information about the GraphQL API from the /graphql endpoint  