.. _reuqest-GET-HR/User/*/RightType/*/Right:

**HR/User/*/RightType/*/Right**
==========================================================

* Use the HTTP **GET** method
* The request is defined by API call ``superdesk.security.api.user_rbac.IUserRbacService.getRights``

* The request will GET a collection of references to models :ref:`entity-security.api.right.Right`

::

   Provides the rights for the provided identifier.
   
   @param identifier: object
       The RBAC object identifier to provide the rights for.
   @param typeName: string|None
       The right type name to provide the rights for, if not provided all rights will be iterated.
   @param q: QRight|None
       The query to apply on the rights.
   @param options: key arguments
       The result iteration options.
   @return: Iterable(Right.Id)
       An iterator containing the rights ids.


URL parameters
-------------------------------------
Each entry matches a **\*** in their respective order.

* The unique identifier **User.Id** from :ref:`entity-superdesk.user.api.user.User`.
* The unique identifier **RightType.Name** from :ref:`entity-security.api.right_type.RightType`.


Query parameters
-------------------------------------
This are the available query parameters, also check the global :ref:`headers_parameters`.

+------------+------------+--------------------------------------------------------------------------+
|  Parameter |   Accepts  |                                Description                               |
+============+============+==========================================================================+
| withTotal  | * **bool** |                                                                          |
|            |            | Indicates that the total count of the collection has to be provided      |
|            |            | If no value is provided it defaults to *True*                            |
+------------+------------+--------------------------------------------------------------------------+
| limit      | * **int**  |                                                                          |
|            |            | Indicates the number of entities to be retrieved from a collection       |
|            |            | If no value is provided it defaults to *30*                              |
|            |            | The maximum value is *100*                                               |
+------------+------------+--------------------------------------------------------------------------+
| offset     | * **int**  |                                                                          |
|            |            | Indicates the start offset in a collection from where to retrieve        |
+------------+------------+--------------------------------------------------------------------------+
| name.ilike | * **str**  |                                                                          |
|            |            | Filters the results in a case insensitive like search                    |
|            |            | You can use % for unknown characters                                     |
+------------+------------+--------------------------------------------------------------------------+
| name.like  | * **str**  |                                                                          |
|            |            | Filters the results in a like search                                     |
|            |            | You can use % for unknown characters                                     |
+------------+------------+--------------------------------------------------------------------------+
| name       | * **str**  |                                                                          |
|            |            | Will automatically set the value to                                      |
|            |            |   * *name.like*                                                          |
|            |            |                                                                          |
+------------+------------+--------------------------------------------------------------------------+
| asc        | One of:    |                                                                          |
|            |            | Provide the names that you want to order by ascending                    |
|            | * *name*   | The order in which the names are provided establishes the order priority |
+------------+------------+--------------------------------------------------------------------------+
| desc       | One of:    |                                                                          |
|            |            | Provide the names that you want to order by descending                   |
|            | * *name*   | The order in which the names are provided establishes the order priority |
+------------+------------+--------------------------------------------------------------------------+

