# Data Product & Dataset Creation

When the data product admin team create a data product, they only actually have to configure information via:-

* The Enterprise Data Catalog (Collibra)
* The Data Product Admin Website.

Within the Enterprise Data Catalog the data product admin team can:-

* Enter data product and dataset metadata
* Create the technical data quality rules

Within the data product admin website, the team can:-

* Create, view and update the configuration information to connect to the persistent data stores and microservices container.
* Create, view and update data source configuration information
* Create, view and update the pipeline sql which is used to move datasets from the input to the output data layer
* Upload the pipeline sql to the microservices container
* Trigger the execution of the pipeline sql within the microservices container
* Maintain the dataset user/group permissions - Access control to the various datasets will be recorded in the dataset authorisation database and implemented as grants against data virtualisation views.

The microservices container will typically be created and deployed to the Azure cloud platform by an IT service team who will then provide the data product admin team with the connection information for the persistent data stores and microservices containers.

![Data product & dataset creation](data-product-creation.png)