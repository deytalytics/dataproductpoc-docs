# Introduction
This website documents how to practically create data products within a data mesh.
It is the instantiation of the architectural theory provided by Zhamak Dehgani in her [Data Mesh book](https://www.oreilly.com/library/view/data-mesh/9781492092384)

The purpose of the proof of concept is to assist organisations who are struggling to build a data mesh and data products.

This documentation will be based on a data product with REST API at it's core. The reasoning for this is that Zhamak's background is in API architecture and its the easiest data product type to create 

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
   * Standard REST API docs
   * A link to a data sharing agreement
   * A link to a data lineage diagram which describes the flow of data from the input data port to the output data port
   * A link to a data model of the dataset as seen at the output data port
   * A link to a data dictionary describing the fields in the dataset
7. [Authentication & Authorisation](dp-authentication.md)
8. How to deploy to a cloud platform
9. API naming and versioning
10. Performance
11. Creation of data models in a data modelling tool
12. Storage of metadata in a data governance tool
13. Creation of a data marketplace

[james.m.dey](mailto://james.dey@hotmail.com) January 2023