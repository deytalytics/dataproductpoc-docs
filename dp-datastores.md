# Data Product data stores
In order to provide data to a data consumer, a data product needs to:-
  * Be able to store datasets as a payload
  * Secure access
  * Be able to provide sufficient documentation (metadata) to assist data consumers.

Zhamak's recommendation is to split a data product into 3 sections:-
  * Input Data Port
  * Abstraction Layer
  * Output Data Port

The reasoning is that the Input Data Port should be able to receive data in the form and structure that it is saved at source. 
The abstraction layer converts data as it's stored at source into a more standardised form 
e.g. Source data could be in a variety of formats (JSON, CSV, avro, parquet, yaml) whilst the abstraction layer could save these in relational format
The output data port then formats the abstracted dataset as desired e.g. json, csv, html

In order to facilitate the buildout of the data product, I've found the following data stores to be required:-
  
  * ## Security data store
  This should at the very least allow authorisation of endpoint paths to specific users/roles to be achieved.
  If desired more fine grained control of returned data can be provided
  
  * ## Metadata data store
  This should contain tables to hold:-
     * Name
     * Version
     * Link to data sharing agreement
     * Link to data consumption agreement
     * Link to data lineage diagram
     * Link to data models
     * Link to a data dictionary
  
   * ## Data data store
   This should be where the datasets that are stored at the input data port, abstraction layer and target data port are stored.

There is no specific technology that needs to be used for a data store but my recommendation would be that:-
1. It is a cloud-based data store - so that the data product can easily use it.
2. It is capable of storing data in a variety of formats, not just relational - this is important as web development doesn't always rely on relational databases.