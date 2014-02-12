.. _reuqest-LINK-HR/User/*/Right/*:

**HR/User/*/Right/***
==========================================================

* Use the HTTP **PUT** method with no content body in order to link
* The request is defined by API call ``superdesk.security.api.user_rbac.IUserRbacService.addRight``
* The request will link, each entry matches a **\*** in their respective order:

 * The model :ref:`entity-superdesk.user.api.user.User` uniquelly identified by **User.Id**.
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