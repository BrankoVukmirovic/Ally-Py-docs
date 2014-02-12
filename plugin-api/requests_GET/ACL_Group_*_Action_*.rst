.. _reuqest-GET-ACL/Group/*/Action/*:

**ACL/Group/*/Action/***
==========================================================

* Use the HTTP **GET** method
* The request is defined by API call ``gui.action.api.action.IActionManagerService.getById``

  
* The request will GET a model :ref:`entity-gui.action.api.action.Action`

::

   Provides the entity based on the identifier.
   
   @param identifier: object
       The id of the entity to find.


URL parameters
-------------------------------------
Each entry matches a **\*** in their respective order.

* The unique identifier **Group.Name** from :ref:`entity-acl.api.group.Group`.
* The unique identifier **Action.Path** from :ref:`entity-gui.action.api.action.Action`.


Query parameters
-------------------------------------
There are no query parameters available for this request except for global :ref:`headers_parameters`.
