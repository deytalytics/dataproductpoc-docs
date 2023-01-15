# Introduction
This website documents how to practically create data products within a data mesh.
It is the instantiation of the architectural theory provided by Zhamak Dehgani in her [Data Mesh book](https://www.oreilly.com/library/view/data-mesh/9781492092384)
which is in turn based on thinking formulated with [Martin Fowler](https://martinfowler.com/articles/data-mesh-principles.html) whilst at [ThoughtWorks](https://www.thoughtworks.com/)

The purpose of the proof of concept is to assist organisations who are struggling to build a data mesh and data products.

This documentation will be based on a data product with [REST API](https://aws.amazon.com/what-is/restful-api/) at it's core. 
The reasoning for this is:-
1. That Zhamak's background is in API architecture so her perspective naturally emerges from that area
2. Its the easiest data product type to create as its reasonably mature so has plenty of support and code examples 

![Data Product Anatomy Diagram](dp-anatomy-diagram.jpg)

It will cover the following topics:- 
1. The [data mesh principles](data-mesh-principles.md) and what is a data product
2. The creation of the REST API
3. The creation of [data stores](dp-datastores.md) to store data captured from:-
   * Source to an Input Data Port/endpoint
   * Transformed into an abstraction layer
   * Formatted and sent via an Output Data Port/endpoint
4. The creation of the [discovery endpoint](dp-discovery-endpoint.md) which will allow information about the REST API to be discovered 
   i.e. human & machine readable documentation & data dictionary
5. The creation of [control endpoints](dp-control-endpoint.md) which will allow:-
   * Metadata and controls to be posted to a controls input port
   * Audit logs to be pulled from a controls output port
6. The documentation required:-
   * Standard REST API docs which provides:-
      * API Name
      * API Version
      * API Query & Field Parameters
      * A playground for a web developer to test access to the API
   * A link to data sharing agreements between
      * Data source owners and the data product owner
      * The data product owner and data consumers
   * A link to a data lineage diagram which describes the flow of data from the input data port to the output data port
   * A link to a data model of the dataset as seen at the output data port
   * A link to a data dictionary describing the fields in the dataset
7. [Authentication & Authorisation](dp-authentication.md)
8. How to [deploy to a cloud platform](cloud-platform-deployment.md)
9. API naming and versioning
10. Performance
11. Metrics
12. Creation of data models in a [data modelling tool](data-modeling-tool.md)
13. Storage of metadata in a [data governance tool](data-governance-tool.md)
14. Creation of a [data marketplace](data-marketplace.md)

[james.m.dey](mailto://james.dey@hotmail.com) January 2023