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

Given these differences how can we ensure/improve performance?

Well if you consider that analytical systems are aggregating information, do data products necessarily have to hold aggregated data sets?
Remember 1 of the key features of the data product/data mesh concept is that they should be decentralised / federated?
Also, does any organisation provide detailed information in executive reporting? 
Typically higher level reporting involves summarising the detail. 

So data products could be made more efficient by:- 
* Holding the detailed data at a more granular level
* Holding summarised data in a higher level data product.

As data products have standardised interfaces, it will be easy to construct higher level data products from more granular data products.
![dp interoperability example](dp-interoperability.png)

## Reducing dataset size for BI reporting
With reports, the report developer really has 2 options:-

1. A direct query option. 
This option covers when a report is expected to directly query a data source. 
The easiest solution is to simply allow the report developer to be able to securely connect to the dataset database 
as a datasource. Grant/revoke policies will be applied to users/roles to restrict their ability to fetch certain datasets. 
Fine grained access control that can filter out certain fields or rows can also be implemented by using the permission information that
has been defined in the dataset authorisation database (which will be maintained via the data product admin website)
The report developer will be able to find the relevant metadata either by going to:-
   * The [data marketplace](data-marketplace.md)
   * The enterprise data catalog
   * Querying the metadata database directly.

2. An import option. 
In this scenario a query that would have been generated in the reporting tool
can have it's performance improved,  by injecting the query into the data product as pipeline SQL, essentially 
creating a data product that has the query resultset as a target dataset. 
This option works in scenarios where the resulting target dataset is relatively small. 

The import option is the recommended option for modern BI tools such as 
Power BI, as Power BI can apply more complex functions to imported datasets than are available in 
straight SQL.