.. _AOP:

Using Aspect-Oriented Programming
============================================================

Although dependency injection programming requires a lot of configuration code, the Ally.py framework reduces the need for plugin configuration by using Aspect-Oriented programming.

Editing the example from :ref:`SQLAlchemy`, instead of manually writing the service instance function for UserService we will adapt conventions and use Aspect-Oriented programming to configure the plugin ``__plugin__.sample_plugin.service`` :

.. code-block:: python

	from __plugin__.plugin.registry import addService
	from __plugin__.sample_plugin.db_sample import alchemySessionCreator
	from ally.container import support
	from ally.support.sqlalchemy.session import bindSession
	
	# --------------------------------------------------------------------
	
	API, IMPL = 'sample_plugin.api.**.I*Service', 'sample_plugin.impl.**.*'
	
	support.createEntitySetup(API, IMPL)
	
	def bindSampleSession(proxy): bindSession(proxy, alchemySessionCreator())
	support.listenToEntities(IMPL, listeners=addService(bindSampleSession,))
	
	support.loadAllEntities(API)

The variables ``API`` and ``IMPL`` contain the Aspect-Oriented signatures for the services:

* ``API`` is the path containing the API specification classes. All classes start with a 'I' and end in 'Service' in ``sample_plugin.api``.
* ``IMPL`` is the path containing the Aspect-Oriented programming implementation. All classes in ``sample_plugin.impl``.

The ``createEntitySupport`` function creates entity setup functions that would otherwise have to be written manually, such as this one:

.. code-block:: python

        @ioc.entity
        def IUserService() -> IUserService:# The API service interface
        return UserService() # The service implementation that inherits the API service

The entity setup function is automatically generated for any pair of service classes that have an API class and an IMPL class that inherits from the API.  The support function ``listenToEntities`` provides the instances of these classes as services, when the entity is created. The function ``addService`` from the plugin component returns a callable function that is used as the listener, this callable creates a proxy for the event instance and then calls the ``bindSampleSession`` function which binds the session creator to the proxy. 

The final support function invoked is ``loadAllEntities``. Because the Inversion of Control container does not invoke entity setup functions we need to calls these manually.

`Example egg <https://github.com/sourcefabric/Ally-Py-docs/blob/master/plugin-guide/source_code/04_-_using_AOP_query_plugin_sample/sample_plugin-1.0.dev-py3.2.egg>`_.
