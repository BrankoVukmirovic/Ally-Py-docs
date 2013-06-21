Associating and Extending Models
=====================================

Associating two models implies that one model contains a reference to another model. This requires modifcation of that model's API and meta functions.

.. 
        The association of two models means that one model contains a reference(id) of another model the association can be optional or mandatory.  The association of two models only require the modification of the models APIs and the meta's. We will use the last sample from "05 - sql alchemy support" chapter, 
        
To associate a UserType model to the User model we need to create an API and implementation for the UserType as we did for the User model in ``sample_plugin.api.user_type``:

.. code-block:: python

        '''
        The API descriptions for user type sample.
        '''
        from ally.api.config import query, service
        from ally.api.criteria import AsLike
        from sample_plugin.api import modelSample
        from sql_alchemy.api.entity import Entity, QEntity, IEntityService
        # --------------------------------------------------------------------
        @modelSample
        class UserType(Entity):
        '''
        The user type model.
        '''
        Name = str
        # --------------------------------------------------------------------
        @query
        class QUserType(QEntity):
        '''
        The user type model query object.
        '''
        name = AsLike
        # --------------------------------------------------------------------
        @service((Entity, UserType), (QEntity, QUserType))
        class IUserTypeService(IEntityService):
        '''
        The user type service.
        '''

The UserType API, is simiar to the User API. We also need to edit ``meta.sample_plugin.meta.user_type``:

.. code-block:: python

        '''
        Mapping for the user type model.
        '''
        from ally.support.sqlalchemy.mapper import mapperModel
        from sample_plugin.api.user_type import UserType
        from sample_plugin.meta import meta
        from sqlalchemy.schema import Table, Column
        from sqlalchemy.types import String, Integer
        # --------------------------------------------------------------------
        table = Table('sample_user_type', meta,
        Column('id', Integer, primary_key=True, key='Id'),
        Column('name', String(20), nullable=False, unique=True, key='Name'))
        # map User Type entity to defined table (above)
        UserType = mapperModel(UserType, table)



``sample_user_type`` table is similar to ``sample_user table`` except that ``name`` is declared as a unique column, we don't want multiple types with the same name. Lastly we need to write the implentation in ``sample_plugin.impl.user_type``:

.. code-block:: python

        '''
        Simple implementation for the user type APIs.
        '''
        from sample_plugin.api.user_type import IUserTypeService, QUserType
        from sample_plugin.meta.user_type import UserType
        from sql_alchemy.impl.entity import EntityServiceAlchemy
        # --------------------------------------------------------------------
        class UserTypeService(EntityServiceAlchemy, IUserTypeService):
        '''
        Implementation for @see: IUserTypeService
        '''
        def __init__(self):
        EntityServiceAlchemy.__init__(self, UserType, QUserType)


After defining the UserType modules, start the application and the Aspect-Oriented configuration will automatically populate the REST services in `\Sample\UserType <http://localhost/resources/Sample/UserType>`_. This list is initially empty, so populate it with a POST request:

method 
        POST

Accept
        xml

Content-Type
        xml
URL     
        http://localhost/resources/Sample/UserType
BODY
   .. code-block:: xml

           <UserType>
                   <Name>Administrator</Name>
           </UserType>
RESPONSE
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

The `name` is declared as unique, so the insertion request checks that the value is not already present in the database.

Editing the User model to reference the ``UserType`` model by changing the user API in ``sample_plugin.api.user``:

.. code-block:: python

        from ally.api.config import service, query
        from ally.api.criteria import AsLike
        from sample_plugin.api import modelSample
        from sample_plugin.api.user_type import UserType
        from sql_alchemy.api.entity import Entity, QEntity, IEntityService

        # --------------------------------------------------------------------

        @modelSample
        class User(Entity):
        '''
        The user model.
        '''
        Name = str
        Type = UserType
        ...

The new User model has an ``Type`` attribute with a value of ``UserType``, which the Ally.py framework detects as reference to an object. The actual value of ``Type`` is the model ``id`` of ``UserType``. 

Modifying the meta class to include ``Type`` in ``sample_plugin.meta.user``:

.. code-block:: python

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

        
We added a new column to the table that is a foreign key to the user type table, you notice that when we define relations with other models we
always need to use the meta class, in this case the UserType mapped in the module sample_plugin.meta.user_type. Because the logic in the
services is not modified by the newly added information we don't need to modify anything in the service APIs or implementations.
In order to test this, before we start the application we need to delete the sample.db file in the distribution, this will force the creation of the new
sample_user table that contains now also the user type foreign key, also to get a better error message that will also tell which attribute is the
problem change the configuration explain_detailed_error to true in the "application.properties" file. Now lets insert a user, keep in mind that our
database is empty.

