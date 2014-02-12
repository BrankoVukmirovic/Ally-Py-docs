.. _reuqest-PUT-GUI/Action/*:

**GUI/Action/***
==========================================================

* Use the HTTP **PUT** method in order to update the model :ref:`entity-gui.action.api.action.Action`
* The request is defined by API call ``gui.action.api.action.IActionManagerService.update``
* The updated model is identified by:

 * The model :ref:`entity-gui.action.api.action.Action` uniquelly identified by **Action.Path**.

::

   Update the entity.
   
   @param entity: Entity
       The entity to be updated.

Content properties
-------------------------------------
This are the available model properties.

+----------+-----------+--------------------------------------------+
| Property |  Accepts  |                 Description                |
+==========+===========+============================================+
| Label    | * **str** |                                            |
|          |           | Maximum text size is *255* characters long |
+----------+-----------+--------------------------------------------+
| NavBar   | * **str** |                                            |
|          |           | Maximum text size is *255* characters long |
+----------+-----------+--------------------------------------------+
| Script   | * **str** |                                            |
|          |           | Maximum text size is *255* characters long |
+----------+-----------+--------------------------------------------+



Response
-------------------------------------
Provides a 200 successful updated code in case the model entity has been successfully inserted, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html#sec9.6 in case
of update problems a 400 code is provided with explanations about the problem.