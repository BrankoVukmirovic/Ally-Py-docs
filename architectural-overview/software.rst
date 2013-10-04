.. _software:

Application Layout
==================

The Ally-Py framework is constructed from components and plugins to facilitate customization. To make the separate parts function as a unified whole, Ally-Py uses Inversion of Control design patterns. The Inversion of Control container, which uses standard python modules not xml configuration files, is implemented in the core component ``ally`` in the package ``ally.container``. 

Ally-Py components:

+-------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Component                           | Depends on                                       | Description                                                                                                                 |
+=====================================+==================================================+=============================================================================================================================+
| ``ally``                            | \-                                               | This is the main component and is the application entry point. It contains the Inversion of Control container.              |
+-------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``ally-http``                       | ``ally``                                         | Handles HTTP requests and contains the basic HTTP server.                                                                   |
+-------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``ally-http-asyncore-server``       | ``ally-http``                                    | Contains an alternative HTTP server that handles requests in an asychronous manner using the python ``asyncore`` package.   |
+-------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``ally-http-mongrel2-server``       | ``ally-http``                                    | An alternative to the asyncore server with added support for using [0MQ]_ messaging to communicate with a [Mongrel2]_       |
|                                     |                                                  | HTTP server.                                                                                                                |
+-------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``ally-plugin``                     | ``ally``                                         | Incorporates plugins into the application.                                                                                  |
+-------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``ally-indexing``                   | ``ally``                                         | Provides a vocabulary for understanding index tables in responses. The indexes                                              |
|                                     |                                                  | provide the mechanism for data aggregation by a proxy server and security filtering at a property level.                    |
+-------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``ally-api``                        | ``ally``                                         | Provides the means of decorating the [REST]_ models and services.                                                           |
+-------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``ally-core``                       | ``ally-api``, ``ally-indexing``                  | Support for handling the [API]_ services that have been decorated as [REST]_ services.                                      |
+-------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``ally-core-http``                  | ``ally-core``, ``ally-http``                     | This component provides the actual handling for the HTTP [REST]_ by combining the ``ally-core`` and ``ally-http``.          |
+-------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``service-assemblage``              | ``ally-http``, ``ally-indexing``                 | Provides the data aggregation service based on the response indexes.                                                        |
+-------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``service-gateway``                 | ``ally-http``, ``ally-indexing``                 | Provides the gateway security service.                                                                                      |
+-------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``service-cdm``                     | ``ally-http``                                    | Provides content delivery management. [REST]_ models contain references to static files which are streamed by the content   |
|				      |                                                  | delivery management service.                                                                                                |
+-------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+

.. TODO::
	Need more info on some of these. indexing?

Splitting All-Py into components means that application deployment can be done in various ways.

Consider the example of a [REST]_ application compsed of ``ally``, ``ally-http``, ``ally-api``, ``ally-core``, ``ally-core-http``, ``ally-plugin`` and some custom **plugins**. This is enough to implement simple plugins, and does not requre database support, security, data aggregation or content delivery.

.. image:: images/application-rest-base.jpg

This [REST]_ application can return [REST]_ type model responses but not media files. To add the ability to stream static files add the ``service-cdm`` component to the application.

.. image:: images/application-rest-cdm.jpg

Now the [REST]_ application can return [REST]_ responses and also static files from the file system. The content delivery management service also streams the application client files (java script) for the client.

In an enterprise application you need to have the ability to scale, so the components can be separated and the content delivery managment be placed on an external server, or be replaced by external HTTP streaming servers. If the application is using [Mongrel2]_, the content is delivered directly by the [Mongrel2]_ server rather than the content delivery manangement service.

.. image:: images/application-cdm.jpg

Now the [REST]_ application is on one server and the content delivery management service is on a different server.

Component separation enables support both normal users and enterprise level customers, but using different combinations of plugins and components:

* Delivery of the application as an easy to install single python application with no external dependencies for use in a low traffic environment. 
* Delivery of a scalable application where you can easily separate the content delivery service, proxy server and [REST]_ server. 

If we use [0MQ]_ as the application messaging service with [Mongrel2]_ as the server we can start as many application instances as we need depending on the traffic since the RESTful server is stateless.

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

In the image above we have a distribution layout that is composed of two web servers, the first one is the gateway proxy that validates the authorization for a certain resource based on gateway API objects
provided by the gateway core plugin. The second web server is the actual REST server. The gateway first fetches the list of allowed gateways then any request that is received will be compared with the
gateways and acted accordingly.

.. image:: images/application-with-assemblage.jpg

Now we added to the REST server also the ``indexing`` plugin and added a new web server that is handling the data aggregation (assemblage) of the REST models. All this servers can also run together in a single
python application. The assemblage first gathers data based on the indexing API objects, this request usually by passes the gateway since we might not want to allow access to the indexing API but still the
assemblage requires it. The requests that are coming on the assemblage server will be passed through the gateway and only after that it reaches the actual REST server.

What is assemblage (data aggregation)?
The biggest problem with a proper REST web server is the fact that it needs to properly separate the resources (models). For instance if you have a *User* resource model that contains data directly related to the
user like *Name*, *Phone*, *Email* ... Lets say we need also an icon to be associated with this *User*, you might be tempted to just add a new property *Icon* to the *User* model that contains a URL that points
to an image file. The problem now is the fact that this file has a certain size and you might want smaller sizes for this image in order to display on the client user interface, if the web server that provides
the image file does actual resizing based on size parameters you will have a big problem with scaling even if you cache the images, and in case you cache them, how can you prevent then a malicious user making
requests with different sizes and filling you cache memory. The approach we made is to have a media archive that can also provide thumbnails of specific sizes that are predefined, in this case we now have a
separate resource for containing the *User* icon. So now in order to display a *User* you need to make a request to fetch the data, then a separate request to fetch the icon data and last the request to get
the actual icon. So in order to prevent at least the first two requests is to use data aggregation. Basically you say in the **X-Filter** header that you require the reference to the icon *Image* resource
to be fetched and injected in the same response. So now when we request the *User* with the **X-Filter** for icon we will have in the same response also the actual image reference.


**ally-py** is a great framework that provides specific rules on how to implement plugins and imposes a certain discipline. Beside the imposed work flow it also provides great support for breaking the application in
layers that can be optimized for great performance and scalability. There are a lot of plugins that can be used of the shelf, for instance the internationalization support or graphical user interface plugins
that help a lot in using as a REST client the java script. There are plugins for configuring security based on roles and users, support for media archive ...

The plugins have more then 90% of the code using [SQLAlchemy]_ so writing plugins is very easy.

.. [IoC] Inversion of control, an overview http://en.wikipedia.org/wiki/Inversion_of_control, also a nice presentation http://martinfowler.com/articles/injection.html.
.. [REST] Representational state transfer, http://en.wikipedia.org/wiki/Representational_state_transfer.
.. [API] Application programming interface, http://en.wikipedia.org/wiki/Application_programming_interface.
.. [0MQ] Zero MQ, http://zeromq.org/
.. [Mongrel2] Mongrel2, http://mongrel2.org/
.. [SQLAlchemy] SQL Alchemy, http://www.sqlalchemy.org/
.. [PO] Gettext, http://en.wikipedia.org/wiki/Gettext
.. [NGINX] Engine X, http://wiki.nginx.org/Main
