.. _reuqest-PUT-Security/Right/*/Access/*/Filter/*/Property/*:

**Security/Right/*/Access/*/Filter/*/Property/***
==========================================================

* Use the HTTP **PUT** method in order to update the model :ref:`entity-acl.api.access.Property`
* The request is defined by API call ``security.api.right.IRightService.addPropertyFilter``
* The updated model is identified by:

 * The model :ref:`entity-security.api.right.Right` uniquelly identified by **Right.Id**.
 * The model :ref:`entity-acl.api.access.Access` uniquelly identified by **Access.Id**.
 * The model :ref:`entity-acl.api.filter.Filter` uniquelly identified by **Filter.Name**.
 * The model :ref:`entity-acl.api.access.Property` uniquelly identified by **Property.Name**.

::

   Adds a filter to a ACL object access property.
   
   @param identifier: object
       The ACL object identifier.
   @param accessId: integer
       The access id.
   @param propertyName: string
       The property name.
   @param filterName: string
       The filter name.

Content properties
-------------------------------------
This are the available model properties.

+-----------+-----------+-------------+
|  Property |  Accepts  | Description |
+===========+===========+=============+
| Signature | * **str** |             |
+-----------+-----------+-------------+



Response
-------------------------------------
Provides a 200 successful updated code in case the model entity has been successfully inserted, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html#sec9.6 in case
of update problems a 400 code is provided with explanations about the problem.