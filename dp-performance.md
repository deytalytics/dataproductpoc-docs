# Performance

## Operational vs Analytical systems

Operational systems (e.g. Salesforce or a web application) typically:-
* Create small raw data sets that are designed for a specific use case and often unique to a single operational system
* Transfer small data sets between systems via APIs using the http protocol. 
* Provide restricted data sets with a limited ability to filter the results

Analytical systems (enterprise data warehouses & data lakes), by contrast, typically:-
* Create fact tables that aggregate and transform information from multiple operational systems 
* Transfer larger data sets using proprietary drivers that ensure that data is transferred as 
efficiently as possible. 
* The end user can often control the contents of the returned data set by directly 
writing SQL or using a business intelligence tool that converts their requirements into a SQL query. 
SQL provides much more sophisticated control over what will be returned in a data set. 

## Improving performance 

Given these differences how can we improve performance?

Well if you consider that analytical systems are aggregating information, do data products necessarily have to hold aggregated data sets?
Remember 1 of the key features of the data product/data mesh concept is that they should be decentralised / federated?
Also, does any organisation provide detailed information in executive reporting? 
Typically higher level reporting involves summarising the detail. 

So data products could be made more efficient by:- 
* Holding the detailed data at a more granular level
* Holding summarised data in a higher level data product.

As data products have standardised interfaces, it will be easy to construct higher level data products from more granular data products.

There is also nothing to prevent a data virtualisation layer being added with views that pull data sets from data products, cache them and 
present them so that they can be queried by business intelligence tools in the normal fashion.
The standardised interfaces that data products provide make the construction of such a data virtualisation layer easier to develop.

## Reducing dataset size for Power BI reporting
With reports, the report developer can create a Power BI report in the normal fashion. 
Then when there is a need to put the report into production, the SQL query can be used as the data pipeline sql within a data product.
The Power BI report can then connect to the higher level data product that will return the desired result set. 