method 
        POST
Accept
        xml
Content-Type
        xml
URL
        http://localhost/resources/Sample/User
BODY
   .. code-block:: xml

           <User>
                   <Name>John Doe</Name>
           </User>
RESPONSE
   .. code-block:: xml

           <?xml version="1.0" encoding="UTF-8"?>
           <error>
                   <code>404</code>
                   <User>
                           <Type>Expected a value</Type>
                   </User>
           </error>

So we get an error of Invalid resource because the User.Type is not specified, that is because when we defined the table we set the nullable flag to false for the Type column. Since our database is empty lets insert a user type.

method
        POST
Accept
        xml
Content-Type
        xml
URL
        http://localhost/resources/Sample/UserType

.. code-block:: xml

        <UserType>
                <Name>root</Name>
        </UserType>

RESPONSE:

.. code-block:: xml

        <?xml version="1.0" encoding="UTF-8"?>
        <UserType href="http://localhost/resources/Sample/UserType/1">
                <Id>1</Id>
        </UserType>

Now that we have user type of id 1 lets try to insert the user having this user type.

method
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
                <Type>2</Type>
        </User>

RESPONSE:

.. code-block:: xml

        <?xml version="1.0" encoding="UTF-8"?>
        <error>
                <code>404</code>
                <User>
                        <Type>Unknown foreign id</Type>
                </User>
        </error>

I had intentionally set the type as 2 because there is no user type in the database with that id and as you see the binded validations will deliver a message telling us that the id we had specified is invalid. Lets to this again but with a valid id.

method
        POST
Accept
        xml
Content-Type
        xml
URL
        http://localhost/resources/Sample/User

.. code-block:: xml

        <User>
                <Name>Jhon Doe</Name>
                <Type>1</Type>
        </User>

RESPONSE:

.. code-block:: xml

        <?xml version="1.0" encoding="UTF-8"?>
        <User href="http://localhost/resources/Sample/User/1">
                <Id>1</Id>
        </User>

Now we have successfully inserted a user in the database that also has a type, so now if you access http://localhost/resources/Sample/User/1

.. code-block:: xml

        <?xml version="1.0" encoding="UTF-8"?>
        <User>
                <Type href="http://localhost/resources/Sample/UserType/1">
                        <Id>1</Id>
                </Type>
                <Id>1</Id>
                <Name>Jhon Doe</Name>
        </User>

, you have the new user model with a user type reference. The sample code can be found here.

Extending Models
-------------------------------

The extending is when a service provides models based on another model id, even if the provided models are not associated with the other
model. The extending requires only the modification of the service's APIs and implementations.  sample_plugin.api.user

.. code-block:: python

        from ally.api.config import service, query, call
        from ally.api.criteria import AsLike
        from ally.api.type import Iter
        from sample_plugin.api import modelSample
        from sample_plugin.api.user_type import UserType
        from sql_alchemy.api.entity import Entity, QEntity, IEntityService
        ...
        # --------------------------------------------------------------------
        @service((Entity, User), (QEntity, QUser))
        class IUserService(IEntityService):
        '''
        The user service.
        '''
        @call
        def getUsersByType(self, typeId:UserType.Id, offset:int=None, limit:int=None,
        q:QUser=None)->Iter(User):
        '''
        Provides the users that have the specified type id.
        '''

We added a service method that will deliver all the users that have the specified type id, also the service method will allow the specification of
offset, limit and user query.sample_plugin.impl.user

.. code-block:: python

        from sample_plugin.api.user import IUserService, QUser
        from sample_plugin.meta.user import User
        from sql_alchemy.impl.entity import EntityServiceAlchemy
        # --------------------------------------------------------------------
        class UserService(EntityServiceAlchemy, IUserService):
        '''
        Implementation for @see: IUserService
        '''
        def __init__(self):
        EntityServiceAlchemy.__init__(self, User, QUser)
        def getUsersByType(self, typeId, offset=None, limit=None, q=None):
        '''
        @see: IUserService.getUsersByType
        '''
        return self._getAll(User.Type == typeId, q, offset, limit)

The implementation is very easy because it makes use of the _getAll method inherited from EntitySupportAlchemy that allows for an easy get
of models from database. So now we have a service method that provides user models based on a user type, if we access
http://localhost/resources/Sample/UserType/1 we get:

.. code-block:: xml

        <?xml version="1.0" encoding="UTF-8"?>
        <UserType>
                <Id>1</Id>
                <Name>root</Name>
                <User href="http://localhost/resources/Sample/UserType/1/User/"/>
        </UserType>

Now, beside the UserType model data we also have a new reference for the User models that belong to this UserType, this reference will call our new service method. The idea is that we are able to add information on existing models like UserType from a different service than the main main user type service.
