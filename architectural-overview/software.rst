.. _software:

Application Layout
==================

The all-py framework is constructed from components and plugins in order to allow for a flexible, layered and well organized customization of features.
The first problem in having an application formed of smaller parts like in our case the components and plugins is how you can bring them together to function as one, in this respect
we use the inversion of control [IoC]_ pattern. To handel the [IoC]_ we created a container that handles this, the implementation is found in the core component ``ally`` in package
``ally.container``. A general approach in [IoC]_ is to use XML configuration files, but this container is designed to be used with standard python modules.


Lets have a view over the major components of the framework.

+-------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Component                           | Depends on                                       | Description                                                                                                                 |
+=====================================+==================================================+=============================================================================================================================+
| ``ally``                            | \-                                               | This is the main component and is the application entry point.                                                              |
|                                     |                                                  | This component provides also support for inversion of control container.                                                    |
|                                     |                                                  | Basically this component contains general support for the application that is not in any way linked with a particular       |
|                                     |                                                  | technology.                                                                                                                 |
+-------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``ally-http``                       | ``ally``                                         | Contains HTTP specific handling for requests and also the basic HTTP server based on the python built in server.            |
+-------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``ally-http-asyncore-server``       | ``ally-http``                                    | Provides an HTTP server substitute for the basic server from ``ally-http`` that handles the requests in an asyncore manner  |
|                                     |                                                  | by using the python built in ``asyncore`` package.                                                                          |
+-------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``ally-http-mongrel2-server``       | ``ally-http``                                    | Similar to the asyncore server but provides support for using [0MQ]_ messaging in order to communicate with [Mongrel2]_     |
|                                     |                                                  | HTTP server.                                                                                                                |
+-------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``ally-plugin``                     | ``ally``                                         | This component handles the plugins and incorporates them in the application.                                                |
+-------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``ally-indexing``                   | ``ally``                                         | The indexing is a component that provides the vocabulary for understanding the index table in the responses, the indexes    |
|                                     |                                                  | provide the mechanism for data aggregation by a proxy server and security filtering at a property level.                    |
+-------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``ally-api``                        | ``ally``                                         | Provides the means of decorating the [REST]_ models and services.                                                           |
+-------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``ally-core``                       | ``ally-api``, ``ally-indexing``                  | Provides the general support for handling the [API]_ services that have been decorated as [REST]_ services.                 |
+-------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``ally-core-http``                  | ``ally-core``, ``ally-http``                     | This component provides the actual handling for the HTTP [REST]_ by combining the ``ally-core`` and ``ally-http``.          |
+-------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``service-assemblage``              | ``ally-http``, ``ally-indexing``                 | This component provides the data aggregation service based on the response indexes.                                         |
+-------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``service-gateway``                 | ``ally-http``, ``ally-indexing``                 | This component provides the gateway security service.                                                                       |
+-------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``service-cdm``                     | ``ally-http``                                    | This component provide the content delivery management, basically the static resources streaming since [REST]_ is only      |
|                                     |                                                  | for models, usually the REST models will have references to static files, like media files and the CDM is used for delivery |
|                                     |                                                  | them.                                                                                                                       |
+-------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+

So what is the reasoning of splitting the application in this components, the most important aspect is the fact that the application deployment can be done in multiple ways.

Lets consider the application [REST]_ base composed of ``ally``, ``ally-http``, ``ally-api``, ``ally-core``, ``ally-core-http``, ``ally-plugin`` and **plugins**, this combination provides the base for a [REST]_ application that allows us to implement
simple plugins with no support for database support, security, data aggregation or content delivery. As it can be seen for a [REST]_ server we don't need all the components.

.. image:: images/application-rest-base.jpg

So we have web application that is able to provide [REST]_ type model responses, this is great but usually not enough for a complex web application, we need more.
Lets consider a [REST]_ model designed to provide internationalization support that will provide references for [PO]_ files, in this case we also need someone to stream the [PO]_ file.
The [REST]_ server is not designed to do that, it is designed to provide only [REST]_ models. So in order to solve this we have the ``service-cdm`` component to stream static files.

.. image:: images/application-rest-cdm.jpg

Now the web server is able to deliver [REST]_ and also static files from the file system. The CDM service also streams the application client files (java script) for the client.
In an enterprise type application you need to have the ability to scale, in this concern the CDM can actually be placed on an external machine(s) or be replaced by external HTTP streaming servers.
Even when the web server is started using [Mongrel2]_ the content is delivered directly by the [Mongrel2]_ server rather then the CDM application, even if the CDM service is present will be automatically deactivated.

