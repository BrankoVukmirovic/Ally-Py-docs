.. _reuqest-GET-Indexing/Action/*/Perform:

**Indexing/Action/*/Perform**
==========================================================

* Use the HTTP **GET** method
* The request is defined by API call ``indexing.api.indexing.IIndexingService.getPerforms``

* The request will GET a collection of references to models :ref:`entity-indexing.api.indexing.Perform`

::

   Provides all performs for action id.


URL parameters
-------------------------------------
Each entry matches a **\*** in their respective order.

* The unique identifier **Action.Id** from :ref:`entity-indexing.api.indexing.Action`.


Query parameters
-------------------------------------
There are no query parameters available for this request except for global :ref:`headers_parameters`.
