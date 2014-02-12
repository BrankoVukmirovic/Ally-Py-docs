.. _reuqest-POST-Security/Authentication:

**Security/Authentication**
==========================================================

* Use the HTTP **POST** method in order to insert the model :ref:`entity-superdesk.security.api.authentication.Token`
* The request is defined by API call ``superdesk.security.api.authentication.IAuthenticationService.requestLogin``

::

   Create a token in order to authenticate.

Content properties
-------------------------------------
There are no model properties required for this request.


Response
-------------------------------------
Provides a 201 successful created code in case the model entity has been successfully inserted, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html#sec9.5 in case
of creation problems a 400 code is provided with explanations about the problem.