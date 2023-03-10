# Data Set Naming & Versioning Standards

A data product can make available multiple data sets. For example in our PoC, we have created the following data sets:- 
* countries
* continents
* continents_and_countries

# Naming
* Data sets should be given names that reflect their content
* Data set names should be in lowercase.
* Where data set names would include a space e.g. "customer sales", the space should be replaced with an underscore e.g. customer_sales

# Versioning
Over time, data set fields/attributes in many ways 
e.g. Field names or datatypes might change
The data set may have fields added or removed.

These changes would have an impact on data consumers. 

It is therefore important that a history of data set changes are tracked so that data consumers can request up to 3 older versions of a data set so as to ensure that data consuming applications can migrate to the latest version in a reasonable time and without breakages.

Note: A data set only has to re-versioned whenever structural changes are made. Each load is not considered a new version.

# Data Set Addressing 
Data sets should be assigned uniform resource identifiers (uris) within the metadata with the following path format:-
```
http://data.<organisation url>/<business area>/<data product>/<data product version>/<data set>/<data set version>
```
So in our example we have:-
```
http://data.acme.com/data_architecture/data_product_poc/0.1/countries/0.1
http://data.acme.com/data_architecture/data_product_poc/0.1/countries/0.1
http://data.acme.com/data_architecture/data_product_poc/0.1/continents_and_countries/0.1
http://data.acme.com/data_architecture/data_product_poc/0.1/continents_and_countries/0.2
```

```<Business area>``` can be hierarchical so you could have:-

```
http://data.acme.com/IT/data_architecture/data_product/0.1/countries/0.1
http://data.acme.com/Europe/UK/sales/data_product/0.1/customers/0.1
http://data.acme.com/North America/USA/sales/data_product/0.1/customers/0.1
```

Although it may seem that the dataset uris have unnecessarily long names, this covers the data mesh principle around addressability. 
The long names also greatly assist in understanding which part of the organisation is responsible for maintaining the dataset
