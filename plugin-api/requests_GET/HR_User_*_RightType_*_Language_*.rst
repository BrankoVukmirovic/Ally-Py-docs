.. _reuqest-GET-HR/User/*/RightType/*/Language/*:

**HR/User/*/RightType/*/Language/***
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

* The unique identifier **User.Id** from :ref:`entity-superdesk.user.api.user.User`.
* The unique identifier **RightType.Name** from :ref:`entity-security.api.right_type.RightType`.
* The unique identifier **Language.Code** from :ref:`entity-internationalization.language.api.language.Language`.


Query parameters
-------------------------------------
There are no query parameters available for this request except for global :ref:`headers_parameters`.
