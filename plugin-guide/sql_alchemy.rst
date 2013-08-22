.. _SQLAlchemy:

Using SQLAlchemy
=================

..  Example 03_-_using_sql_alchemy_plugin_sample

Continuing the example from :ref:`Creating`, we will make user model persistant by storing it in a database. We need to add the SQLAlchemy egg to the python path. 

add to python path
        ``distribution/libraries/SQLAlchemy-0.7.1-py3.2.egg``

Then to use SQLAlchemy we define a ``MetaData`` object in ``sample_plugin.meta.__init__.py`` that is used to create the table:

.. code-block:: python

    from sqlalchemy.schema import MetaData

    # --------------------------------------------------------------------

    meta = MetaData()
    # Provides the meta object for SQL alchemy.


Add the Ally.py SQLAlchemy egg to the Python path

add to python path
        ``distribution/components/ally-core-sqlalchemy.1.0.egg``

Create a user module in ``sample_plugin.meta.user.py`` to map the User model to a database table: 


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

We now have a mapped User model class that we can use in our implementation, you need to use the ``User`` class from ``sample_plugin.meta`` to use SQLAlchemy. The next step is to edit the ``getUsers`` implementation in ``sample_plugin.impl.user.py`` to query ``User`` information from the database. 

A database query to an empty database is not of much use, we need to add a method to the ``IUserService`` class in ``sample_plugin.api.user.py``:
 
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

and then write the service implementation to populate the database in ``sample_plugin.impl.user.py``.

.. code-block:: python

    from ally.support.sqlalchemy.session import SessionSupport
    from sample_plugin.api.user import IUserService, QUser
    from sample_plugin.meta.user import User
    from ally.container.ioc import injected
    from ally.container.support import setup
    from sqlalchemy.exc import SQLAlchemyError
    from sqlalchemy.sql.expression import desc
    from sqlalchemy.sql.operators import like_op
    import logging

    # --------------------------------------------------------------------

    log = logging.getLogger(__name__)

    # --------------------------------------------------------------------

    @injected
    @setup(IUserService, name='userService')
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

The ``insert`` method handles the insertion of the user model, and is annotated with the input and output types. The input is a user model object and the output is the user id.

When implementing the insert method in ``sample_plugin.impl.user.py`` we need to convert the user model from ``sample_plugin.api.user.py`` to the user model in ``sample_plugin.meta.user.py`` which SQLAlchemy understands, in ``sample_plugin.impl.user.py``:

.. code-block:: python

        mapped = User()
    if User.Name in user: mapped.Name = user.Name

The following code in ``sample_plugin.impl.user.py``, checks if the ``User.Name`` attribute is specified for the user instance, and if it is, sets it on the corresponding mapped object. To insert the mapped User object into the database, add it to the session, and flush the session to get the inserted users Id. 

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

To add a user, send a POST request containing 

.. code-block:: xml

    <User>
        <Name>John Doe</Name>
    </User>

with the following parameters

Accept 
        xml
Content-Type
        xml
URL       
        http://localhost/resources/Sample/User

Verify that you receive the following response, containing the id of the new user:

.. code-block:: xml

    <?xml version="1.0" encoding="ISO-8859-1"?>
    <User>
        <Id>1</Id>
    </User>


Configuring the Database
-------------------------------

..  Example 03_-_using_sql_alchemy_plugin_sample

We can add users to the database, and query the database for existing users, but we must specify which database we are using. 

``database_url()`` specifies the database URL that SQLAlchemy connects to, in this case ``sample.db``. This SQLite database is created inside the ``distribution`` folder if it does not already exist. 

``alchemyEngine()`` is the SQLAlchemy setup function. Note that the database URL is specified using the configuration function ``database_url`` explained above, so that the Ally.py Inversion of Control container can override this configuration if necessary.  ``alchemySessionCreator()`` creates sessions whenever a service method is invoked. 

The ``createTables()`` setup function creates tables in the database. When the application starts, all tables defined in meta that do not already exist are created.

Define the database setup module in ``__plugin__.sample_plugin.db_sample.py``:

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

Sessions are created using the session creator whenever a service API method is invoked. After the method has been invoked the session is closed, either with a commit (when no exception has occurred) or with a rollback (if an exception has occured).

To prevent multiple methods using the same session, we need to wrap the service implementionation in a proxy in ``__plugin__.sample_plugin.service.py``:

.. TODO:: [SW] Not really sure why wrapping this in a proxy fixes the problem.
 

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

Instead of returning the instance of UserService directly, a proxy containing all the of the methods definied in the API service interface ``IuserService`` is returned. The proxy delegates calls to the actual user service implementation and handles the session management for all the methods.
        
Now when you run the application you see ``sample.db`` inside the distribution folder. If you access `resources/Sample/User <http://localhost/resources/Sample/User>`_ the response is an empty list, because there are no user in the database.

Querying the Database
-------------------------------- 

When querying users from a database you cannot know how many users the response will contain, so to avoid huge responses we need to implement an offset and limit for the query in ``sample_plugin.api.user.py``: 

.. code-block:: python

    from ally.api.config import service, call, query
    from ally.api.criteria import AsLikeOrdered
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

    @query(User)
    class QUser:
        '''
        The user model query object.
        '''
        name = AsLikeOrdered

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

We added offset and limit attributes of type integer to the ``getUsers`` method. The Ally.py framework automatically handles free parameters as long as they have a default value and are of a primitive type. Adjusting ``sample_plugin.impl.user.py``:

.. code-block:: python

    from ally.support.sqlalchemy.session import SessionSupport
    from sample_plugin.api.user import IUserService, QUser
    from sample_plugin.meta.user import User
    from ally.container.ioc import injected
    from ally.container.support import setup
    from sqlalchemy.exc import SQLAlchemyError
    from sqlalchemy.sql.expression import desc
    from sqlalchemy.sql.operators import like_op
    import logging

    # --------------------------------------------------------------------

    log = logging.getLogger(__name__)

    # --------------------------------------------------------------------

    @injected
    @setup(IUserService, name='userService')
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

Because the ``getUsers`` implementation method has a default value for ``limit`` of None instead of 10, whenever ``getUsers`` is called from an external request the limit of 10 is used, whenever ``getUsers`` is called from an internal request the None limit is used. 

Provide the limit and offset as parameters in the URL `User?offset=1&limit=1 <http://localhost/resources/Sample/User?offset=1&limit=1>`_. Download the `example egg <https://github.com/sourcefabric/Ally-Py-docs/blob/master/plugin-guide/source_code/03_-_query_sql_alchemy_plugin_sample/sample_plugin-1.0.dev-py3.2.egg>`_
