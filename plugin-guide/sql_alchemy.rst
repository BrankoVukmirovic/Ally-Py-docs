Using SQLAlchemy
=================

Continuing the example from :ref:`Creating`, we'll make a persistent user model stored in a database. We need to add the SQLAlchemy egg to the python path. 

add to python path
        ``distribution/libraries/SQLAlchemy-0.7.1-py3.2.egg``

Then to use SQLAlchemy we define a ``MetaData`` object in ``sample_plugin.meta.__init__`` that is used to create the table:

.. code-block:: python

        from sqlalchemy.schema import MetaData

        # --------------------------------------------------------------------

        meta = MetaData()
        # Provides the meta object for SQL alchemy.


After adding the Ally.py SQLAlchemy egg to the Python path, create a user module in ``sample_plugin.meta.user`` to map the User model to a database table: 

add to python path
        ``distribution/components/ally-core-sqlalchemy.1.0.egg``

.. code-block:: python

        '''
        Database mapping for the user model.
        '''

        from ally.support.sqlalchemy.mapper import mapperModel
        from sample_plugin.api.user import User
        from sample_plugin.meta import meta
        from sqlalchemy.schema import Table, Column
        from sqlalchemy.types import String, Integer

        # --------------------------------------------------------------------
        
        table = Table('sample_user', meta,
                Column('id', Integer, primary_key=True, key='Id'),
                Column('name', String(20), nullable=False, key='Name'))

        # --------------------------------------------------------------------

        # map User entity to defined table (above)
        User = mapperModel(User, table)

We have defined a SQLAlchemy table called ``sample_user`` that has two columns, ``id`` and ``name``. Each column linked to the REST model has the attribute it is linked to in the key definition. Then we map the table to the REST model. 


Implementing Database Queries
------------------------------

To add session support to the service implementation, extend ``SessionSupport``, the Ally.py framework starts a transaction when a request is made, and ends it after the response is delivered. 

.. NOTE:: If you implement the ``__init__`` method, you must call call the ``SessionSupport.__init__`` within your implementation.

We now have a mapped User model class that we can use in our implementation, you need to use the ``User`` class from ``sample_plugin.meta`` to use SQLAlchemy. The next step is to edit the ``getUsers`` implementation in ``sample_plugin.impl.user`` to query ``User`` information from the database. 

.. code-block:: python
   
        from sample_plugin.api.user import IUserService
        from ally.support.sqlalchemy.session import SessionSupport
        from sample_plugin.meta.user import User

        # --------------------------------------------------------------------

        class UserService(IUserService, SessionSupport):
        '''
        Implementation for @see: IUserService
        '''

        def getUsers(self):
                '''
                @see: IUserService.getUsers
                '''
                return self.session().query(User).all()

A database query to an empty database is not of much use, we need to add a method to the ``IUserService`` class in ``sample_plugin.api.user``, and then write the service implementation to populate the database in ``sample_plugin.impl.user``.

``sample_plugin.api.user``:

.. code-block:: python
   
        from sample_plugin.api.user import IUserService
        from ally.support.sqlalchemy.session import SessionSupport
        from sample_plugin.meta.user import User

        # --------------------------------------------------------------------

        class UserService(IUserService, SessionSupport):
        '''
        Implementation for @see: IUserService
        '''

        def getUsers(self):
                '''
                @see: IUserService.getUsers
                '''
                return self.session().query(User).all()

        @service
        class IUserService:
                '''
                The user service.
                '''
                ...
                @call
                def insert(self, user:User) -> User.Id:
                        '''
                        Persist the user model.
                        '''
                        
The ``insert`` method handles the insertion of the user model, and is annotated with the input and output types. The input is a user model object and the output is the user id.

When implementing the insert method in ``sample_plugin.impl.user`` we need to convert the user model from ``sample_plugin.api.user`` to the user model in ``sample_plugin.meta.user`` which SQLAlchemy understands, in ``sample_plugin.impl.user``:

