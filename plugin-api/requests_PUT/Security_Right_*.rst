.. _reuqest-PUT-Security/Right/*:

**Security/Right/***
==========================================================

* Use the HTTP **PUT** method in order to update the model :ref:`entity-security.api.right.Right`
* The request is defined by API call ``security.api.right.IRightService.update``
* The updated model is identified by:

 * The model :ref:`entity-security.api.right.Right` uniquelly identified by **Right.Id**.

::

   Update the entity.
   
   @param entity: Entity
       The entity to be updated.

Content properties
-------------------------------------
This are the available model properties.

+-------------+-----------+----------------------------------------------------------------------+
|   Property  |  Accepts  |                              Description                             |
+=============+===========+======================================================================+
| Description | * **str** |                                                                      |
|             |           | Maximum text size is *255* characters long                           |
+-------------+-----------+----------------------------------------------------------------------+
| Name        | * **str** |                                                                      |
|             |           | Maximum text size is *150* characters long                           |
+-------------+-----------+----------------------------------------------------------------------+
| Type        | * **str** |                                                                      |
|             |           | The provided value needs to be available at '*Security/RightType/**' |
+-------------+-----------+----------------------------------------------------------------------+



Response
-------------------------------------
Provides a 200 successful updated code in case the model entity has been successfully inserted, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html#sec9.6 in case
of update problems a 400 code is provided with explanations about the problem.