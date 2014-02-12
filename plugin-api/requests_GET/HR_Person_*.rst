.. _reuqest-GET-HR/Person/*:

**HR/Person/***
==========================================================

* Use the HTTP **GET** method
* The request is defined by API call ``superdesk.person.api.person.IPersonService.getById``

  
* The request will GET a model :ref:`entity-superdesk.person.api.person.Person`

::

   Provides the entity based on the identifier.
   
   @param identifier: object
       The id of the entity to find.


URL parameters
-------------------------------------
Each entry matches a **\*** in their respective order.

* The unique identifier **Person.Id** from :ref:`entity-superdesk.person.api.person.Person`.


Query parameters
-------------------------------------
There are no query parameters available for this request except for global :ref:`headers_parameters`.
