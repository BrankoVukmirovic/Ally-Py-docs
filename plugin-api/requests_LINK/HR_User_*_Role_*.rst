.. _reuqest-LINK-HR/User/*/Role/*:

**HR/User/*/Role/***
==========================================================

* Use the HTTP **PUT** method with no content body in order to link
* The request is defined by API call ``superdesk.security.api.user_rbac.IUserRbacService.addRole``
* The request will link, each entry matches a **\*** in their respective order:

 * The model :ref:`entity-superdesk.user.api.user.User` uniquelly identified by **User.Id**.
 * The model :ref:`entity-security.rbac.api.role.Role` uniquelly identified by **Role.Name**.


::

   Add to the RBAC object with identifier the role.
   
   @param identifier: object
       The RBAC object identifier to add the role to.
   @param roleName: string
       The role name to assign to identifier.
   @return: boolean
       True if the role has been added, False otherwise.


Response
-------------------------------------
Provides a 200 successful code in case the model entities have been successfully linked, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html#sec9.7 in case
the provided model identifiers are invalid it will return a 400 cannot find code.