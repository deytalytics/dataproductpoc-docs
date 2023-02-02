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

### Service/App authorisation
This type of authorisation just ensures that a particular user/role is permitted to access a particular service/app. Dependent on the authorisation system used it may be able to authorise just a service/app or a particular endpoint on a service/app.
Identity & access management systems such as Azure Active Directory typically just provide authorisation at this level

### Fine grained access control authorisation
If more fine grained access control is required e.g. as is typically the case in a relational database or a file store, then a different authorisation system needs to be employed.
For data products, we'd ideally be able to be able to ensure that only particular users/roles can be given access to a particular dataset and possibly fields within that dataset.

# Implementing Authentication & Authorisation within an Organisation
![Proposed authentication & authorisation architecture](dp-authentication.png)

## Machine to machine authentication & authorisation
When an application/system needs access to data products:-
1. Token based authentication should be used 
2. Access to the data products should be via a gateway
3. The gateway can then check the token with an authentication system and check that the application/system is allowed access to the data product (minimal) or data product endpoint (preferred) via an authorisation system.

## User to machine authentication & authorisation
When a user wants to access a data product, then the problem is that only consumer facing applications know who that user is. 
The user's credentials are typically not passed back to back end systems, and it's usually deemed bad practice to do so. 
For example, Microsoft typically advise that any application that they host be authorised using a personal access token that is owned by the "service principal" (the account that created the app/service)
In the case of Power BI, even if it was possible for a Power BI desktop user to be able to pass their credentials to a data product, when the report is deployed to Power BI Service, it can only retrieve a dataset from the data product using a single account. 

So in the case of Power BI, user authentication & authorisation needs to occur in the consumer application.
For example, if a power BI report is created that accesses an organisations sales information, then in this scenario, access to the data product will be controlled by machine to machine authorisation and authentication by passing a personal access token generated for the service principal. 
A particular user will be authenticated using the organisations standard identity and access management system e.g. Azure Active Directory.
A Power BI administrator will ensure that user is given authorised access to the report, not a particular dataset.

## Fine Grained Authorisation
Where fine grained data authorisation is required e.g. to omit sensitive field data, 
the easiest method would be to create 2 versions of a dataset e.g.
* customers/0.1
* secure-customers/0.1

The consuming web application/tool can then incorporate the specific dataset into a web page or report 
The webpage/report could then display the appropriate dataset that the user is entitled to see.