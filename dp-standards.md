# Data Product Naming & Versioning Standards

## Data Product Naming & Grouping

Standardised data product names need to be determined. These should relate to either a business domain or business domain rather than the data sets that the data product provides.

Data products need to be grouped by business domain/sub-domain appropriately.

For example, a data product that belongs to the UK sales department could be grouped (using metadata) under:-

organisation->sales
or 
organisation->uk

You should resist the temptation to:-
* Group data products by IT systems as systems change over time and data products should align to the business rather than IT.
* Make data products follow a particular naming convention for the underlying technology/approach e.g. APIs may have their own naming convention but not all data products are APIs so are unlikely to all be delivered via a http url.
* Include groupings in the data product name e.g. in the examples above, you shouldn't create a data product called organisation-uk-sales or organisation-sales-uk but should just call it uk or sales and provide the grouping as part of the metadata.

## Data Product Versioning
The general principle is that if a data product is put into production, strong change control should be enforced to ensure that data products are only changed if strictly necessary.

Versioning should follow the concept of breaking and non-breaking changes, where a breaking change will impact existing data consumers and a non-breaking change will not impact the data consumer 

Breaking changes should result in a major version number change i.e. 1.x to 2.x

Non-breaking changes should result in a minor version number change e.g. 1.1 to 1.2


## API Naming & Versioning Standards
API naming & versioning should be controlled by an organisation's existing standards and enforced on an API Gateway/Management system

### API Addressing 
As APIs use the http protocol the recommendation would be to use:-
```
https://<organisation>/<business domain>/<business sub-domain>/<api type(REST|GraphQL)>/<version>/<data set>/<data set version>
``` 
where ```<data set version>``` would be optional and default to latest.