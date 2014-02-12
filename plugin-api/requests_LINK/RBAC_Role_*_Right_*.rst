.. _reuqest-LINK-RBAC/Role/*/Right/*:

**RBAC/Role/*/Right/***
==========================================================

* Use the HTTP **PUT** method with no content body in order to link
* The request is defined by API call ``security.rbac.api.role_rbac.IRoleRbacService.addRight``
* The request will link, each entry matches a **\*** in their respective order:

 * The model :ref:`entity-security.rbac.api.role.Role` uniquelly identified by **Role.Name**.
 * The model :ref:`entity-security.api.right.Right` uniquelly identified by **Right.Id**.


::

   Add to the RBAC object with identifier the right.
   
   @param identifier: object
       The RBAC object identifier to add the right to.
   @param rightId: integer
       The right id to assign to identifier.


Response
-------------------------------------
Provides a 200 successful code in case the model entities have been successfully linked, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html#sec9.7 in case
the provided model identifiers are invalid it will return a 400 cannot find code.