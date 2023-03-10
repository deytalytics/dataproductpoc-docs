# Data Product Naming & Versioning Standards

From a data consumer's perspective, data products:- 
* Are catalogued on a [data marketplace](data-marketplace.md)
* Provide [datasets](ds-standards.md) for consumption.

When naming & versioning data products, we need to make the distinction between the data product, 
the [data product type](dp-types.md) (e.g. REST API) and the [dataset](ds-standards.md)

## Data Product Naming & Grouping
Standardised data product names need to be determined. 
These should relate to either a business domain or business subdomain 
rather than the data sets that the data product provides or the systems that provide the data

Data products need to be grouped by business domain/sub-domain appropriately.

For example, a data product that belongs to the UK sales department could be grouped (using metadata) under:-

organisation->sales
or 
organisation->uk

You should resist the temptation to:-
* Group data products by IT systems as systems change over time and data products should align to the business rather than IT.
* Make data products follow a particular naming convention for the underlying technology/approach e.g. APIs may have their own naming convention but not all data products are APIs so are unlikely to all be delivered via a http url.
* Include groupings in the data product name e.g. in the examples above, you shouldn't create a data product called 
```<organisation>/uk/sales``` or ```<organisation>/sales/uk``` but should just call it uk or sales and provide the grouping as part of the metadata.


## Data Product Versioning
The general principle is that if a data product is put into production, strong change control should be enforced to ensure that data products are only changed if strictly necessary.

Versioning should follow the concept of breaking and non-breaking changes, where a breaking change will impact existing data consumers and a non-breaking change will not impact the data consumer 

Breaking changes should result in a major version number change i.e. 1.x to 2.x

Non-breaking changes should result in a minor version number change e.g. 1.1 to 1.2

# Data Product Addressing 
Data products should be assigned uniform resource identifiers within the metadata with the following path format:-
```
http://data.<organisation url>/<business area>/<data product>/<data product version>
```
So in our PoC example we have a single data product with just 1 version :-
```
http://data-acme/data_architecture/data_product_poc/0.1
```

```<Business area>``` can be hierarchical so you could have:-

```
http://data.acme.com/IT/data_architecture/data_product/0.1
http://data.acme/Europe/UK/sales/data_product/0.1
http://data.acme/North America/USA/sales/data_product/0.1
```
