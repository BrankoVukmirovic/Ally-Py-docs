.. _reuqest-POST-HR/Person:

**HR/Person**
==========================================================

* Use the HTTP **POST** method in order to insert the model :ref:`entity-superdesk.person.api.person.Person`
* The request is defined by API call ``superdesk.person.api.person.IPersonService.insert``

::

   Insert the entity.
   
   @param entity: Entity
       The entity to be inserted.
   @return: object
       The identifier of the entity

Content properties
-------------------------------------
This are the available model properties.

+-------------+-----------+--------------------------------------------+
|   Property  |  Accepts  |                 Description                |
+=============+===========+============================================+
| Address     | * **str** |                                            |
|             |           | Maximum text size is *255* characters long |
+-------------+-----------+--------------------------------------------+
| EMail       | * **str** |                                            |
|             |           | Maximum text size is *255* characters long |
+-------------+-----------+--------------------------------------------+
| FirstName   | * **str** |                                            |
|             |           | Maximum text size is *255* characters long |
+-------------+-----------+--------------------------------------------+
| LastName    | * **str** |                                            |
|             |           | Maximum text size is *255* characters long |
+-------------+-----------+--------------------------------------------+
| PhoneNumber | * **str** |                                            |
|             |           | Maximum text size is *255* characters long |
+-------------+-----------+--------------------------------------------+



Response
-------------------------------------
Provides a 201 successful created code in case the model entity has been successfully inserted, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html#sec9.5 in case
of creation problems a 400 code is provided with explanations about the problem.