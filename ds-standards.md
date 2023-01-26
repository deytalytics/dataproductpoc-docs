# Data Set Naming & Versioning Standards

A data product can make available multiple data sets. For example, from the output data port, if a REST API is built, it could provide countries, continents or geography data sets with:-
http://<hostname>/REST/<version>/<object>
e.g. 
* http://data-products.acme.com/REST/0.1/countries
* http://data-products.shell.com/REST/0.1/continents
* http://data-products.shell.com/REST/0.1/geography

In addition to this, data sets which capture the data at source in the input data layer and data sets which abstract the data in the transformation/abstraction layer are also required.

# Naming
Data sets should have business meaning and be unique for their purpose
e.g. If there is a distinctive difference between the way that Sales rather than Marketing store customer information then the 2 data sets should be differentiated. sales_customer and marketing_customer

# Versioning
Over time, data set fields/attributes in many ways 
e.g. Field names or datatypes might change
The data set may have fields added or removed.

These changes would have an impact on data consumers. 

It is therefore important that a history of data set changes are tracked so that data consumers can request up to 3 older versions of a data set so as to ensure that data consuming applications can migrate to the latest version in a reasonable time and without breakages.