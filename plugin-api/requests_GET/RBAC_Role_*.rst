.. _reuqest-GET-RBAC/Role/*:

**RBAC/Role/***
==========================================================

* Use the HTTP **GET** method
* The request is defined by API call ``security.rbac.api.role_rbac.IRoleRbacService.getById``

  
* The request will GET a model :ref:`entity-security.rbac.api.role.Role`

::

   Provides the entity based on the identifier.
   
   @param identifier: object
       The id of the entity to find.


URL parameters
-------------------------------------
Each entry matches a **\*** in their respective order.

* The unique identifier **Role.Name** from :ref:`entity-security.rbac.api.role.Role`.


Query parameters
-------------------------------------
There are no query parameters available for this request except for global :ref:`headers_parameters`.
