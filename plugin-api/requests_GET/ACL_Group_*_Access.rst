.. _reuqest-GET-ACL/Group/*/Access:

**ACL/Group/*/Access**
==========================================================

* Use the HTTP **GET** method
* The request is defined by API call ``acl.api.group.IGroupService.getAccesses``

* The request will GET a collection of references to models :ref:`entity-acl.api.access.Access`

::

   Provides the allowed access for the ACL object identifier.
   
   @param identifier: object
       The ACL object identifier to provide the access for.
   @param options: key arguments
       The result iteration options.
   @return: Iterable(Access.Id)
       An iterator containing the access ids.


URL parameters
-------------------------------------
Each entry matches a **\*** in their respective order.

* The unique identifier **Group.Name** from :ref:`entity-acl.api.group.Group`.


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

