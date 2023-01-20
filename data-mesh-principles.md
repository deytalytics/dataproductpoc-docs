# Data Mesh Principles

![image](https://images.squarespace-cdn.com/content/v1/5b2d3045e2ccd153f0ad5922/1632344527154-18X6X5U1NC4W3FC4VN32/Picture2.png)

## Domain-orientated decentralised data ownership & architecture 
Rather than having a central data governance & architecture team providing definitions and data quality rules for data that they have little experience with. 
The idea is that a data governance team which is closest to the business data be able to provide this role. 
e.g. a team of HR experts should govern HR data, finance experts should govern finance etc.
Note: There is still a need for a central architecture team to define standards, policies & guidelines, however, to ensure interoperability at the very least. 
This principle is just saying that within that framework, solution architecture teams close to the business should be free to create their own solutions. 

## Data should be treated as a product
It needs to be packaged up with associated [documentation and metadata](dp-docs_and_metadata.md) and controls in a similar way to how an application is treated.

The data product can be broken down into 3 main architectural components:-
   * Code
   * Data & Metadata
   * Infrastructure 

Code and Data & Metadata is expected to be containerised and utilise enterprise infrastructure

The data product should have defined roles & responsibilities associated with it
   * data product owner - the person responsible in the business for the data product
   * dataset owner - a person whose responsible for the datasets
   * data product developer - a developer who builds out the date product using a coding language.

3. Self-serve data infrastructure as a platform

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

4. Federated computational governance

This is the data mesh concept. 
Data products should be able to be deployed on any cloud or on-premises platform that is network accessible. 
Containerisation of data products using technologies such as Docker allows for consistent data product builds to occur.
Kubernetes allows for cloud-agnostic infrastructure deployement.
By defining standard interfaces for the ports/endpoints, data products can be controlled and discovered and documentation, metadata and data obtained.

## References
For more detail around these concepts, please refer to:-
* Martin Fowler's [data mesh principles](https://martinfowler.com/articles/data-mesh-principles.html) 
* Zhamak Dahgani's [data mesh](https://www.oreilly.com/library/view/data-mesh/9781492092384/) book