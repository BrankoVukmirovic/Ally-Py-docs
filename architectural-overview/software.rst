.. _software:

Application Layout
==================

The all-py framework is constructed from components and plugins in order to allow for a flexible and well organized customization of features.
The first problem in having an application formed of smaller parts like in our case the components and plugins is how you can bring them toghether to function as one, in this respect
we use the inversion of control [IoC]_ pattern. To handel the [IoC]_ we created a container that handles this, the implementation is found in the core component ``ally`` in package
``ally.container``. A general aproach in [IoC]_ is to use XML configuration files, but this container is designed to be used with standared python modules.


Lets have a view over the major components of the framework.

======================================  =================================================  ======================================================================================================================
Component                               Depends on                                         Description
======================================  =================================================  ======================================================================================================================
``ally``                                                                                   this is the main component and is the application entry point. This component provides also support for inversion of control container. Basically this component contains general support for the application that is not in any way linked with a particular tehnology.
``ally-http``                           ``ally``                                           contains HTTP specific handling for requests and also the basic HTTP server based on the python built in server.
``ally-http-asyncore-server``           ``ally-http``                                      TODO
``ally-http-mongrel2-server``           ``ally-http``                                      TODO
``ally-plugin``                         ``ally``                                           TODO
``ally-indexing``                       ``ally``                                           TODO
``ally-api``                            ``ally``                                           provides the means of decorating the [REST]_ models and services.
``ally-core``                           ``ally-api``, ``ally-indexing``                    provides the general support for handling the [API]_ services that have been decorated as [REST]_ services.
``ally-core-http``                      ``ally-core``, ``ally-http``                       TODO
``service-assemblage``                  ``ally-http``, ``ally-indexing``                   TODO
``service-gateway``                     ``ally-http``, ``ally-indexing``                   TODO
``service-cdm``                         ``ally-http``                                      TODO
======================================  =================================================  ======================================================================================================================



.. [IoC] Inversion of control, an overview http://en.wikipedia.org/wiki/Inversion_of_control, also a nice presentation http://martinfowler.com/articles/injection.html.
.. [REST] Representational state transfer, http://en.wikipedia.org/wiki/Representational_state_transfer.
.. [API] Application programming interface, http://en.wikipedia.org/wiki/Application_programming_interface.