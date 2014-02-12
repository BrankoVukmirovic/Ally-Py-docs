.. _reuqest-GET-Localization/AvailableLanguage:

**Localization/AvailableLanguage**
==========================================================

* Use the HTTP **GET** method
* The request is defined by API call ``internationalization.language.api.language.ILanguageService.getAllAvailable``

* The request will GET a collection of references to models :ref:`entity-internationalization.language.api.language.Language`

::

   Provides all the available languages.




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

