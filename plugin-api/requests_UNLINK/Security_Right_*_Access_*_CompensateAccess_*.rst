.. _reuqest-UNLINK-Security/Right/*/Access/*/CompensateAccess/*:

**Security/Right/*/Access/*/CompensateAccess/***
==========================================================

* Use the HTTP **DELETE** method in order to unlink
* The request is defined by API call ``security.api.right.IRightService.remCompensate``
* The request will link, each entry matches a **\*** in their respective order:

 * The model :ref:`entity-security.api.right.Right` uniquelly identified by **Right.Id**.
 * The model :ref:`entity-acl.api.access.Access` uniquelly identified by **Access.Id**.
 * The model :ref:`entity-acl.api.access.Access` uniquelly identified by **Access.Id**.


::

   Removes the compensated access for the provided access id
   
   @param identifier: object
       The ACL object identifier.
   @param accessId: integer
       The access id that compensates.
   @param compensatedId: integer
       The access id that is compensated.
   @return: boolean
       True if any compensated has been removed, False otherwise.


Response
-------------------------------------
Provides a 204 delete successful code in case the model entities have been successfully unlinked, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html#sec9.7 in case
the provided model identifiers are invalid or not linked it will return a 400 cannot find code.