.. code-block:: python

        mapped = User()
                if User.Name in user: mapped.Name = user.Name

The following code, ``sample_plugin.impl.user``, checks if the ``User.Name`` attribute is specified for the user instance, and if it is, sets it on the corresponding mapped object. To insert the mapped User object into the database, add it to the session, and flush the session to get the inserted users Id. 

.. code-block:: python

        ...
        from sqlalchemy.exc import SQLAlchemyError
        import logging

        # --------------------------------------------------------------------
        log = logging.getLogger(__name__)

        # --------------------------------------------------------------------
        class UserService(IUserService, SessionSupport):
                '''
                Implementation for @see: IUserService
                '''
                ...

                def insert(self, user):
                '''
                @see: IUserService.insert
                '''
                        mapped = User()
                        if User.Name in user: mapped.Name = user.Name
                        try:
                                self.session().add(mapped)
                                self.session().flush((mapped,))
                        except SQLAlchemyError:
                                log.exception('Could not insert %s' % user)
                        return mapped.Id

Configuring the Database
-------------------------------

We can add users to the database, and query the database for existing users, but we must specify which database we are using. Define the database setup module, in ``db_sample`` in ``__plugin__.sample_plugin.db_sample``:

``database_url()`` specifies the database URL that SQLAlchemy connects to, in this case ``sample.db``. This SQLite database is created inside the ``distribution`` folder if it does not already exist. 

``alchemyEngine()`` is the SQLAlchemy setup function. Note that the database URL is specified using the configuration function ``database_url`` explained above, so that the Ally.py Inversion of Control container can override this configuration if necessary.  ``alchemySessionCreator()`` creates sessions whenever a service method is invoked. 

The ``createTables()`` setup function creates tables in the database. When the application starts, all tables defined in meta that do not already exist are created.

.. code-block:: python

        '''
        Contains the database setup for the samples.
        '''

        from ally.container import ioc
        from sample_plugin.meta import meta
        from sqlalchemy.engine import create_engine
        from sqlalchemy.engine.base import Engine
        from sqlalchemy.orm.session import sessionmaker

        # --------------------------------------------------------------------
        @ioc.config
        def database_url():
                '''The database URL for the samples'''
                return 'sqlite:///sample.db'

        @ioc.entity
        def alchemyEngine() -> Engine:
                engine = create_engine(database_url())
                return engine

        @ioc.entity
        def alchemySessionCreator():
                return sessionmaker(bind=alchemyEngine())

        @ioc.start
        def createTables():
                meta.create_all(alchemyEngine())












A session needs to be created using the session creator whenever a method (that belongs to the service API) of the service is invoked, after the method has been invoked the session is closed with a commit if no exception has occur or with a rollback if there was an exception. This is the general view for the session handling but there are some exceptions, if for instance while a service method is processed and another service method is used while processing and that service uses the same session creator (same database) no new session or transaction will be created but instead the same one will be used. So in order to have this session handling we need to wrap the service
implementation with a proxy that does that, so lets go back to the __plugin__.sample_plugin.service configuration module.  __plugin__.sample_plugin.service:


.. code-block:: python

        from __plugin__.plugin.registry import registerService
        from __plugin__.sample_plugin.db_sample import alchemySessionCreator
        from ally.container import ioc
        from ally.container.proxy import createProxy, ProxyWrapper
        from ally.support.sqlalchemy.session import bindSession
        from sample_plugin.api.user import IUserService
        from sample_plugin.impl.user import UserService

        # --------------------------------------------------------------------

        @ioc.entity
        def userService() -> IUserService:
                b = UserService()
                proxy = createProxy(IUserService)(ProxyWrapper(b))
                bindSession(proxy, alchemySessionCreator())
                return proxy
                
        @ioc.start
        def register():
                registerService(userService())

