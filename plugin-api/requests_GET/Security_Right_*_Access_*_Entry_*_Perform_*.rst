.. _reuqest-GET-Security/Right/*/Access/*/Entry/*/Perform/*:

**Security/Right/*/Access/*/Entry/*/Perform/***
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
* The unique identifier **Access.Id** from :ref:`entity-acl.api.access.Access`.
* The unique identifier **Entry.Position** from :ref:`entity-acl.api.access.Entry`.
* The unique identifier **Perform.Id** from :ref:`entity-indexing.api.indexing.Perform`.


Query parameters
-------------------------------------
There are no query parameters available for this request except for global :ref:`headers_parameters`.
