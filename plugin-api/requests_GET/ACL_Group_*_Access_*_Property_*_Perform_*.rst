.. _reuqest-GET-ACL/Group/*/Access/*/Property/*/Perform/*:

**ACL/Group/*/Access/*/Property/*/Perform/***
==========================================================

* Use the HTTP **GET** method
* The request is defined by API call ``indexing.api.indexing.IIndexingService.getPerform``

  
* The request will GET a model :ref:`entity-indexing.api.indexing.Perform`

::

   Provides the perform for id.


URL parameters
-------------------------------------
Each entry matches a **\*** in their respective order.

* The unique identifier **Group.Name** from :ref:`entity-acl.api.group.Group`.
* The unique identifier **Access.Id** from :ref:`entity-acl.api.access.Access`.
* The unique identifier **Property.Name** from :ref:`entity-acl.api.access.Property`.
* The unique identifier **Perform.Id** from :ref:`entity-indexing.api.indexing.Perform`.


Query parameters
-------------------------------------
There are no query parameters available for this request except for global :ref:`headers_parameters`.
