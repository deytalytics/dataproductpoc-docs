# Data Product Naming & Versioning Standards

Data products need to be grouped by a business domain so a logical way of grouping will be:-
[\<organisation>\<business domain>\<data product>\<version>]()

You should resist the temptation to:-
* Grouping data products by IT systems as systems change over time and data products should align to the business rather than IT.

* Make data products follow a particular naming convention for the underlying technology/approach e.g. APIs may have their own naming convention but not all data products are APIs so are unlikely to all be delivered via a http url.

## Versioning
The general principle is that if a data product is put into production, strong change control should be enforced to ensure that data products are only changed if strictly necessary.

Versioning should follow the concept of breaking and non-breaking changes, where a breaking change will impact existing data consumers and a non-breaking change will not impact the data consumer 
Breaking changes should result in a major version number change i.e. 1.x to 2.x and non-breaking changes should result in a minor version number change e.g. 1.1 to 1.2


## API Naming & Versioning Standards
API naming & versioning should be controlled by an organisation's existing standards and enforced on an API Gateway/Management system
