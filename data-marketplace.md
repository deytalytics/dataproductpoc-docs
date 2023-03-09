# Data Marketplace

A data marketplace is the shop window for data products.  
The users who visit the data marketplace are called “data consumers”. 

## Data Consumer Types
In laymans terms, a data consumer can be:-

* A non-technical user who will be looking for data products that are easily downloadable/accessible e.g. CSV files or Reports
* A technical user who additionally will be looking for data products that they can incorporate into the development of their application. For example:-
* An application developer might want to incorporate a dataset into their application by connecting to a Kafka queue or call a REST API endpoint
* A data analyst might want to query a dataset from a relational database, a file or a REST API endpoint and process the fetched data to produce a desired output
* A BI analyst may want to query a dataset from a relational database to produce an executive report. 

## Alignment to the business
Another significant factor that the data mesh/data product concept introduces is the need to align data products and datasets to specific business areas. 

So, if you work in Acme Department A, you should be able to view data products and datasets that are relevant only to your department and not have to wade through data products and datasets that are not relevant.

As with any business organisation, there are organisational hierarchies to consider, so some data consumers should be entitled to be able to see all data products and datasets relevant to the entire organisation, others just those that are relevant to a particular division, others just those that are relevant to a particular deparment, and within a department you may also want to restrict datasets from certain users.

## Data Marketplace audience requirements
So that only permitted and appropriate data products and datasets are provided to a data consumer, we will need to:-
* Identify particular data consumers – this means that we will need the data marketplace to have a single sign-on (SSO) capability
* Identify what data consumer type (non-technical/technical) they fit into
* Identify which area of the business they work in and at what level.

These identifications will be set up via the data product admin website, but the data marketplace will need to be able to use the information.

## Metadata
Metadata simply means information that we need to store so that it can be presented back to the data consumer via the data marketplace, so that they fully understand what the data product and datasets can provide.

There are going to be various types of metadata that need to be captured to support the data marketplace that relate to:-
* Data consumer 
* Data product 
* Datasets

### Data Consumer Metadata
Data consumer metadata needs to be stored so that we know everything about our target audience so that the correct data products are provided to them:- The following should be considered as a minimum set:-
* userid/email
* group/role(s)
* business area
* data consumer type (technical | non-technical)

### Data Product Metadata
A particular business area can create 1 or more data products.
Each data product will have a data product owner
Each data product can provide 1 or more datasets. 
The data product metadata should cover just what is required for a data product and not what is required for each dataset
The following should be considered to be the minimum required:-
* data product owner (name, contact)
* data product name
* data product version
* Last updated date
* Description
* Links to Datasets
* Links to data sharing agreement(s) 
Note: A data sharing agreement will need to be in place between the data product and any data sources that are supplying data to the data product.

### Dataset Metadata
Dataset metadata will provide the data consumer with full details as to what they can expect from the data

The following should be considered a minimum set of metadata:-
* Name
* Version
* Type (file, queue, relational database table, report, data science model)
* Last updated timestamp
* URL to data dictionary 
* URL to data model diagram 
* URL to data lineage diagram 
* URL to technical data quality rules 
* Latest technical dq rule results
* Access Methods - This could be a hyperlink to the dataset (if held as a downloadable file) and/or a URL to an information page which explains how to access the dataset (for other dataset types)

### Technology requirements
The data marketplace will need to:-
* Be created as a web application using an organisation's front end development language of choice
* Deployable to a cloud platform
* Integrated with the organisation's authentication & authorisation systems
* Able to query the data product data stores
* Able to connect to external tools/systems that provide additional documentation e.g. the data sharing agreements

### Application requirements
The data marketplace should:-
* Be visually appealing i.e. engage the audience with using imagery and wording that is meaningful to them.
* Provide intuitive navigation through the data marketplace e.g. If a data consumer is entitled to see all of their division's data products 
then they should be able to drill down to departmental data products.
* Only present data products to a data consumer that are relevant and they are permitted to access
* If it is anticipated that this would still result in a large number of data products and datasets for a data consumer to look at, then a search capability should be added so that they can look for specific data products. 

# Off-the-shelf Data Marketplace
If you're using Collibra as your data governance tool, it provides a [data marketplace](https://productresources.collibra.com/docs/collibra/latest/Content/DataMarketplace/to_dm.htm) which can utilise the data product & dataset metadata within Collibra.
Bear in mind that you may not be able to tailor such a solution sufficiently for your data consumers, however.


