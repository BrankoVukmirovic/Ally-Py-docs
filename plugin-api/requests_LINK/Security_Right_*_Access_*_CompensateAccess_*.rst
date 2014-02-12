.. _reuqest-LINK-Security/Right/*/Access/*/CompensateAccess/*:

**Security/Right/*/Access/*/CompensateAccess/***
==========================================================

* Use the HTTP **PUT** method with no content body in order to link
* The request is defined by API call ``security.api.right.IRightService.addCompensate``
* The request will link, each entry matches a **\*** in their respective order:

 * The model :ref:`entity-security.api.right.Right` uniquelly identified by **Right.Id**.
 * The model :ref:`entity-acl.api.access.Access` uniquelly identified by **Access.Id**.
 * The model :ref:`entity-acl.api.access.Access` uniquelly identified by **Access.Id**.


::

   Adds the compensated access for the provided access id.
   
   @param identifier: object
       The ACL object identifier.
   @param accessId: integer
       The access id that compensates.
   @param compensatedId: integer
       The access id that is compensated.


Response
-------------------------------------
Provides a 200 successful code in case the model entities have been successfully linked, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html#sec9.7 in case
the provided model identifiers are invalid it will return a 400 cannot find code.