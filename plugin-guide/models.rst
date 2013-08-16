Associating and Extending Models
=====================================

Associating two models implies that one model contains a reference to another model. This requires modifcation of that model's API and meta functions.

.. TODO:: [SW] Not sure how the 00 plugin works with these last two plugin examples
.. TODO:: [SW] Also, why example not sample, and why alter the directory structure, ie example/user/api 

.. 
        The association of two models means that one model contains a reference(id) of another model the association can be optional or mandatory.  The association of two models only require the modification of the models APIs and the meta's. We will use the last sample from "05 - sql alchemy support" chapter, 
        
To associate a UserType model to the User model we need to create an API and implementation for the UserType as we did for the User model in ``example.user.api.user_type.py``:

.. code-block:: python

	from ally.api.config import query, service
	from ally.api.criteria import AsLikeOrdered
	from example.api.domain_example import modelExample
	from ally.support.api.entity import Entity, QEntity, IEntityService

	# --------------------------------------------------------------------

	@modelExample
	class UserType(Entity):
	    '''
	    The user type model.
	    '''
	    Name = str

	# --------------------------------------------------------------------

	@query(UserType)
	class QUserType(QEntity):
	    '''
	    The user type model query object.
	    '''
	    name = AsLikeOrdered

	# --------------------------------------------------------------------

	@service((Entity, UserType), (QEntity, QUserType))
	class IUserTypeService(IEntityService):
	    '''
	    The user type service.
	    '''

The UserType API, is similar to the User API. We also need to edit ``example.user.meta.user_type.py``:

.. code-block:: python

	from example.user.api.user_type import UserType
	from ally.support.sqlalchemy.mapper import validate
	from sqlalchemy.dialects.mysql.base import INTEGER
	from sqlalchemy.schema import Column
	from sqlalchemy.types import String
	from example.meta.metadata_example import Base

	# --------------------------------------------------------------------

	@validate
	class UserTypeMapped(Base, UserType):
	    __tablename__ = 'user_type'
	    __table_args__ = dict(mysql_engine='InnoDB', mysql_charset='utf8')

	    Id = Column('id', INTEGER(unsigned=True), primary_key=True)
	    Name = Column('name', String(20), nullable=False, unique=True)

``sample_user_type`` table is similar to ``sample_user table`` except that ``name`` is declared as a unique column, we don't want multiple types with the same name. Lastly we need to write the implentation in ``example.user.impl.user_type.py``:

.. code-block:: python

	from example.user.api.user_type import IUserTypeService, QUserType
	from example.user.meta.user_type import UserTypeMapped
	from sql_alchemy.impl.entity import EntityServiceAlchemy
	from ally.container.ioc import injected
	from ally.container.support import setup

	# --------------------------------------------------------------------

	@injected
	@setup(IUserTypeService, name='userTypeService')
	class UserTypeServiceAlchemy(EntityServiceAlchemy, IUserTypeService):
	    '''
	    Implementation for @see: IUserTypeService
	    '''

	    def __init__(self):
		EntityServiceAlchemy.__init__(self, UserTypeMapped, QUserType)

After defining the UserType modules, start the application and the Aspect-Oriented configuration will automatically populate the REST services in `\Sample\UserType <http://localhost/resources/Sample/UserType>`_. This list is initially empty, so populate it with a POST request to http://localhost/resources/Sample/UserType with the following headers:

Accept
        xml
Content-Type
        xml
Body
   .. code-block:: xml

           <UserType>
                   <Name>Administrator</Name>
           </UserType>

Verify that the response is:

.. code-block:: xml

	<?xml version="1.0" encoding="UTF-8"?>
	<UserType href="http://localhost/resources/Sample/UserType/1">
		<Id>1</Id>
	</UserType>

If you try to resend the POST request you will receive the following response:

.. code-block:: xml

        <?xml version="1.0" encoding="UTF-8"?>
        <error>
                <message>Already an entry with this value</message>
                <code>404</code>
        </error>

`name` is declared as unique, so the insertion request checks that the value is not already present in the database.

Edit the User model to reference the ``UserType`` model by changing the user API in ``example.user.api.user.py``:

.. code-block:: python

	from ally.api.config import service, query
	from ally.api.criteria import AsLikeOrdered
	from example.api.domain_example import modelExample
	from example.user.api.user_type import UserType
	from ally.support.api.entity import Entity, QEntity, IEntityService

	# --------------------------------------------------------------------

	@modelExample
	class User(Entity):
	    '''
	    The user model.
	    '''
	    Name = str
	    Type = UserType
	...

The new User model has an ``Type`` attribute with a value of ``UserType``, which the Ally.py framework detects as reference to an object. The actual value of ``Type`` is the model ``id`` of ``UserType``. 

Modifying the meta class to include ``Type`` in ``example.user.meta.user.py``:

.. code-block:: python

	from example.user.api.user import User
	from example.user.meta.user_type import UserTypeMapped
	from ally.support.sqlalchemy.mapper import validate
	from sqlalchemy.dialects.mysql.base import INTEGER
	from sqlalchemy.schema import Column, ForeignKey
	from sqlalchemy.types import String
	from example.meta.metadata_example import Base

	# --------------------------------------------------------------------

	@validate
	class UserMapped(Base, User):
	    __tablename__ = 'user'
	    __table_args__ = dict(mysql_engine='InnoDB', mysql_charset='utf8')

	    Id = Column('id', INTEGER(unsigned=True), primary_key=True)
	    Name = Column('name', String(20), nullable=False)
	    Type = Column('fk_user_type', ForeignKey(UserTypeMapped.Id, ondelete='RESTRICT'), nullable=False)

