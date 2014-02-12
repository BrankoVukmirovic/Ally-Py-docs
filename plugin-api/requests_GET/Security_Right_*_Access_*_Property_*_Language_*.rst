.. _reuqest-GET-Security/Right/*/Access/*/Property/*/Language/*:

**Security/Right/*/Access/*/Property/*/Language/***
==========================================================

* Use the HTTP **GET** method
* The request is defined by API call ``internationalization.language.api.language.ILanguageService.getById``

  
* The request will GET a model :ref:`entity-internationalization.language.api.language.Language`

::

   Provides the entity based on the identifier.
   
   @param identifier: object
       The id of the entity to find.


URL parameters
-------------------------------------
Each entry matches a **\*** in their respective order.

* The unique identifier **Right.Id** from :ref:`entity-security.api.right.Right`.
* The unique identifier **Access.Id** from :ref:`entity-acl.api.access.Access`.
* The unique identifier **Property.Name** from :ref:`entity-acl.api.access.Property`.
* The unique identifier **Language.Code** from :ref:`entity-internationalization.language.api.language.Language`.


Query parameters
-------------------------------------
There are no query parameters available for this request except for global :ref:`headers_parameters`.
