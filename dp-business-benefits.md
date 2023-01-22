# What is special about data products?

For Analytics / Business Intelligence, the following are the main methods of storing data that will allow business users to be able to create/view analyticals information:-

## An operational data store (ODS)
This method effectively copies relational data at source with limited attempts to clean the data. 
It achieves this typically by capturing data from source logs and applying it to the ODS.
It's useful for running intra-day reports or reacting to source data changes
It's main disadvantages are that:-
  1. The capture-apply replication method isn't very scalaable so can only cope with relatively small data changes.
  2. It can only handle relational data

## An enterprise data warehouse (EDW)
This method was prevalent from 1990s through to 2000s. It involves:-
* Capturing relational data from source into a staging area
* Writing complex extract, transformation and load (ETL) scripts to push data into an enterprise data warehouse.

The problems with this approach are:-
1. Data warehouses are typically loaded as an overnight batch job so are not suitable for information that is updated intra-day
2. IT are in total control of the data that gets loaded into the data warehouse. Where the data is sourced from and how it is transformed is buried in the complex scripts
3. Knowing what data is available in the enterprise data warehouse is also often in the gift of IT
4. To create an enterprise data warehouse typically takes years and any requests to add or update it typically takes months.

## A data lake

By the late 2000s, it became apparent that analytics would need to be able to cope with much larger volumes of data, process the data more rapidly and be able to deal with more than just relational data. Fortuitously, data storage costs came down significantly around the same time.

Due the identified ODS and EDW, organisations realised that they needed a better solution, so data lakes emerged. 
A data lake involves:-
* Operational systems writing data to the data lake as raw data files in a variety of formats
* Data pipelining scripts can then run to merge data from different files and clean it so that its of good enough quality for use in analytics.

A data lake avoids expensive updates of existing data, so can cope with much larger volumes of data and much more quickly than previously. For data scientists, they were also able to start writing scripts against the raw data captured in the data lake without waiting for IT to clean up the data. This gave a speed to market benefit.

The downsides of a data lake include:-
1. As the raw data is stored in a variety of formats, it originally required IT to be able to write code to extract analytics for business users. Later SQL interfaces partially circumvented this problem, however.
2. Physically stored data is typically not understandable to anybody who doesn't work in IT and isn't familiar with the source systems.
3. Business users cannot easily get access to data in the data lake nor discover what data is in there. 
4. Raw data in the data lake is of poor quality and hence cannot be trusted.
5. Data security is often a problem with data lakes as it can be the case that a user who is given access to a data lake can see files that they should not be permitted to see.

# Data Products
So data products are stepping in to solve this problem. They provide the following key benefits:-

1. A [data marketplace](data-marketplace.md) - which will allow a user to search for data products by business function.
2. [Documentation](dp-docs_and_metadata.md) - each data product will contain documentation which allows the user to fully understand what the data product can provide, where it came from, how good quality it is etc.
3. Improved [security](dp-authentication.md) - access to data products will be via organisation's preferred authentication systems and only accessible, if authorised.
4. Better trusted - data product documentation will identify where data has come from, when it was updated and what data quality rules have been applied
5. Better alignment with the business - As business users will be able to search for data products grouped by their functional area, they will be able to be able to read the documentation and examine the data product data for themselves. This will help to easily identify problems with the data both within their business area and across business areas for data that needs to be reported on at a higher level. For example, a UK sales team might observe that in their sales system, amounts are stored in £ and convertable to $ and €, whereas the France Sales Data Product only has the currency in €. They could then work with their French colleagues on coming up with a common data product standard that would work for both teams.
6. More efficient - Enterprise data warehouses and data lakes end up as large monoliths of data. This was similar to the situation that existed with application code up until 1990s. Application coders realised that the way to improve things was to split monolithic applications into microservices. Data products can follow the same path.
For example, in the case of an enterprise data warehouse, you typically join all of your sales data from multiple systems and store in a sales table which can be diced and sliced by a number of dimensional tables e.g. country. When you write a report, you might then filter on country. So you've built a large sales table and are then decomposing it when you query it.
However, in the case of a data product, you could create:-
   * A sales data product for each country
   * And then an aggregated sales data product for each continent
   * And finally a global sales data product. 
The user can then decide which level of data product they want to use in a particular report. This is much more efficient. 
7. Able to source and provide data in a variety of formats - For example, most business users would most likely want to view data as csv files so that they can use Excel, whereas web application developers typically want to deal with data in JSON file format. 
8. Interoperable - by providing standardised interfaces for data products, data products can be linked together like Lego bricks to provide much more sophisticated solutions.