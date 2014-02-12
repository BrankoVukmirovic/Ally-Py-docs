.. _reuqest-GET-ACL/Filter/*:

**ACL/Filter/***
==========================================================

* Use the HTTP **GET** method
* The request is defined by API call ``acl.api.filter.IFilterService.getById``

  
* The request will GET a model :ref:`entity-acl.api.filter.Filter`

::

   Provides the entity based on the identifier.
   
   @param identifier: object
       The id of the entity to find.


URL parameters
-------------------------------------
Each entry matches a **\*** in their respective order.

* The unique identifier **Filter.Name** from :ref:`entity-acl.api.filter.Filter`.


Query parameters
-------------------------------------
There are no query parameters available for this request except for global :ref:`headers_parameters`.