So instead of returning the actual instance of UserService implementation we first create a proxy class for the API service interface IuserService this proxy class contains all the methods that are defined in the API, then we create an instance of this proxy class that will delegate all the calls tothe actual user service implementation ant this proxy will be the returned instance, but before we return this instance we are going to bind the session handling to all the proxy methods.  Now we have a service that uses a database, just added to the distribution and run the application. After the application has been started you should see the sample.db file in the distribution folder. If you access http://localhost/resources/Sample/User you will get an empty list as the response since there are no users in the user_sample database table.method 
        POST
Accept 
        xml
Content-Type
        xml
URL       
        http://localhost/resources/Sample/User

.. code-block:: xml

        <User>
                <Name>John Doe</Name>
        </User>

After making this post you will receive as a response the id of the newly inserted user:

.. code-block:: xml

        <?xml version="1.0" encoding="ISO-8859-1"?>
        <User>
                <Id>1</Id>
        </User>

Querying
--------

We have seen how to do the simple implementation lets see how we will handle the querying, you just need to use the user API from the query example in the "create a plugin" chapter but keep also the insert service method. Because now the users are from the database we cannot know how many users we will have in the response, so in order to avoid huge responses we will introduce the offset and limit for the users list.sample_plugin.impl.user:

.. code-block:: python

        from ally.api.config import service, call, query
        from ally.api.criteria import AsLike
        from ally.api.type import Iter
        from sample_plugin.api import modelSample

        # --------------------------------------------------------------------

        @modelSample(id='Id')
        class User:
                '''
                The user model.
                '''
                Id = int
                Name = str

        # --------------------------------------------------------------------

        @query
        class QUser:
                '''
                The user model query object.
                '''
                name = AsLike

        # --------------------------------------------------------------------

        @service
        class IUserService:
                '''
                The user service.
                '''

                @call
                def getUsers(self, offset:int=None, limit:int=10, q:QUser=None) -> Iter(User):
                        '''
                        Provides all the users.
                        '''

                @call
                def insert(self, user:User) -> User.Id:
                        '''
                        Persist the user model.
                        '''

We added an offset and limit attribute of type integer in the getUsers method. The ally framework knows how to handle free parameters as long as they have a default value and are of a primitive type. Now we need to adjust the implementation.sample_plugin.impl.user:

.. code-block:: python

        from ally.support.sqlalchemy.session import SessionSupport
        from sample_plugin.api.user import IUserService, QUser
        from sample_plugin.meta.user import User
        from sqlalchemy.exc import SQLAlchemyError
        from sqlalchemy.sql.expression import desc
        from sqlalchemy.sql.operators import like_op
        import logging

        # --------------------------------------------------------------------
        log = logging.getLogger(__name__)

        # --------------------------------------------------------------------

        class UserService(IUserService, SessionSupport):
                '''
                Implementation for @see: IUserService
                '''

                def getUsers(self, offset=None, limit=None, q=None):
                        '''
                        @see: IUserService.getUsers
                        '''
                        sql = self.session().query(User)
                        if q:
                                if QUser.name.like in q:
                                        sql = sql.filter(like_op(User.Name, q.name.like))
                                if QUser.name.ascending in q:
                                        sql = sql.order_by(User.Name if q.name.ascending else desc(User.Name))
                        if offset: sql = sql.offset(offset)
                        if limit: sql = sql.limit(limit)
                        return sql.all()

                def insert(self, user):
                        '''
                        @see: IUserService.insert
                        '''
                        mapped = User()
                        if User.Name in user: mapped.Name = user.Name
                        try:
                                self.session().add(mapped)
                                self.session().flush((mapped,))
                        except SQLAlchemyError:
                                log.exception('Could not insert %s' % user)
                        return mapped.Id

You will notice that the getUsers implementation method has a default value for limit set to None instead of 10, the effect of this is that whenever the getUsers is called using external requests the API limit of 10 will be used, if is made internal (from a different plugin for example) the None limit will apply. Now in order to provide the limit and offset like this http://localhost/resources/Sample/User?offset=1&limit=1. 
