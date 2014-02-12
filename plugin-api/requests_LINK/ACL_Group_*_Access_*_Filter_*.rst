.. _reuqest-LINK-ACL/Group/*/Access/*/Filter/*:

**ACL/Group/*/Access/*/Filter/***
==========================================================

* Use the HTTP **PUT** method with no content body in order to link
* The request is defined by API call ``acl.api.group.IGroupService.registerFilter``
* The request will link, each entry matches a **\*** in their respective order:

 * The model :ref:`entity-acl.api.group.Group` uniquelly identified by **Group.Name**.
 * The model :ref:`entity-acl.api.access.Access` uniquelly identified by **Access.Id**.
 * The model :ref:`entity-acl.api.filter.Filter` uniquelly identified by **Filter.Name**.


::

   Register a new filter for access, the place is used only when the filter matches multiple entries in the access
   path, the location of the filter will be marked '@'. The register will also propagate to the shadow, shadowing and 
   shadowed accesses.
   
   @param identifier: object
       The ACL object identifier.
   @param accessId: integer
       The access id.
   @param filterName: string
       The filter name.
   @param place: string
       The filter place.
   @return: boolean
       True if a filter has been successfully registered, False otherwise.


Response
-------------------------------------
Provides a 200 successful code in case the model entities have been successfully linked, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html#sec9.7 in case
the provided model identifiers are invalid it will return a 400 cannot find code.