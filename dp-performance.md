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

As data products have standardised interfaces this should be achievable.

Further efficiency can be provided by allowing field parameters to be passed to the data product that would allow 
a data product such as a REST API to simulate some of what SQL can achieve.
e.g. the REST API developer could code to return a grouped, ordered and filtered UK food sales data set if the following query parameters were provided.

```https:acme.com/europe/uk/REST/0.1/sales/0.1?group_by=sales_date&order_by=customer_id&product_type='Food'```

There is also nothing to prevent a data virtualisation layer being added with views that pull data sets from data products, cache them and 
present them so that they can be queried by business intelligence tools in the normal fashion.
The standardised interfaces that data products provide make the construction of such a data virtualisation layer easier to develop.