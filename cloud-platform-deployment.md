# Cloud Platform Deployment
Although legacy database systems still exist on on-premise and, perhaps, there will be a return to organisation-maintained servers in the future
most modern applications need to be deployed to the cloud. 

Cloud platform deployment exists at various levels of complexity.

## Easy deployment
The easiest deployments are where the cloud platform's application service can automatically be built 
from GitHub (a version code repository)

For hobbyists, Heroku used to be the go-to cloud platform due to it being free for small developments 
For enterprises, Azure App Service, AWS Elastic Beanstalk, Google Cloud App Engine are the 3 easy cloud deployments. 

## Enterprise level deployment
The problem with the easy deployments is that they don't have the following characteristics that 
a more enteprise level deployment allows for.

1. Scalability
2. Containerisation
3Multi-cloud platform support

For a more professional cloud platform, the code and data+metadata are typically containerised using Docker 
and encapsulated in Kubernetes which provides the infrastructure related information that assists with scalablilty rules