.. image:: images/application-cdm.jpg

Now we have the RESTful application on a server and the content files streaming on a different server.
What is the point for this?
First of all we can deliver the application as a simple all together python application with no external dependencies (outside python libraries) to normal users that do not have such high traffic and only want
and easy to install application that can serve their needs at this point.
If the user has a great success and the traffic demands increase we also are able to scale by simply externalizing the static file delivery system to more powerful system and event more then that by externalizing the
proxy servers (gateway and aggregation) or sardining the RESTful server.
For instance we use [0MQ]_ as the application messaging service with [Mongrel2]_ as the server we can start as many application instances as we need depending on the traffic since the RESTful server is stateless.
The main goal here is to address the needs of normal users but also the needs of enterprise level customers by using the same plugins and components.

The content file system service is a simple one, for the other services we usually need more information that is provided by the core plugins. A plugin is like a component except that the purpose of the plugin
is to publish REST models rather then influence the application behavior.
As a general rule all plugins that provide REST models depend on ``ally-api``. Lets have a view over the major core plugins of the framework that are used by the proxy services (``service-assemblage``, ``service-gateway``).

+-------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Plugin                              | Depends on                                       | Description                                                                                                                 |
+=====================================+==================================================+=============================================================================================================================+
| ``support-sqlalchemy``              | ``ally-api``                                     | The [SQLAlchemy]_ support plugin that facilitates the work with SQL Alchemy object relational mapping. Contains support for |
|                                     |                                                  | mapping REST models with SQL Alchemy, also support for transaction handling at a request scope level. Has a central         |
|                                     |                                                  | database application configuration but also the means of setting a different or multiple databases.                         |
+-------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``gateway``                         | ``support-sqlalchemy``                           | This plugin provides the Gateway API and also the means of setting up custom gateways, for instance allowing for a certain  |
|                                     |                                                  | IP full access to REST models. The gateway plugin is agnostic to the actual services that are published by the REST server  |
|                                     |                                                  | and any type of URLs and rules can be placed with this plugin.                                                              |
+-------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``gateway-acl``                     | ``gateway``, \[``ally-core-http``\]              | The ACL (access control layer) gateway plugin integrates gateways that are designed based on published REST models and      |
|                                     |                                                  | services, basically makes the conversion between access allowed on a service call and a gateway REST model.                 |
+-------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``indexing``                        | ``ally-api``, \[``ally-core``\]                  | This plugin offers the Indexing API and the implementation provides details related to the REST models content response     |
|                                     |                                                  | indexing based on data associate with ``ally-core``.                                                                        |
+-------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+

For instance ``service-gateway`` needs to know what URLs are allowed for anonymous access or user based access. This information is provided also through RESTful services.
First the ``service-gateway`` fetches a list of allowed gateways (lets consider the anonymous access) from the RESTful server, based on that, whenever a request comes in it will be first checked against the
list of gateways that the REST server declared available. In case of user based access the process also involves an authentication of the user with the REST server, based on this process the client receives
a session id that the gateway will then recognize. The REST server also provides a list of gateways based on a session id. Even though the REST server (actually the security plugin) stores and manages the
session id it never acts on it, like restricting information or providing other data based on this. Actually the security plugin is like a normal plugin is just that his API is recognized and can be used by
the gateway service. The gateway service can be implemented also as an external application (maybe even written as an [NGINX]_ plugin) since the functionality of it is very simple, is just compares the list
of allowed gateways provided by the REST server, no fancy workings.

.. image:: images/application-with-gateway.jpg

TODO: continue with image explanation


.. [IoC] Inversion of control, an overview http://en.wikipedia.org/wiki/Inversion_of_control, also a nice presentation http://martinfowler.com/articles/injection.html.
.. [REST] Representational state transfer, http://en.wikipedia.org/wiki/Representational_state_transfer.
.. [API] Application programming interface, http://en.wikipedia.org/wiki/Application_programming_interface.
.. [0MQ] Zero MQ, http://zeromq.org/
.. [Mongrel2] Mongrel2, http://mongrel2.org/
.. [SQLAlchemy] SQL Alchemy, http://www.sqlalchemy.org/
.. [PO] Gettext, http://en.wikipedia.org/wiki/Gettext
.. [NGINX] Engine X, http://wiki.nginx.org/Main