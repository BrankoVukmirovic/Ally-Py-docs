.. _reuqest-GET-ACL/Group/*/Access/*/Property/*/Filter:

**ACL/Group/*/Access/*/Property/*/Filter**
==========================================================

* Use the HTTP **GET** method
* The request is defined by API call ``acl.api.group.IGroupService.getPropertyFilters``

* The request will GET a collection of references to models :ref:`entity-acl.api.filter.Filter`

::

   Provides the filters for the ACL object identifier with access and property name.
   
   @param identifier: object
       The ACL object identifier.
   @param accessId: integer
       The access id.
   @param propertyName: string
       The property name.
   @param options: key arguments
       The result iteration options.
   @return: Iterable(Filter.Name)
       An iterator containing the filters.


URL parameters
-------------------------------------
Each entry matches a **\*** in their respective order.

* The unique identifier **Group.Name** from :ref:`entity-acl.api.group.Group`.
* The unique identifier **Access.Id** from :ref:`entity-acl.api.access.Access`.
* The unique identifier **Property.Name** from :ref:`entity-acl.api.access.Property`.


Query parameters
-------------------------------------
There are no query parameters available for this request except for global :ref:`headers_parameters`.
