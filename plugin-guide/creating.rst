.. _Creating:

Creating a plugin
=================

In this guide We will create a simple plugin called ``sample_plugin`` with the structure described in :ref:`Structure`.

Describing the API
------------------

The first example is based on a model of a user, with a name and an id number.  Create the module ``user`` in ``sample_plugin.api.user`` containing:

.. code-block:: python

        class User:
                '''
                The user model.
                '''
                Id = int
                Name = str


Add the Ally.py egg to the python path.               

add to python path
        ``distribution/components/ally-api.1.0.egg``

To make the class recognizable by the Ally.py framework, edit the previous code to import the Ally.py model, specify the attribute to use as a unique id by passing it as a keyed argument to the model decorator (this is required for all Ally.py models) and specify a domain (similar to a namespace).

.. code-block:: python

   from ally.api.config import model

   @model(id='Id', domain='Sample')
   class User:
        '''
        The user model.
        '''
        Id = int
        Name = str

Without a domain, the model is accessible at `User <http://localhost/resources/User>`_ , but with domain set to 'Sample' the domain is accessible at `Sample/User <http://localhost/resources/Sample/User>`_.

To reuse a domain definition in various modules or plugins, define a domained model decorator in the ``sample_plugin.api.__init__`` module::

   from functools import partial
   from ally.api.config import model
   
   # --------------------------------------------------------------------

   modelSample = partial(model, domain='Sample')

And edit the decorated user model in ``sample_plugin.api.user``::

        from sample_plugin.api import modelSample

        # --------------------------------------------------------------------

        @modelSample(id='Id')
        class User:
                '''
                The user model.
                '''
                Id = int
                Name = str
        


To complement the model, we need to add a service to deliver instances of the model as a REST response in ``sample_plugin.api.user``: 

.. code-block:: python

        from ally.api.config import service, call
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

        @service
        class IUserService:
                '''
                The user service.
                '''
                @call
                def getUsers(self) -> Iter(User):
                        '''
                        Provides all the users.
                        '''

All service interface names start with a capital 'I' followed by the service name and ending in 'Service' and are decorated with ``@service``. This convention simplifies Ally.py inversion of control and aspect oriented programming configuration. Each method that exposes a response model is decorated with ``@call`` and annoted with the return type. In the previous example, the return type is an interable collection of User models.  The Ally.py framework maps annotated return and input types to a path invoking the corresponding service method. All service methods, even those not exposed using the ``@call`` decorator must have input and return types annotated. 

.. TODO:: 
        [SW] This is not totally clear to me. "framework, also each method definition that needs to be considered as exposing response models needs to be decorated with call. We need to annotate the method with the return type of the method in this case is an iterable collection that contains User models. The ally framework uses"

Implementing the API
----------------------------------------------

After defining the API we can create an implementation based upon it, returning a list with one user model at the address `Sample/User <http://localhost/resources/Sample/User>`_:

.. code-block:: xml

        <UserList>
                <User>
                        <Name>User 1</Name>
                        <Id>1</Id>
                </User>
        </UserList>

To achieve this, edit the user implementation in ``sample_plugin.impl.user`` ::

        from sample_plugin.api.user import IUserService, User

        # --------------------------------------------------------------------

        class UserService(IUserService):
                '''
                Implementation for @see: IUserService
                '''

                def getUsers(self):
                        '''
                        @see: IUserService.getUsers
                        '''
                        users = []
                        for k in range(1, 2):
                                user = User()
                                user.Id = k
                                user.Name = 'User %s' % k
                                users.append(user)
                        return users

To return more than one user adjust the range. 

Creating the configuration
--------------------------

After defining the API and the implementation of the API, use the dependency injection container to expose the API through the HTTP REST interface of the Ally.py framework. Create the module ``service`` in package ``__plugin __.sample_plugin.service`` 

We have defined a setup function decorated with ``@ioc.entity`` that delivers the implementation instance of ``UserService`` for the ``IUserService`` api.  Because this function is decorated with the ioc.entity decorator it will be used as a entity source by the DI container. 

The register method will register the user service implementation instance to be used exposed, please notice that the instance is obtained by invoking the DI entity function userService.

.. code-block:: python

        from __plugin__.plugin.registry import registerService
        from ally.container import ioc
        from sample_plugin.api.user import IUserService
        from sample_plugin.impl.user import UserService

        # --------------------------------------------------------------------

        @ioc.entity
        def userService() -> IUserService:
                b = UserService()
                return b

        @ioc.start
        def register():
                registerService(userService())


Packaging and Deploying
-----------------------

The plugin is now fully functional, but we need to package it up for deployment to the application using ``build-plugin.ant`` :

The ant script creates ``02 - plugin sample.1.0.egg`` in the plugin ``source`` folder. To deploy the plugin, copy the file into the ``distribution/plugin/`` folder of your application. If the application is running on localhost port 80, access your plugin at http://localhost/resources and verify that the resource SampleUser exists:

.. code-block:: xml

        <Resources>
                <SampleUser href="http://localhost/resources/Sample/User/" />
                ...
        </Resources>

Querying and Filtering
------------------------

To filter the list of users use ``@query`` as shown in ``objects.sample_plugin.api.user``:

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

        ...

Query objects are like a models that contains data used for filtering. Queries have the name of the model and are prefixed with 'Q', and attributes are lower case to avoid confusion with the model attributes. Query attribute values are the criteria class of the model attribute. ``AsLike`` enables filtering and ordering on an attribute.

.. code-block:: python 

        ...

        @service
        class IUserService:
                '''
                The user service.
                '''

                @call
                def getUsers(self, q:QUser=None) -> Iter(User):
                        '''
                        Provides all the users.
                        '''

The ``getUsers`` method now takes an query object instance as an optional parameter (with a default value of None). It is good practice to specify a default value for all query objects used in service methods, as queries are optional. 

.. code-block:: python 

        from sample_plugin.api.user import IUserService, User, QUser
        from ally.support.api.util_service import likeAsRegex

        # --------------------------------------------------------------------

        class UserService(IUserService):
                '''
                Implementation for @see: IUserService
                '''

                def getUsers(self, q=None):
                        '''
                        @see: IUserService.getUsers
                        '''
                        users = []
                        for k in range(1, 10):
                                user = User()
                                user.Id = k
                                user.Name = 'User %s' % k
                                users.append(user)

                        if q:
                                assert isinstance(q, QUser)
                                if QUser.name.like in q:
                                        nameRegex = likeAsRegex(q.name.like)
                                        users = [user for user in users if nameRegex.match(user.Name)]
                                if QUser.name.ascending in q:
                                        users.sort(key=lambda user: user.Name, reverse=not q.name.ascending)

                        return users


``getUsers`` now returns 10 users, and checks if query object exists. If a query object exists and has a specified like value in the name criteria, we generate a regular expression and filter the user list accordingly. If the ascending flag exists, we sort the user list in ascending order. 

Redeploy the plugin then view all ten users at `/Sample/User <http://localhost/resources/Sample/User>`_. View only the seventh user at `/Sample/User?name=%7 <http://localhost/resources/Sample/User?name=%7>`_ and sort the user list at `/Sample/User?asc=name <http://localhost/resources/Sample/User?asc=name>`_.

Download the `example egg <https://github.com/sourcefabric/Ally-Py-docs/blob/master/plugin-guide/source_code/02_-_query_plugin_sample/sample_plugin-1.0.dev-py3.2.egg>`_
