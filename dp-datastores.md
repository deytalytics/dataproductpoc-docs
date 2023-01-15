# Data Product databases
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

In order to facilitate the buildout of the data product, I've found the following databases to be required:-
  
  * ## Security database
  This should at the very least allow authorisation of endpoint paths to specific users/roles to be achieved.
  If desired more fine grained control of returned data can be provided
  
  * ## Metadata database
  This should contain tables to hold:-
     * Name
     * Version
     * Link to data sharing agreement
     * Link to data consumption agreement
     * Link to data lineage diagram
     * Link to data models
     * Link to a data dictionary
  
   * ## Data database
   This should be where the datasets that are stored at the input data port, abstraction layer and target data port are stored.