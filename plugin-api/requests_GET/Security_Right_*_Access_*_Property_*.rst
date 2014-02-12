.. _reuqest-GET-Security/Right/*/Access/*/Property/*:

**Security/Right/*/Access/*/Property/***
==========================================================

* Use the HTTP **GET** method
* The request is defined by API call ``acl.api.access.IAccessService.getProperty``

  
* The request will GET a model :ref:`entity-acl.api.access.Property`

::

   Provides the input property with the provided name and access.


URL parameters
-------------------------------------
Each entry matches a **\*** in their respective order.

* The unique identifier **Right.Id** from :ref:`entity-security.api.right.Right`.
* The unique identifier **Access.Id** from :ref:`entity-acl.api.access.Access`.
* The unique identifier **Property.Name** from :ref:`entity-acl.api.access.Property`.


Query parameters
-------------------------------------
There are no query parameters available for this request except for global :ref:`headers_parameters`.
