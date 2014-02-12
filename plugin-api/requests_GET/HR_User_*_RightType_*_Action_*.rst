.. _reuqest-GET-HR/User/*/RightType/*/Action/*:

**HR/User/*/RightType/*/Action/***
==========================================================

* Use the HTTP **GET** method
* The request is defined by API call ``indexing.api.indexing.IIndexingService.getAction``

  
* The request will GET a model :ref:`entity-indexing.api.indexing.Action`

::

   Provides the action for id.


URL parameters
-------------------------------------
Each entry matches a **\*** in their respective order.

* The unique identifier **User.Id** from :ref:`entity-superdesk.user.api.user.User`.
* The unique identifier **RightType.Name** from :ref:`entity-security.api.right_type.RightType`.
* The unique identifier **Action.Id** from :ref:`entity-indexing.api.indexing.Action`.


Query parameters
-------------------------------------
There are no query parameters available for this request except for global :ref:`headers_parameters`.
