# Authentication & Authorisation

![Authentication vs Authorisation](https://miro.medium.com/max/413/0*nrG185aDIksAga3W.jpg)

Apart from public data, most organisation's data needs to be secured. 

In terms of a data product, security will need to cover authentication and authorisation of a user.

This particular topic is one of the hardest parts of implementing a data product as each organisation has their 
own established ways of authenticating and authorising users/systems which in my experience can take weeks to establish.

## Authentication
Authentication means ensuring that a user is who they say they are. There are many methods of authenticating a user. 
These include:-

### Basic Authentication
This is a simple username and password which are typically combined, base-64 encrypted and passed to a data product in the header of a http request.
This type of authentication is the easiest to implement but also the least secure, due to base64 being relatively easy to hack. 

### Multi-factor authentication
Takes authentication to the next level by requiring a user/system to authenticate by more than 1 method 
e.g. 
1. the user is asked to type their username and password in a web browser
2. The user is also required to confirm their identity typically by:-
   * Sending a text or email which the user either has to click a link or copy a one-time password in to the web page
   * Using an identity provider app to confirm their identity. When done, they are returned to the original website
   * Being redirected to an identity provider website to confirm their identity. When done, they are returned to the original website
   Common examples of trusted identity providers include:-
   * PingID
   * Microsoft
   * Google
   * Facebook
   * Linkein

## Token based authentication
   Token based authentication can involve:-
   1. A developer registering their application with another application that they wish to communicate with. During registration, a SHA256 (or similar) encrypted token can be generated and together with an API key or Client ID and Client secret ensures that only registered applications can gain access.

   More complex flows e.g. OAUTH2, ensure that the registered application is who they say they are and not another application imitating it by going through a more complex authentication flow which involves swapping the registered token with an access token by sending the response back to the registered application's callback url :-
   * the server application providing information that was previously registered with the authentication system
   * the authentication system responding to a server application url which was previously registered.
   * the server application redirecting the user to the authentication system to securely authenticate
   * the authentication system responding with an access token to a callback url on the server application
   * the server application can subsequently use the access token (which periodically typically needs to be refreshed) to authenticate as the user

## Authorisation
Authorisation means ensuring that an authenticated user is permitted to access the requested data.
Authorisation is a loaded term. So needs to be split down further for clarity.

### Data Product Authorisation
This type of authorisation just ensures that a particular user/role is permitted to access a particular data product. 
Dependent on the authorisation system used it may be able to authorise the data product in it's entirety or specific endpoints.
So, for example, it may be desirable to allow free access to the Discovery port/endpoint so that anybody can view the data product documentation, but restrict access to the output data ports
to a particular set of users, and restrict access to the input data port and control data port to specific roles.

### Dataset authorisation
As a data product can provide more than 1 target dataset, it is also desirable to provide more fine grained access control at the dataset level.

# Implementing Authentication & Authorisation within an Organisation
![Proposed authentication & authorisation architecture](dp-authentication.png)

# REST API authentication and authorisation
For REST APIs, the approach should be the following:-

1. The data product admin website should register users and record permissions against specific data products and data sets.
2. An authentication system should be built that allows an ID token to be generated for a particular user. The 1st time that a user logins to their laptop, a call should be made to the authentication system to validate the user and store the ID token on their computer.
3. Whenever a front end application needs to know who the user is then it should call the authentication system that will respond with the user's details and the ID token.
4. The frontend application can then send the ID token rather than the userID to a REST API gateway or REST API making this secure.
5. The REST API can then call the authentication system (if desired) to get the userID
6. The REST API can then query the dataset auth permissions in the persistant data store using either the userID and/or the ID token to see if the user is allowed to access a particular dataset.

# Relational Database authentication & authorisation
1. In this scenario, the necessary grants on tables to particular users/groups should be applied using the information in the dataset auth database against the tables in the dataset database. This logic can be run from the data product admin website.
2. The reporting or sql query tool will typically already have been connected to the authentication system so it knows who the user is.
3. When a reporting or sql query tool wishes to query a dataset in the dataset database then they need to passthrough the userid to the database which then needs to be able to run a query as though it was the passed through user.

# Queue authentication & authorisation
Tbd