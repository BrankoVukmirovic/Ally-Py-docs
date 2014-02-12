.. _reuqest-PUT-HR/UserType/*:

**HR/UserType/***
==========================================================

* Use the HTTP **PUT** method in order to update the model :ref:`entity-superdesk.user.api.user_type.UserType`
* The request is defined by API call ``superdesk.user.api.user_type.IUserTypeService.update``
* The updated model is identified by:

 * The model :ref:`entity-superdesk.user.api.user_type.UserType` uniquelly identified by **UserType.Key**.

::

   Update the entity.
   
   @param entity: Entity
       The entity to be updated.

Content properties
-------------------------------------
There are no model properties required for this request.


Response
-------------------------------------
Provides a 200 successful updated code in case the model entity has been successfully inserted, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html#sec9.6 in case
of update problems a 400 code is provided with explanations about the problem.