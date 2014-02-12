.. _reuqest-PUT-HR/Person/*:

**HR/Person/***
==========================================================

* Use the HTTP **PUT** method in order to update the model :ref:`entity-superdesk.person.api.person.Person`
* The request is defined by API call ``superdesk.person.api.person.IPersonService.update``
* The updated model is identified by:

 * The model :ref:`entity-superdesk.person.api.person.Person` uniquelly identified by **Person.Id**.

::

   Update the entity.
   
   @param entity: Entity
       The entity to be updated.

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
| FullName    | * **str** |                                            |
+-------------+-----------+--------------------------------------------+
| LastName    | * **str** |                                            |
|             |           | Maximum text size is *255* characters long |
+-------------+-----------+--------------------------------------------+
| PhoneNumber | * **str** |                                            |
|             |           | Maximum text size is *255* characters long |
+-------------+-----------+--------------------------------------------+



Response
-------------------------------------
Provides a 200 successful updated code in case the model entity has been successfully inserted, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html#sec9.6 in case
of update problems a 400 code is provided with explanations about the problem.