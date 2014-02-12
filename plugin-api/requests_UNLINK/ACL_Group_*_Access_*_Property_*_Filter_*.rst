.. _reuqest-UNLINK-ACL/Group/*/Access/*/Property/*/Filter/*:

**ACL/Group/*/Access/*/Property/*/Filter/***
==========================================================

* Use the HTTP **DELETE** method in order to unlink
* The request is defined by API call ``acl.api.group.IGroupService.remPropertyFilter``
* The request will link, each entry matches a **\*** in their respective order:

 * The model :ref:`entity-acl.api.group.Group` uniquelly identified by **Group.Name**.
 * The model :ref:`entity-acl.api.access.Access` uniquelly identified by **Access.Id**.
 * The model :ref:`entity-acl.api.access.Property` uniquelly identified by **Property.Name**.
 * The model :ref:`entity-acl.api.filter.Filter` uniquelly identified by **Filter.Name**.


::

   Removes an filter from the ACL object access property.
   
   @param identifier: object
       The ACL object identifier.
   @param accessId: integer
       The access id.
   @param entryPosition: integer
       The entry position.
   @param propertyName: string
       The property name.
   @return: boolean
       True if a filter has been successfully removed for property, False otherwise.


Response
-------------------------------------
Provides a 204 delete successful code in case the model entities have been successfully unlinked, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html#sec9.7 in case
the provided model identifiers are invalid or not linked it will return a 400 cannot find code.