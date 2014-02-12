.. _reuqest-GET-Security/Right/*/Action/*/SubAction:

**Security/Right/*/Action/*/SubAction**
==========================================================

* Use the HTTP **GET** method
* The request is defined by API call ``gui.action.api.category_right.IActionRightService.getSubActions``

* The request will GET a collection of references to models :ref:`entity-gui.action.api.action.Action`

::

   Provides the actions paths for the provided identifier and parent path.
   
   @param identifier: object
       The action category object identifier.
   @param parentPath: string
       THe parent path to provide the actions for.
   @param options: key arguments
       The result iteration options.
   @return: Iterable(Action.Path)
       An iterator containing the action paths.


URL parameters
-------------------------------------
Each entry matches a **\*** in their respective order.

* The unique identifier **Right.Id** from :ref:`entity-security.api.right.Right`.
* The unique identifier **Action.Path** from :ref:`entity-gui.action.api.action.Action`.


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

