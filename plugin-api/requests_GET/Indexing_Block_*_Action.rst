.. _reuqest-GET-Indexing/Block/*/Action:

**Indexing/Block/*/Action**
==========================================================

* Use the HTTP **GET** method
* The request is defined by API call ``indexing.api.indexing.IIndexingService.getActions``

* The request will GET a collection of references to models :ref:`entity-indexing.api.indexing.Action`

::

   Provides all indexing actions for block.


URL parameters
-------------------------------------
Each entry matches a **\*** in their respective order.

* The unique identifier **Block.Id** from :ref:`entity-indexing.api.indexing.Block`.


Query parameters
-------------------------------------
There are no query parameters available for this request except for global :ref:`headers_parameters`.
