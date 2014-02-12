.. _reuqest-DELETE-RBAC/Role/*/SubRole/*:

**RBAC/Role/*/SubRole/***
==========================================================

* Use the HTTP **DELETE** method in order to remove models
* The request is defined by API call ``security.rbac.api.role_rbac.IRoleRbacService.remRole``
* Delete the entity :ref:`entity-security.rbac.api.role.Role` based on **Role.Name**.


::

   Remove from the RBAC object with identifier the role. 
   
   @param identifier: object
       The RBAC object identifier to add remove the role from.
   @param roleName: string
       The role name to remove.
   @return: boolean
       True if a role has been removed, False otherwise.


Response
-------------------------------------
Provides a 204 delete successful code if the model associated with the identifier has been removed, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html#sec9.6 in case
of problems it will return a 400 cannot delete code.