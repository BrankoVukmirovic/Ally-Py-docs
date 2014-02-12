.. _reuqest-PUT-HR/User/*:

**HR/User/***
==========================================================

* Use the HTTP **PUT** method in order to update the model :ref:`entity-superdesk.user.api.user.User`
* The request is defined by API call ``superdesk.user.api.user.IUserService.update``
* The updated model is identified by:

 * The model :ref:`entity-superdesk.user.api.user.User` uniquelly identified by **User.Id**.

::

   Update the entity.
   
   @param entity: Entity
       The entity to be updated.

Content properties
-------------------------------------
This are the available model properties.

+-------------+----------------+---------------------------------------------------------------+
|   Property  |     Accepts    |                          Description                          |
+=============+================+===============================================================+
| Active      | * **bool**     |                                                               |
+-------------+----------------+---------------------------------------------------------------+
| Address     | * **str**      |                                                               |
|             |                | Maximum text size is *255* characters long                    |
+-------------+----------------+---------------------------------------------------------------+
| CreatedOn   | * **datetime** |                                                               |
|             |                | Example *1982-01-18T02:40:12Z*                                |
+-------------+----------------+---------------------------------------------------------------+
| EMail       | * **str**      |                                                               |
|             |                | Maximum text size is *255* characters long                    |
+-------------+----------------+---------------------------------------------------------------+
| FirstName   | * **str**      |                                                               |
|             |                | Maximum text size is *255* characters long                    |
+-------------+----------------+---------------------------------------------------------------+
| FullName    | * **str**      |                                                               |
+-------------+----------------+---------------------------------------------------------------+
| LastName    | * **str**      |                                                               |
|             |                | Maximum text size is *255* characters long                    |
+-------------+----------------+---------------------------------------------------------------+
| Name        | * **str**      |                                                               |
|             |                | Maximum text size is *150* characters long                    |
+-------------+----------------+---------------------------------------------------------------+
| Password    | * **str**      |                                                               |
+-------------+----------------+---------------------------------------------------------------+
| PhoneNumber | * **str**      |                                                               |
|             |                | Maximum text size is *255* characters long                    |
+-------------+----------------+---------------------------------------------------------------+
| Type        | * **str**      |                                                               |
|             |                | The provided value needs to be available at '*HR/UserType/**' |
+-------------+----------------+---------------------------------------------------------------+



Response
-------------------------------------
Provides a 200 successful updated code in case the model entity has been successfully inserted, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html#sec9.6 in case
of update problems a 400 code is provided with explanations about the problem.