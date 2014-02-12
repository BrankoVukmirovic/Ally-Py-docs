.. _reuqest-GET-HR/User/*/RightType/*/Perform/*:

**HR/User/*/RightType/*/Perform/***
==========================================================

* Use the HTTP **GET** method
* The request is defined by API call ``indexing.api.indexing.IIndexingService.getPerform``

  
* The request will GET a model :ref:`entity-indexing.api.indexing.Perform`

::

   Provides the perform for id.


URL parameters
-------------------------------------
Each entry matches a **\*** in their respective order.

* The unique identifier **User.Id** from :ref:`entity-superdesk.user.api.user.User`.
* The unique identifier **RightType.Name** from :ref:`entity-security.api.right_type.RightType`.
* The unique identifier **Perform.Id** from :ref:`entity-indexing.api.indexing.Perform`.


Query parameters
-------------------------------------
There are no query parameters available for this request except for global :ref:`headers_parameters`.
