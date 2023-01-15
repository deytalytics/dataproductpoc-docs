#Data Mesh Principles

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
   * A link to a data sharing agreement which explains the terms & conditions that are in place between the data product owner and data source owners
   * A link to a data consumer agreement which explains the terms & conditions that are in place in terms of change control and notification to data consumers
   * Information on how the data product can be accessed
The data product can be broken down into 3 main architectural components:-
   * Code
   * Data & Metadata
   * Infrastructure 
The data product should have defined roles & responsibilities associated with it
e.g. data product owner, data product developer etc

3. Self-serve platform

The data product should provide sufficient metadata and controls to allow it to be self-served. The capabilities include:-
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