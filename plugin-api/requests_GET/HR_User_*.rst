.. _reuqest-GET-HR/User/*:

**HR/User/***
==========================================================

* Use the HTTP **GET** method
* The request is defined by API call ``superdesk.user.api.user.IUserService.getById``

  
* The request will GET a model :ref:`entity-superdesk.user.api.user.User`

::

   Provides the entity based on the identifier.
   
   @param identifier: object
       The id of the entity to find.


URL parameters
-------------------------------------
Each entry matches a **\*** in their respective order.

* The unique identifier **User.Id** from :ref:`entity-superdesk.user.api.user.User`.


Query parameters
-------------------------------------
There are no query parameters available for this request except for global :ref:`headers_parameters`.
