.. _reuqest-POST-Security/Login:

**Security/Login**
==========================================================

* Use the HTTP **POST** method in order to insert the model :ref:`entity-superdesk.security.api.authentication.Login`
* The request is defined by API call ``superdesk.security.api.authentication.IAuthenticationService.performLogin``

::

   Called in order to authenticate

Content properties
-------------------------------------
This are the available model properties.

+-------------+-----------+-------------------------+
|   Property  |  Accepts  |       Description       |
+=============+===========+=========================+
| Token       | * **str** |                         |
|             |           | Represents the model id |
+-------------+-----------+-------------------------+
| HashedToken | * **str** |                         |
+-------------+-----------+-------------------------+
| UserName    | * **str** |                         |
+-------------+-----------+-------------------------+



Response
-------------------------------------
Provides a 201 successful created code in case the model entity has been successfully inserted, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html#sec9.5 in case
of creation problems a 400 code is provided with explanations about the problem.