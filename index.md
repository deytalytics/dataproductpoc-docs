# Introduction
This website documents how to practically create data products within a data mesh.
It is the instantiation of the architectural theory provided by Zhamak Dehgani in her [Data Mesh book](https://www.oreilly.com/library/view/data-mesh/9781492092384)

This documentation will be based on a data product with REST API at it's core.

It will cover the following topics:- 
1. The data mesh principles and what is a data product
2. The creation of the REST API
3. The creation of relational databases to store data captured from:-
   * Source to an Input Data Port/endpoint
   * Transformed into an abstraction layer
   * Formatted and sent via an Output Data Port/endpoint
3. The creation of the discovery endpoint which will allow information about the REST API to be discovered 
   i.e. human & machine readable documentation & data dictionary
4. The creation of a control endpoint which will allow metadata and data to be posted to the REST API
5. The documentation required:-
   * Standard REST API docs
   * A link to a data sharing agreement
   * A link to a data lineage diagram which describes the flow of data from the input data port to the output data port
   * A link to a data model of the dataset as seen at the output data port
   * A link to a data dictionary describing the fields in the dataset
6. Basic Authentication & Authorisation
7. How to deploy to a cloud platform
8. API naming and versioning
