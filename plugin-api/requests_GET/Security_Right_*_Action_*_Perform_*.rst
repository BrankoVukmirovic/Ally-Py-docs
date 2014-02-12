.. _reuqest-GET-Security/Right/*/Action/*/Perform/*:

**Security/Right/*/Action/*/Perform/***
==========================================================

* Use the HTTP **GET** method
* The request is defined by API call ``indexing.api.indexing.IIndexingService.getPerform``

  
* The request will GET a model :ref:`entity-indexing.api.indexing.Perform`

::

   Provides the perform for id.


URL parameters
-------------------------------------
Each entry matches a **\*** in their respective order.

* The unique identifier **Right.Id** from :ref:`entity-security.api.right.Right`.
* The unique identifier **Action.Path** from :ref:`entity-gui.action.api.action.Action`.
* The unique identifier **Perform.Id** from :ref:`entity-indexing.api.indexing.Perform`.


Query parameters
-------------------------------------
There are no query parameters available for this request except for global :ref:`headers_parameters`.
