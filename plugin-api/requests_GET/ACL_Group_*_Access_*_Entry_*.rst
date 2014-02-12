.. _reuqest-GET-ACL/Group/*/Access/*/Entry/*:

**ACL/Group/*/Access/*/Entry/***
==========================================================

* Use the HTTP **GET** method
* The request is defined by API call ``acl.api.access.IAccessService.getEntry``

  
* The request will GET a model :ref:`entity-acl.api.access.Entry`

::

   Provides the path dynamic entry for access and position.


URL parameters
-------------------------------------
Each entry matches a **\*** in their respective order.

* The unique identifier **Group.Name** from :ref:`entity-acl.api.group.Group`.
* The unique identifier **Access.Id** from :ref:`entity-acl.api.access.Access`.
* The unique identifier **Entry.Position** from :ref:`entity-acl.api.access.Entry`.


Query parameters
-------------------------------------
There are no query parameters available for this request except for global :ref:`headers_parameters`.
