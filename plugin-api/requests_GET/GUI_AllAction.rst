.. _reuqest-GET-GUI/AllAction:

**GUI/AllAction**
==========================================================

* Use the HTTP **GET** method
* The request is defined by API call ``gui.action.api.action.IActionManagerService.getAll``

* The request will GET a collection of references to models :ref:`entity-gui.action.api.action.Action`

::

   Provides the entities identifiers.
   
   @param options: @see: SliceAndTotal
       The options to fetch the entities with.
   @return: Iterable(object)
       The iterable with the entities identifiers.




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

