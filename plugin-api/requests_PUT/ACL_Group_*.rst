.. _reuqest-PUT-ACL/Group/*:

**ACL/Group/***
==========================================================

* Use the HTTP **PUT** method in order to update the model :ref:`entity-acl.api.group.Group`
* The request is defined by API call ``acl.api.group.IGroupService.update``
* The updated model is identified by:

 * The model :ref:`entity-acl.api.group.Group` uniquelly identified by **Group.Name**.

::

   Update the entity.
   
   @param entity: Entity
       The entity to be updated.

Content properties
-------------------------------------
This are the available model properties.

+-------------+------------+--------------------------------------------+
|   Property  |   Accepts  |                 Description                |
+=============+============+============================================+
| Description | * **str**  |                                            |
|             |            | Maximum text size is *255* characters long |
+-------------+------------+--------------------------------------------+
| IsAnonymous | * **bool** |                                            |
+-------------+------------+--------------------------------------------+



Response
-------------------------------------
Provides a 200 successful updated code in case the model entity has been successfully inserted, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html#sec9.6 in case
of update problems a 400 code is provided with explanations about the problem.