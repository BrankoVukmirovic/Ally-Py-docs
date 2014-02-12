.. _reuqest-PUT-HR/UserPassword/*:

**HR/UserPassword/***
==========================================================

* Use the HTTP **PUT** method in order to update the model :ref:`entity-superdesk.user.api.user.Password`
* The request is defined by API call ``superdesk.user.api.user.IUserService.changePassword``
* The updated model is identified by:

 * The model :ref:`entity-superdesk.user.api.user.User` uniquelly identified by **User.Id**.

::

   Changes user password

Content properties
-------------------------------------
This are the available model properties.

+-------------+-----------+-------------+
|   Property  |  Accepts  | Description |
+=============+===========+=============+
| NewPassword | * **str** |             |
+-------------+-----------+-------------+
| OldPassword | * **str** |             |
+-------------+-----------+-------------+



Response
-------------------------------------
Provides a 200 successful updated code in case the model entity has been successfully inserted, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html#sec9.6 in case
of update problems a 400 code is provided with explanations about the problem.