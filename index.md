The information captured in this Wiki has been deduced by carrying out a [data product proof of concept (PoC)](dp-poc.md)

# Introduction
This website documents how to practically create data products within a data mesh.
It is the instantiation of the architectural theory provided by Zhamak Dehgani in her [Data Mesh book](https://www.oreilly.com/library/view/data-mesh/9781492092384)
which is in turn based on thinking formulated with [Martin Fowler](https://martinfowler.com/articles/data-mesh-principles.html) whilst at [ThoughtWorks](https://www.thoughtworks.com/)

The purpose of the proof of concept is to assist organisations in understanding how to build a data mesh and data products.

This documentation will be based initially on a data product with [REST API](https://aws.amazon.com/what-is/restful-api/) at it's core. 
The reasoning for this is:-
1. That Zhamak's background is in API architecture so her perspective naturally emerges from that area
2. Its the easiest data product type to create as its reasonably mature so has plenty of support and code examples 

Later these standards will be adapted for other data product types.

![Data Product Anatomy Diagram](dp-anatomy-diagram.jpg)

It will cover the following topics:- 
* [What is special about data products](dp-business-benefits.md)
* The [data mesh principles](data-mesh-principles.md) and what is a data product
* [High level data product architecture](dp-architecture.md)
* The creation of [data stores](dp-datastores.md) to store data captured from:-
   * Source to an Input Data Port/endpoint
   * Transformed into an abstraction layer
   * Formatted and sent via an Output Data Port/endpoint
* [Required Documentation & Metadata](dp-docs_and_metadata.md)
* The creation of the [discovery endpoint](dp-discovery-endpoint.md) which will allow information about the REST API to be discovered 
   i.e. human & machine readable documentation & data dictionary
* The creation of [control endpoints](dp-control-endpoint.md) which will allow:-
   * Metadata and controls to be posted to a controls input port
   * Audit logs to be pulled from a controls output port
* [Improving Data Quality](dp-data-quality.md)
* [Authentication & Authorisation](dp-authentication.md)
* How to [deploy to a cloud platform](cloud-platform-deployment.md)
* [Data Product naming and versioning standards](dp-standards.md)
   * [REST API naming and versioning standards](REST-api-standards.md)
   * [Data Set naming and versioning standards](ds-standards.md)
* [Improving Performance](dp-performance.md)
* [Capturing Metrics and Auditing](dp-audit-and-metrics.md)
* Creation of data models in a [data modelling tool](data-modeling-tool.md)
* Storage of metadata in a [data governance tool](data-governance-tool.md)
* Creation of a [data marketplace](data-marketplace.md)

[james.m.dey](mailto://james.dey@hotmail.com) January 2023james.m.dey](mailto://james.dey@hotmail.com) January 2023