.. _reuqest-UNLINK-ACL/Group/*/Action/*:

**ACL/Group/*/Action/***
==========================================================

* Use the HTTP **DELETE** method in order to unlink
* The request is defined by API call ``gui.action.api.category_group.IActionGroupService.remAction``
* The request will link, each entry matches a **\*** in their respective order:

 * The model :ref:`entity-acl.api.group.Group` uniquelly identified by **Group.Name**.
 * The model :ref:`entity-gui.action.api.action.Action` uniquelly identified by **Action.Path**.


::

   Removes the action for the action category object identifier.
   
   @param identifier: object
       The action category object identifier.
   @param actionPath: string
       The action path to be removed.
   @return: boolean
       True if an action has been successfully removed, False otherwise. 


Response
-------------------------------------
Provides a 204 delete successful code in case the model entities have been successfully unlinked, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html#sec9.7 in case
the provided model identifiers are invalid or not linked it will return a 400 cannot find code.