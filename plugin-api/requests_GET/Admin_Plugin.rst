.. _reuqest-GET-Admin/Plugin:

**Admin/Plugin**
==========================================================

 * The request is defined by API call ``admin.introspection.api.plugin.IPluginService.getAll``

 * The request will GET a collection of references to models ``admin.introspection.api.plugin.Plugin``

URL parameters
-------------------------------------
TODO:


Query parameters
-------------------------------------
This are the available query parameters, also check the global :ref:`headers_parameters`.

+---------------+------------+---------------------------------------------------------------------+
|   Parameter   |   Accepts  |                             Description                             |
+===============+============+=====================================================================+
| withTotal     | * **bool** |                                                                     |
|               |            | Indicates that the total count of the collection has to be provided |
|               |            | If no value is provided it defaults to *True*                       |
+---------------+------------+---------------------------------------------------------------------+
| limit         | * **int**  |                                                                     |
|               |            | Indicates the number of entities to be retrieved from a collection  |
|               |            | If no value is provided it defaults to *30*                         |
|               |            | The maximum value is *100*                                          |
+---------------+------------+---------------------------------------------------------------------+
| offset        | * **int**  |                                                                     |
|               |            | Indicates the start offset in a collection from where to retrieve   |
+---------------+------------+---------------------------------------------------------------------+
| group.like    | * **str**  |                                                                     |
|               |            | Filters the results in a like search                                |
|               |            | You can use % for unknown characters                                |
+---------------+------------+---------------------------------------------------------------------+
| group.ilike   | * **str**  |                                                                     |
|               |            | Filters the results in a case insensitive like search               |
|               |            | You can use % for unknown characters                                |
+---------------+------------+---------------------------------------------------------------------+
| group         | * **str**  |                                                                     |
|               |            | Will automatically set the value to                                 |
|               |            |   * *group.like*                                                    |
|               |            |                                                                     |
+---------------+------------+---------------------------------------------------------------------+
| name.like     | * **str**  |                                                                     |
|               |            | Filters the results in a like search                                |
|               |            | You can use % for unknown characters                                |
+---------------+------------+---------------------------------------------------------------------+
| name.ilike    | * **str**  |                                                                     |
|               |            | Filters the results in a case insensitive like search               |
|               |            | You can use % for unknown characters                                |
+---------------+------------+---------------------------------------------------------------------+
| name          | * **str**  |                                                                     |
|               |            | Will automatically set the value to                                 |
|               |            |   * *name.like*                                                     |
|               |            |                                                                     |
+---------------+------------+---------------------------------------------------------------------+
| version.like  | * **str**  |                                                                     |
|               |            | Filters the results in a like search                                |
|               |            | You can use % for unknown characters                                |
+---------------+------------+---------------------------------------------------------------------+
| version.ilike | * **str**  |                                                                     |
|               |            | Filters the results in a case insensitive like search               |
|               |            | You can use % for unknown characters                                |
+---------------+------------+---------------------------------------------------------------------+
| version       | * **str**  |                                                                     |
|               |            | Will automatically set the value to                                 |
|               |            |   * *version.like*                                                  |
|               |            |                                                                     |
+---------------+------------+---------------------------------------------------------------------+
| path.like     | * **str**  |                                                                     |
|               |            | Filters the results in a like search                                |
|               |            | You can use % for unknown characters                                |
+---------------+------------+---------------------------------------------------------------------+
| path.ilike    | * **str**  |                                                                     |
|               |            | Filters the results in a case insensitive like search               |
|               |            | You can use % for unknown characters                                |
+---------------+------------+---------------------------------------------------------------------+
| path          | * **str**  |                                                                     |
|               |            | Will automatically set the value to                                 |
|               |            |   * *path.like*                                                     |
|               |            |                                                                     |
+---------------+------------+---------------------------------------------------------------------+
| inEgg.value   | * **bool** |                                                                     |
+---------------+------------+---------------------------------------------------------------------+
| inEgg         | * **bool** |                                                                     |
|               |            | Will automatically set the value to                                 |
|               |            |   * *inEgg.value*                                                   |
|               |            |                                                                     |
+---------------+------------+---------------------------------------------------------------------+
| loaded.value  | * **bool** |                                                                     |
+---------------+------------+---------------------------------------------------------------------+
| loaded        | * **bool** |                                                                     |
|               |            | Will automatically set the value to                                 |
|               |            |   * *loaded.value*                                                  |
|               |            |                                                                     |
+---------------+------------+---------------------------------------------------------------------+

