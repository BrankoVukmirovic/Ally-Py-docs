.. _reuqest-GET-Security/Login/*/Gateway:

**Security/Login/*/Gateway**
==========================================================

* Use the HTTP **GET** method
* The request is defined by API call ``superdesk.security.api.authentication.IAuthenticationService.getGateways``

* The request will GET a collection of models :ref:`entity-gateway.api.gateway.Gateway`

::

   Provides the authenticated gateways for the provided session, if the session is invalid an error is raised.


URL parameters
-------------------------------------
Each entry matches a **\*** in their respective order.

* The unique identifier **Login.Session** from :ref:`entity-superdesk.security.api.authentication.Login`.


Query parameters
-------------------------------------
There are no query parameters available for this request except for global :ref:`headers_parameters`.
