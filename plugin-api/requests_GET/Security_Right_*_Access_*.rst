.. _reuqest-GET-Security/Right/*/Access/*:

**Security/Right/*/Access/***
==========================================================

* Use the HTTP **GET** method
* The request is defined by API call ``acl.api.access.IAccessService.getById``

  
* The request will GET a model :ref:`entity-acl.api.access.Access`

::

   Provides the entity based on the identifier.
   
   @param identifier: object
       The id of the entity to find.


URL parameters
-------------------------------------
Each entry matches a **\*** in their respective order.

* The unique identifier **Right.Id** from :ref:`entity-security.api.right.Right`.
* The unique identifier **Access.Id** from :ref:`entity-acl.api.access.Access`.


Query parameters
-------------------------------------
There are no query parameters available for this request except for global :ref:`headers_parameters`.
