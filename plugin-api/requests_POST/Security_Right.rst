.. _reuqest-POST-Security/Right:

**Security/Right**
==========================================================

* Use the HTTP **POST** method in order to insert the model :ref:`entity-security.api.right.Right`
* The request is defined by API call ``security.api.right.IRightService.insert``

::

   Insert the entity.
   
   @param entity: Entity
       The entity to be inserted.
   @return: object
       The identifier of the entity

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
Provides a 201 successful created code in case the model entity has been successfully inserted, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html#sec9.5 in case
of creation problems a 400 code is provided with explanations about the problem.