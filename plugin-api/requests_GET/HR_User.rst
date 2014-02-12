.. _reuqest-GET-HR/User:

**HR/User**
==========================================================

* Use the HTTP **GET** method
* The request is defined by API call ``superdesk.user.api.user.IUserService.getAll``

* The request will GET a collection of references to models :ref:`entity-superdesk.user.api.user.User`

::

   Provides the entities identifiers searched by the provided query.
   
   @param q: Query|None
       The query to search by.
   @param options: @see: SliceAndTotal
       The options to fetch the entities with.
   @return: Iterable(object)
       The iterable with the entities identifiers.




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
| all.like          | * **str**       |                                                                          |
|                   |                 | Filters the results in a like search                                     |
|                   |                 | You can use % for unknown characters                                     |
+-------------------+-----------------+--------------------------------------------------------------------------+
| all.ilike         | * **str**       |                                                                          |
|                   |                 | Filters the results in a case insensitive like search                    |
|                   |                 | You can use % for unknown characters                                     |
+-------------------+-----------------+--------------------------------------------------------------------------+
| all               | * **str**       |                                                                          |
|                   |                 | Will automatically set the value to                                      |
|                   |                 |   * *all.like*                                                           |
|                   |                 |                                                                          |
+-------------------+-----------------+--------------------------------------------------------------------------+
| name.ilike        | * **str**       |                                                                          |
|                   |                 | Filters the results in a case insensitive like search                    |
|                   |                 | You can use % for unknown characters                                     |
+-------------------+-----------------+--------------------------------------------------------------------------+
| name.like         | * **str**       |                                                                          |
|                   |                 | Filters the results in a like search                                     |
|                   |                 | You can use % for unknown characters                                     |
+-------------------+-----------------+--------------------------------------------------------------------------+
| name              | * **str**       |                                                                          |
|                   |                 | Will automatically set the value to                                      |
|                   |                 |   * *name.like*                                                          |
|                   |                 |                                                                          |
+-------------------+-----------------+--------------------------------------------------------------------------+
| firstName.ilike   | * **str**       |                                                                          |
|                   |                 | Filters the results in a case insensitive like search                    |
|                   |                 | You can use % for unknown characters                                     |
+-------------------+-----------------+--------------------------------------------------------------------------+
| firstName.like    | * **str**       |                                                                          |
|                   |                 | Filters the results in a like search                                     |
|                   |                 | You can use % for unknown characters                                     |
+-------------------+-----------------+--------------------------------------------------------------------------+
| firstName         | * **str**       |                                                                          |
|                   |                 | Will automatically set the value to                                      |
|                   |                 |   * *firstName.like*                                                     |
|                   |                 |                                                                          |
+-------------------+-----------------+--------------------------------------------------------------------------+
| lastName.ilike    | * **str**       |                                                                          |
|                   |                 | Filters the results in a case insensitive like search                    |
|                   |                 | You can use % for unknown characters                                     |
+-------------------+-----------------+--------------------------------------------------------------------------+
| lastName.like     | * **str**       |                                                                          |
|                   |                 | Filters the results in a like search                                     |
|                   |                 | You can use % for unknown characters                                     |
+-------------------+-----------------+--------------------------------------------------------------------------+
| lastName          | * **str**       |                                                                          |
|                   |                 | Will automatically set the value to                                      |
|                   |                 |   * *lastName.like*                                                      |
|                   |                 |                                                                          |
+-------------------+-----------------+--------------------------------------------------------------------------+
| createdOn.end     | * **datetime**  |                                                                          |
|                   |                 | Example *1982-01-18T02:40:12Z*                                           |
+-------------------+-----------------+--------------------------------------------------------------------------+
| createdOn.since   | * **datetime**  |                                                                          |
|                   |                 | Example *1982-01-18T02:40:12Z*                                           |
+-------------------+-----------------+--------------------------------------------------------------------------+
| createdOn.start   | * **datetime**  |                                                                          |
|                   |                 | Example *1982-01-18T02:40:12Z*                                           |
+-------------------+-----------------+--------------------------------------------------------------------------+
| createdOn.until   | * **datetime**  |                                                                          |
|                   |                 | Example *1982-01-18T02:40:12Z*                                           |
+-------------------+-----------------+--------------------------------------------------------------------------+
| createdOn         | * **datetime**  |                                                                          |
|                   |                 | Will automatically set the value to                                      |
|                   |                 |   * *createdOn.start*                                                    |
|                   |                 |   * *createdOn.end*                                                      |
|                   |                 |                                                                          |
+-------------------+-----------------+--------------------------------------------------------------------------+
| inactive.value    | * **bool**      |                                                                          |
+-------------------+-----------------+--------------------------------------------------------------------------+
| inactive          | * **bool**      |                                                                          |
|                   |                 | Will automatically set the value to                                      |
|                   |                 |   * *inactive.value*                                                     |
|                   |                 |                                                                          |
+-------------------+-----------------+--------------------------------------------------------------------------+
| phoneNumber.ilike | * **str**       |                                                                          |
|                   |                 | Filters the results in a case insensitive like search                    |
|                   |                 | You can use % for unknown characters                                     |
+-------------------+-----------------+--------------------------------------------------------------------------+
| phoneNumber.like  | * **str**       |                                                                          |
|                   |                 | Filters the results in a like search                                     |
|                   |                 | You can use % for unknown characters                                     |
+-------------------+-----------------+--------------------------------------------------------------------------+
| phoneNumber       | * **str**       |                                                                          |
|                   |                 | Will automatically set the value to                                      |
|                   |                 |   * *phoneNumber.like*                                                   |
|                   |                 |                                                                          |
+-------------------+-----------------+--------------------------------------------------------------------------+
| email.ilike       | * **str**       |                                                                          |
|                   |                 | Filters the results in a case insensitive like search                    |
|                   |                 | You can use % for unknown characters                                     |
+-------------------+-----------------+--------------------------------------------------------------------------+
| email.like        | * **str**       |                                                                          |
|                   |                 | Filters the results in a like search                                     |
|                   |                 | You can use % for unknown characters                                     |
+-------------------+-----------------+--------------------------------------------------------------------------+
| email             | * **str**       |                                                                          |
|                   |                 | Will automatically set the value to                                      |
|                   |                 |   * *email.like*                                                         |
|                   |                 |                                                                          |
+-------------------+-----------------+--------------------------------------------------------------------------+
| asc               | One of:         |                                                                          |
|                   |                 | Provide the names that you want to order by ascending                    |
|                   | * *createdOn*   | The order in which the names are provided establishes the order priority |
|                   | * *email*       |                                                                          |
|                   | * *firstName*   |                                                                          |
|                   | * *lastName*    |                                                                          |
|                   | * *name*        |                                                                          |
|                   | * *phoneNumber* |                                                                          |
+-------------------+-----------------+--------------------------------------------------------------------------+
| desc              | One of:         |                                                                          |
|                   |                 | Provide the names that you want to order by descending                   |
|                   | * *createdOn*   | The order in which the names are provided establishes the order priority |
|                   | * *email*       |                                                                          |
|                   | * *firstName*   |                                                                          |
|                   | * *lastName*    |                                                                          |
|                   | * *name*        |                                                                          |
|                   | * *phoneNumber* |                                                                          |
+-------------------+-----------------+--------------------------------------------------------------------------+

