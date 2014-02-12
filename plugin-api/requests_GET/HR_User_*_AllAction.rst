.. _reuqest-GET-HR/User/*/AllAction:

**HR/User/*/AllAction**
==========================================================

* Use the HTTP **GET** method
* The request is defined by API call ``superdesk.security.api.user_rbac.IUserRbacService.getActions``

* The request will GET a collection of references to models :ref:`entity-gui.action.api.action.Action`

::

   Provides all the actions paths for the provided identifier.
   
   @param identifier: object
       The action category object identifier.
   @param options: key arguments
       The result iteration options.
   @return: Iterable(Action.Path)
       An iterator containing the action paths.


URL parameters
-------------------------------------
Each entry matches a **\*** in their respective order.

* The unique identifier **User.Id** from :ref:`entity-superdesk.user.api.user.User`.


Query parameters
-------------------------------------
This are the available query parameters, also check the global :ref:`headers_parameters`.

+-----------+------------+---------------------------------------------------------------------+
| Parameter |   Accepts  |                             Description                             |
+===========+============+=====================================================================+
| withTotal | * **bool** |                                                                     |
|           |            | Indicates that the total count of the collection has to be provided |
|           |            | If no value is provided it defaults to *True*                       |
+-----------+------------+---------------------------------------------------------------------+
| limit     | * **int**  |                                                                     |
|           |            | Indicates the number of entities to be retrieved from a collection  |
|           |            | If no value is provided it defaults to *30*                         |
|           |            | The maximum value is *100*                                          |
+-----------+------------+---------------------------------------------------------------------+
| offset    | * **int**  |                                                                     |
|           |            | Indicates the start offset in a collection from where to retrieve   |
+-----------+------------+---------------------------------------------------------------------+