.. 
	from ally.support.sqlalchemy.mapper import mapperModel
	from sample_plugin.api.user import User
	from sample_plugin.meta import meta
	from sqlalchemy.schema import Table, Column, ForeignKey
	from sqlalchemy.types import String, Integer
	from sample_plugin.meta.user_type import UserType
	# --------------------------------------------------------------------
	table = Table('sample_user', meta,
	Column('id', Integer, primary_key=True, key='Id'),
	Column('name', String(20), nullable=False, key='Name'),
	Column('fk_user_type', ForeignKey(UserType.Id, ondelete='RESTRICT'), nullable=False,
	key='Type'))
	# map User entity to defined table (above)
	User = mapperModel(User, table)

.. TODO:: I Don't understand all of this.  
	We added a new column to the table that is a foreign key to the user type table, you notice that when we define relations with other models we always need to use the meta class, in this case the UserType mapped in the module sample_plugin.meta.user_type. Because the logic in the services is not modified by the newly added information we don't need to modify anything in the service APIs or implementations.  In order to test this, before we start the application we need to delete the sample.db file in the distribution, this will force the creation of the new sample_user table that contains now also the user type foreign key, also to get a better error message that will also tell which attribute is the problem change the configuration explain_detailed_error to true in the "application.properties" file. 

Try to insert a user into the empty database by making a POST request to http://localhost/resources/Sample/User with the following headers:

Accept
        xml
Content-Type
        xml
BODY
   .. code-block:: xml

           <User>
                   <Name>John Doe</Name>
           </User>

And verify that response is 

.. code-block:: xml

   <?xml version="1.0" encoding="UTF-8"?>
   <error>
	   <code>404</code>
	   <User>
		   <Type>Expected a value</Type>
	   </User>
   </error>

The response is an error, because the request did not specify ``User.Type``, and it is defined as not nullable. Insert a ``User.Type`` into the empty database by making a POST request to http://localhost/resources/Sample/UserType with the following headers:

Accept
        xml
Content-Type
        xml
Body 
	.. code-block:: xml

		<UserType>
			<Name>John Doe</Name>
		</UserType>

The response confirming insertion of a ``User.Type`` is:

.. code-block:: xml

        <?xml version="1.0" encoding="UTF-8"?>
        <UserType href="http://localhost/resources/Sample/UserType/1">
                <Id>1</Id>
        </UserType>

Now that we have ``User.Type`` of id 1 we can insert a user of type 1 by making a POST request to http://localhost/resources/Sample/User with the following headers:

Accept
        xml
Content-Type
        xml
Body 
	.. code-block:: xml

		<User>
			<Name>John Doe</Name>
			<Type>1</Type>
		</User>

Note the confirmation response:

.. code-block:: xml

        <?xml version="1.0" encoding="UTF-8"?>
        <User href="http://localhost/resources/Sample/User/1">
                <Id>1</Id>
        </User>

If you make the same request using a ``User.Type=2`` the request fails, as validation tells us that there is only 1 ``User.Type`` in the database.

Now we have successfully inserted a user with a user type into the database, so we can access http://localhost/resources/Sample/User/1 , and view the new user model with a user type reference. 

.. code-block:: xml

        <?xml version="1.0" encoding="UTF-8"?>
        <User>
                <Type href="http://localhost/resources/Sample/UserType/1">
                        <Id>1</Id>
                </Type>
                <Id>1</Id>
                <Name>John Doe</Name>
        </User>


Extending Models
-------------------------------

Extending a model requires the service providing a model based on another model's id, but does not require the models to be associated with each other. This requires only the modification of the service API and implementation.

Editing the API ``example.user.api.user.py``:

.. code-block:: python

	from ally.api.config import service, query, call
	from ally.api.criteria import AsLikeOrdered
	from ally.api.type import Iter
	from example.api.domain_example import modelExample
	from example.user.api.user_type import UserType
	from ally.support.api.entity import Entity, QEntity, IEntityService

	...

	@service((Entity, User), (QEntity, QUser))
	class IUserService(IEntityService):
	    '''
	    The user service.
	    '''

	    @call
	    def getUsersByType(self, typeId:UserType.Id, offset:int=None, limit:int=None, q:QUser=None) -> Iter(User):
		'''
		Provides the users that have the specified type id.
		'''

We added a service method that provides all users that have the specified user type. You can specify offset, limit and user.

Editing the implementation ``example.user.impl.user.py``:

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

	    def getUsersByType(self, typeId, offset=None, limit=None, q=None):
		'''
		@see: IUserService.getUsersByType
		'''
		return self._getAll(UserMapped.Type == typeId, q, offset, limit)

This implementation makes use of the ``_getAll`` method inherited from ``EntitySupportAlchemy`` that simplifies getting models from the database. So now we have a service method that provides user models based on a user type, if we access http://localhost/resources/Sample/UserType/1 we get:

.. code-block:: xml

        <?xml version="1.0" encoding="UTF-8"?>
        <UserType>
                <Id>1</Id>
                <Name>John Doe</Name>
                <User href="http://localhost/resources/Sample/UserType/1/User/"/>
        </UserType>

As well as the ``UserType`` model data, we also have a reference to the User models that belong to the ``UserType`` that calls the service method. In this way other services can add information to the ``UserType`` model without using the main user type service.
