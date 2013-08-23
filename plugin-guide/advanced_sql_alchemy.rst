.. _Advanced_SQLAlchemy:

Using Advanced SQLAlchemy
============================

Continuing the example from :ref:`AOP`, we look at some support modules that simplify configuration, models and services.

add to python path:
    ``distribution/plugins/support-sqlalchemy.1.0.egg``

Looking at the database configuration code in the common plugin ``example.__plugin__.example.db_example.py``:

.. code-block:: python 

    from ally.container import ioc, support
    from ally.container.binder_op import bindValidations
    from ally.support.sqlalchemy.mapper import mappingsOf
    from ally.support.sqlalchemy.session import bindSession
    from sample_plugin.meta import meta
    from sql_alchemy import database_config
    from sql_alchemy.database_config import database_url, alchemySessionCreator, metas

    # --------------------------------------------------------------------

    support.include(database_config)

    # --------------------------------------------------------------------
    @ioc.replace(database_url)
    def database_url():
    	'''The database URL for the samples'''
    	return 'sqlite:///sample.db'

    @ioc.replace(metas)
    def metas(): return [meta]

    def bindSampleSession(proxy): bindSession(proxy, alchemySessionCreator())
    def bindSampleValidations(proxy): bindValidations(proxy, mappingsOf(meta))

The database configuration is loaded from a common plugin used by multiple plugins. It replaces the IoC function with one that provides a default database url, and replaces the metas function with one that provides a list of meta plugins.  ``bindSampleSession`` performs input and output validation for REST services. Do not bind proxies meant for internal use so as not to decrease performance. 

Configuring the service in the common plugin ``example.__plugin__.example.service.py``:

.. code-block:: python 

    from __plugin__.plugin.registry import addService
    from __plugin__.sample_plugin.db_sample import bindSampleSession, bindSampleValidations
    from ally.container import support

    # --------------------------------------------------------------------

    API, IMPL = 'sample_plugin.api.**.I*Service', 'sample_plugin.impl.**.*'

    support.createEntitySetup(API, IMPL)

    support.bindToEntities(IMPL, binders=bindSampleSession)
    support.listenToEntities(IMPL, listeners=addService(bindSampleSession, bindSampleValidations))

    support.loadAllEntities(API)

So we got rid of the bindSampleSession since is now defined in the db_sample setup module. We are calling a new support function bindToEntities, this will actually create proxies for all entities setup functions that return an instance that with the class found in IMPL, this will apply to the user defined entities setups functions and also to the automatically created entities setup functions. This proxies will be used whenever another service requires internally an instance of a service having a class from IMPL so this is why we only bind to this proxies the session. The listen to entities that adds the services to the REST framework is now binding to the proxies services the session and also the validation, keep in mind that this proxies are only used for external requests. You can find the sample here. 

Adding the API configuration ``example-user.example.user.api.user.py``:

.. code-block:: python 

    from ally.api.config import service, query
    from ally.api.criteria import AsLikeOrdered
    from example.api.domain_example import modelExample
    from ally.support.api.entity import Entity, QEntity, IEntityService

    # --------------------------------------------------------------------

    @modelExample
    class User(Entity):
        '''
        The user model.
        '''
        Name = str

    # --------------------------------------------------------------------

    @query(User)
    class QUser(QEntity):
        '''
        The user model query object.
        '''
        name = AsLikeOrdered

    # --------------------------------------------------------------------

    @service((Entity, User), (QEntity, QUser))
    class IUserService(IEntityService):
        '''
        The user service.
        '''

First the User model now extends the Entity base model, it has no Id anymore because is inherited from Entity. The QEntity inherited by the query provides no functionality but is extended in order to be used as generic replacement in the service. Finally the service interface has no more methods defined that is because they are inherited from the IEntityService.

======================= ===================== ======================= ===================== =====================================
Interface               Inherits              Calls                   Requires              Description
======================= ===================== ======================= ===================== =====================================
IEntityGetService       -                     getById                 a model               Provides the get entity by id method
IEntityFindService      -                     getAll                  a model               Provides the get all entities service without a query object
IEntityQueryService     -                     getAll                  a model and a query   Provides the get all entities service with a query object
IEntityCRUDService      -                     insert, update, delete  a model               Provides the entity CRUD service 
IEntityGetCRUDService   IEntityGetService,    getById, insert,update  a model               Just combines the interfaces, no additional call methods
    	        	IEntityCRUDService    delete                        
IEntityNQService        IEntityGetService,    getById, getAll,insert, a model               Just combines the interfaces, no additional call methods
    			IEntityFindService,   update,delete
    			IEntityCRUDService 
IEntityService          IEntityGetService,    getById, getAll,insert, a model and a query   Just combines the interfaces, no additional call methods
    			IEntityQueryService,  update, delete
    			IEntityCRUDService 
======================= ===================== ======================= ===================== =====================================

Beside the fact that the user service extend the entity service you also notice that when we decorate the service we provide two tuples, the role of this is to provide generic replacing, what it will happen is that every type annotation that contains Entity for example Entity, Entity.Id, Iter(Entity), it will get replaced with User so the examples will look like User, User.Id, Iter(User), the same thing will happen with the query also.

Editing the implementation ``example-user.example.user.impl.user.py``

.. code-block:: python 

    from example.user.api.user import IUserService, QUser
    from example.user.meta.user import UserMapped
    from sql_alchemy.impl.entity import EntityServiceAlchemy
    from ally.container.ioc import injected
    from ally.container.support import setup

    # --------------------------------------------------------------------

    @injected
    @setup(IUserService, name='userService')
    class UserServiceAlchemy(EntityServiceAlchemy, IUserService):
        '''
        Implementation for @see: IUserService
        '''

        def __init__(self):
            EntityServiceAlchemy.__init__(self, UserMapped, QUser)

This is all the implementation we need to make for the entity interface methods, basically the EntityServiceAlchemy has the method implementations for the IEntityService, also there is a specific implementation for each interface defined in the previous table. 

So now if you redeploy the application and access http://localhost/resources/Sample/User you see the user list:

.. code-block:: xml

    <UserList>
    	<User href="http://localhost/resources/Sample/User/1" />
    	<User href="http://localhost/resources/Sample/User/2" />
    </UserList>

You notice that now in the users list we do not get anymore the user models representations, this is because we have a new method getById in our service which is used by the Ally.py framework to retrieve single model instances based on the id, and that is why we only get the reference addresses where the models can be retrieved in respect with the REST ideology. 
