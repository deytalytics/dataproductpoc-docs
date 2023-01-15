# Cloud Platform Deployment

[Cloud deployment models](https://k21academy.com/wp-content/uploads/2020/04/Cloud-CDeployment-Model-1-e1627451820602.png)

Although legacy database systems still exist on on-premise and, perhaps, there will be a return to organisation-maintained servers in the future
most modern applications need to be deployed to the cloud. 

Cloud platform deployment exists at various levels of complexity.

## Easy deployment
The easiest deployments are where the cloud platform's application service can automatically be built 
from GitHub (a version code repository)

For hobbyists, [Heroku](https://www.heroku.com/) used to be the go-to cloud platform due to it being free for small developments 
For enterprises, the following app services are easiest to use for proofs of concept:-
   * [Azure App Service](https://azure.microsoft.com/en-gb/products/app-service/)
   * [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/)
   * [Google Cloud App Engine](https://cloud.google.com/appengine) 

## Enterprise level deployment
The problem with the easy deployments is that they don't have the following characteristics that 
a more enteprise level deployment allows for.

1. Scalability
2. Containerisation
3. Multi-cloud platform support

For a more professional cloud platform, the code and data+metadata are typically containerised using [Docker](https://www.docker.com/) 
and encapsulated in [Kubernetes](https://kubernetes.io/) which provides the infrastructure related information that assists with scalablilty rules