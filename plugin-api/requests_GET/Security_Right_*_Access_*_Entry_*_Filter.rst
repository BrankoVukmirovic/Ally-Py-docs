.. _reuqest-GET-Security/Right/*/Access/*/Entry/*/Filter:

**Security/Right/*/Access/*/Entry/*/Filter**
==========================================================

* Use the HTTP **GET** method
* The request is defined by API call ``security.api.right.IRightService.getEntryFilters``

* The request will GET a collection of references to models :ref:`entity-acl.api.filter.Filter`

::

   Provides the filters for the ACL object identifier with access and entry position.
   
   @param identifier: object
       The ACL object identifier.
   @param accessId: integer
       The access id.
   @param entryPosition: integer
       The entry position.
   @param options: key arguments
       The result iteration options.
   @return: Iterable(Filter.Name)
       An iterator containing the filters.


URL parameters
-------------------------------------
Each entry matches a **\*** in their respective order.

* The unique identifier **Right.Id** from :ref:`entity-security.api.right.Right`.
* The unique identifier **Access.Id** from :ref:`entity-acl.api.access.Access`.
* The unique identifier **Entry.Position** from :ref:`entity-acl.api.access.Entry`.


Query parameters
-------------------------------------
There are no query parameters available for this request except for global :ref:`headers_parameters`.
