# Data Mesh Principles

![image](https://images.squarespace-cdn.com/content/v1/5b2d3045e2ccd153f0ad5922/1632344527154-18X6X5U1NC4W3FC4VN32/Picture2.png)

1. Federated data governance 
i.e. rather than having a central data governance team providing definitions and data quality rules for data that they have little experience with. 
The idea is that a data governance team which is closest to the business data be able to provide this role. 
e.g. a team of HR experts should govern HR data, finance experts should govern finance etc.

2. Data should be treated as a product
i.e. It needs to be packaged up with associated documentation and controls in a similar way to how an application is treated.
Documentation should include:-
   * Data product Name (should follow a naming standard)
   * Version (should follow versioning standards)
   * A link to a data lineage diagram showing how data has flowed from source
   * A link to a target data model showing how datasets are stored in the data product
   * A link to data sharing agreements which explains the terms & conditions that are in place between:-
     * The data product owner and data source owners 
     * The data product owner and data consumers
   * Information on how the data product can be accessed

The data product can be broken down into 3 main architectural components:-
   * Code
   * Data & Metadata
   * Infrastructure 

The data product should have defined roles & responsibilities associated with it
   * data product owner - the person responsible in the business for the data product
   * dataset owner - a person whose responsible for the datasets
   * data product developer - a developer who builds out the date product using a coding language.

3. Self-serve platform

The data product should provide sufficient metadata and controls to allow it to be self-served. 
The capabilities include:-
   * Scalable polyglot big data storage
   * Encryption for data at rest and in motion
   * Data product versioning
   * Data product schema
   * Data product de-identification
   * Unified data access control and logging
   * Data pipeline implementation and orchestration
   * Data product discovery, catalog registration and publishing
   * Data governance and standardization
   * Data product lineage
   * Data product monitoring/alerting/log
   * Data product quality metrics (collection and sharing)
   * In memory data caching
   * Federated identity management
   * Compute and data locality