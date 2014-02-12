.. _reuqest-DELETE-RBAC/Role/*:

**RBAC/Role/***
==========================================================

* Use the HTTP **DELETE** method in order to remove models
* The request is defined by API call ``security.rbac.api.role_rbac.IRoleRbacService.delete``
* Delete the entity :ref:`entity-security.rbac.api.role.Role` based on **Role.Name**.


::

   Delete the entity for the provided identifier.
   
   @param identifier: object
       The identifier of the entity to be deleted.
   @return: boolean
       True if the delete is successful, false otherwise.


Response
-------------------------------------
Provides a 204 delete successful code if the model associated with the identifier has been removed, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html#sec9.6 in case
of problems it will return a 400 cannot delete code.