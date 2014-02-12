.. _reuqest-UNLINK-HR/User/*/Right/*:

**HR/User/*/Right/***
==========================================================

* Use the HTTP **DELETE** method in order to unlink
* The request is defined by API call ``superdesk.security.api.user_rbac.IUserRbacService.remRight``
* The request will link, each entry matches a **\*** in their respective order:

 * The model :ref:`entity-superdesk.user.api.user.User` uniquelly identified by **User.Id**.
 * The model :ref:`entity-security.api.right.Right` uniquelly identified by **Right.Id**.


::

   Remove from the RBAC object with identifier the right.
   
   @param identifier: object
       The RBAC object identifier to add remove the right from.
   @param rightId: integer
       The right id to remove.
   @return: boolean
       True if a right has been removed, False otherwise.


Response
-------------------------------------
Provides a 204 delete successful code in case the model entities have been successfully unlinked, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html#sec9.7 in case
the provided model identifiers are invalid or not linked it will return a 400 cannot find code.