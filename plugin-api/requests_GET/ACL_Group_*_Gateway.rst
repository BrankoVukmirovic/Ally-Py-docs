.. _reuqest-GET-ACL/Group/*/Gateway:

**ACL/Group/*/Gateway**
==========================================================

* Use the HTTP **GET** method
* The request is defined by API call ``acl.api.gateway_acl.IGatewayACLService.getGateways``

* The request will GET a collection of models :ref:`entity-gateway.api.gateway.Gateway`

::

   Get the gateways for the ACL group.


URL parameters
-------------------------------------
Each entry matches a **\*** in their respective order.

* The unique identifier **Group.Name** from :ref:`entity-acl.api.group.Group`.


Query parameters
-------------------------------------
There are no query parameters available for this request except for global :ref:`headers_parameters`.
