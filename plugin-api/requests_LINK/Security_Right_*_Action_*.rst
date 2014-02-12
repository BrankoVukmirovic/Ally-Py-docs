.. _reuqest-LINK-Security/Right/*/Action/*:

**Security/Right/*/Action/***
==========================================================

* Use the HTTP **PUT** method with no content body in order to link
* The request is defined by API call ``gui.action.api.category_right.IActionRightService.addAction``
* The request will link, each entry matches a **\*** in their respective order:

 * The model :ref:`entity-security.api.right.Right` uniquelly identified by **Right.Id**.
 * The model :ref:`entity-gui.action.api.action.Action` uniquelly identified by **Action.Path**.


::

   Adds a new action for the action category object identifier.
   
   @param identifier: object
       The action category object identifier.
   @param actionPath: string
       The action path to be added.


Response
-------------------------------------
Provides a 200 successful code in case the model entities have been successfully linked, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html#sec9.7 in case
the provided model identifiers are invalid it will return a 400 cannot find code.