.. _reuqest-GET-ACL/Access:

**ACL/Access**
==========================================================

 * The request is defined by API call ``acl.api.access.IAccessService.getAll``

 * The request will GET a collection of references to models ``acl.api.access.Access``

URL parameters
-------------------------------------
TODO:


Query parameters
-------------------------------------
This are the available query parameters, also check the global :ref:`headers_parameters`.

+----------------+------------+--------------------------------------------------------------------------+
|    Parameter   |   Accepts  |                                Description                               |
+================+============+==========================================================================+
| withTotal      | * **bool** |                                                                          |
|                |            | Indicates that the total count of the collection has to be provided      |
|                |            | If no value is provided it defaults to *True*                            |
+----------------+------------+--------------------------------------------------------------------------+
| limit          | * **int**  |                                                                          |
|                |            | Indicates the number of entities to be retrieved from a collection       |
|                |            | If no value is provided it defaults to *30*                              |
|                |            | The maximum value is *100*                                               |
+----------------+------------+--------------------------------------------------------------------------+
| offset         | * **int**  |                                                                          |
|                |            | Indicates the start offset in a collection from where to retrieve        |
+----------------+------------+--------------------------------------------------------------------------+
| path.ilike     | * **str**  |                                                                          |
|                |            | Filters the results in a case insensitive like search                    |
|                |            | You can use % for unknown characters                                     |
+----------------+------------+--------------------------------------------------------------------------+
| path.like      | * **str**  |                                                                          |
|                |            | Filters the results in a like search                                     |
|                |            | You can use % for unknown characters                                     |
+----------------+------------+--------------------------------------------------------------------------+
| path           | * **str**  |                                                                          |
|                |            | Will automatically set the value to                                      |
|                |            |   * *path.like*                                                          |
|                |            |                                                                          |
+----------------+------------+--------------------------------------------------------------------------+
| isShadow.value | * **bool** |                                                                          |
+----------------+------------+--------------------------------------------------------------------------+
| isShadow       | * **bool** |                                                                          |
|                |            | Will automatically set the value to                                      |
|                |            |   * *isShadow.value*                                                     |
|                |            |                                                                          |
+----------------+------------+--------------------------------------------------------------------------+
| method.equal   | * **str**  |                                                                          |
+----------------+------------+--------------------------------------------------------------------------+
| method         | * **str**  |                                                                          |
|                |            | Will automatically set the value to                                      |
|                |            |   * *method.equal*                                                       |
|                |            |                                                                          |
+----------------+------------+--------------------------------------------------------------------------+
| asc            | One of:    |                                                                          |
|                |            | Provide the names that you want to order by ascending                    |
|                | * *method* | The order in which the names are provided establishes the order priority |
|                | * *path*   |                                                                          |
+----------------+------------+--------------------------------------------------------------------------+
| desc           | One of:    |                                                                          |
|                |            | Provide the names that you want to order by descending                   |
|                | * *method* | The order in which the names are provided establishes the order priority |
|                | * *path*   |                                                                          |
+----------------+------------+--------------------------------------------------------------------------+

