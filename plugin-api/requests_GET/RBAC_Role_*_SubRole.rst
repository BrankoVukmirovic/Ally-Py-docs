.. _reuqest-GET-RBAC/Role/*/SubRole:

**RBAC/Role/*/SubRole**
==========================================================

 * The request is defined by API call ``security.rbac.api.role_rbac.IRoleRbacService.getRoles``

 * The request will GET a collection of references to models ``security.rbac.api.role.Role``

URL parameters
-------------------------------------
TODO:


Query parameters
-------------------------------------
This are the available query parameters, also check the global :ref:`headers_parameters`.

+-------------------+-----------------+--------------------------------------------------------------------------+
|     Parameter     |     Accepts     |                                Description                               |
+===================+=================+==========================================================================+
| withTotal         | * **bool**      |                                                                          |
|                   |                 | Indicates that the total count of the collection has to be provided      |
|                   |                 | If no value is provided it defaults to *True*                            |
+-------------------+-----------------+--------------------------------------------------------------------------+
| limit             | * **int**       |                                                                          |
|                   |                 | Indicates the number of entities to be retrieved from a collection       |
|                   |                 | If no value is provided it defaults to *30*                              |
|                   |                 | The maximum value is *100*                                               |
+-------------------+-----------------+--------------------------------------------------------------------------+
| offset            | * **int**       |                                                                          |
|                   |                 | Indicates the start offset in a collection from where to retrieve        |
+-------------------+-----------------+--------------------------------------------------------------------------+
| description.ilike | * **str**       |                                                                          |
|                   |                 | Filters the results in a case insensitive like search                    |
|                   |                 | You can use % for unknown characters                                     |
+-------------------+-----------------+--------------------------------------------------------------------------+
| description.like  | * **str**       |                                                                          |
|                   |                 | Filters the results in a like search                                     |
|                   |                 | You can use % for unknown characters                                     |
+-------------------+-----------------+--------------------------------------------------------------------------+
| description       | * **str**       |                                                                          |
|                   |                 | Will automatically set the value to                                      |
|                   |                 |   * *description.like*                                                   |
|                   |                 |                                                                          |
+-------------------+-----------------+--------------------------------------------------------------------------+
| asc               | One of:         |                                                                          |
|                   |                 | Provide the names that you want to order by ascending                    |
|                   | * *description* | The order in which the names are provided establishes the order priority |
+-------------------+-----------------+--------------------------------------------------------------------------+
| desc              | One of:         |                                                                          |
|                   |                 | Provide the names that you want to order by descending                   |
|                   | * *description* | The order in which the names are provided establishes the order priority |
+-------------------+-----------------+--------------------------------------------------------------------------+

