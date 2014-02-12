.. _reuqest-GET-ACL/Group/*/Access/*/Compensate:

**ACL/Group/*/Access/*/Compensate**
==========================================================

* Use the HTTP **GET** method
* The request is defined by API call ``acl.api.group.IGroupService.getCompensates``

* The request will GET a collection of models :ref:`entity-acl.api.compensate.Compensate`

::

   Provides the compensated accesses for the provided access id.
   
   @param identifier: object
       The ACL object identifier.
   @param accessId: integer
       The access id that compensates.
    @return: Iterable(Compensate)
       An iterator containing the compensated accesses.


URL parameters
-------------------------------------
Each entry matches a **\*** in their respective order.

* The unique identifier **Group.Name** from :ref:`entity-acl.api.group.Group`.
* The unique identifier **Access.Id** from :ref:`entity-acl.api.access.Access`.


Query parameters
-------------------------------------
There are no query parameters available for this request except for global :ref:`headers_parameters`.
