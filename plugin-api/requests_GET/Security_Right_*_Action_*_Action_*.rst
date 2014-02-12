.. _reuqest-GET-Security/Right/*/Action/*/Action/*:

**Security/Right/*/Action/*/Action/***
==========================================================

* Use the HTTP **GET** method
* The request is defined by API call ``indexing.api.indexing.IIndexingService.getAction``

  
* The request will GET a model :ref:`entity-indexing.api.indexing.Action`

::

   Provides the action for id.


URL parameters
-------------------------------------
Each entry matches a **\*** in their respective order.

* The unique identifier **Right.Id** from :ref:`entity-security.api.right.Right`.
* The unique identifier **Action.Path** from :ref:`entity-gui.action.api.action.Action`.
* The unique identifier **Action.Id** from :ref:`entity-indexing.api.indexing.Action`.


Query parameters
-------------------------------------
There are no query parameters available for this request except for global :ref:`headers_parameters`.
