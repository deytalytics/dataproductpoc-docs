# REST API Naming & Versioning Standards
<strong>Note: Do not confuse Data Product naming & versioning with the way in which you name REST APIs. 

Data Product metadata will be used by the [data marketplace](data-marketplace.md) and will include information about how to get to the REST API address</strong> 

REST API naming & versioning should be controlled centrally so that different parts of the organisation don't use different names for the same thing e.g. 1 part of the organisation creates a url:- https://shell.com/trading-and-supply/shell-energy/slmt whilst another part refers to https://shell.com/Trading_and_Supply/Shell_Energy_US 
REST API naming & versioning can be enforced by imposing the standards on an API Gateway/Management system rather than leaving it to individual development teams.

It is unimportant how the REST API is named locally but it is very important that it is standardised on the API Gateway

For example, if dev team A creates a REST API:-
https://acme.com/sales/uk
and DEV team b creates:-
https://acme.com/northamerica/usa/sales

On the API gateway, these can be linked to standardised REST API addresses:-
https://data-products.acme.com/north-america/usa/sales
https://data-products.acme.com/europe/uk/sales

if that is the standard that has been decided upon.

## REST API URL Addressing 
As REST APIs use the http protocol the recommendation would be to use:-
```
https://data-products.<organisation>/<business domain>/<business sub-domain>/<data product type>/<data product subtype>/<data product name>/<data product version>
``` 
where ```<business domain>, <business-sub-domain>``` are optional

## REST API Datasets
Datasets that are to be provided via the REST API should follow the [Dataset Naming & Versioning Standards](ds-standards.md)

The dataset routes should be added to the REST API URL in the form:-
```<dataset name>/<dataset version>```

For example, a REST API which would allow you to access the latest european sales deals would be:-
https://data-products.acme.com/europe/sales/api/REST/data_product_poc/1.0/sales

And if the data consumer wanted v0.1 of the uk's sales dataset they'd access it via:-
https://data-products.acme.com/europe/uk/sales/api/REST/data_product_poc/1.0/sales/0.1
