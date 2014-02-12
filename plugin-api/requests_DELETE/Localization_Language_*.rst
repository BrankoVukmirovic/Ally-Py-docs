.. _reuqest-DELETE-Localization/Language/*:

**Localization/Language/***
==========================================================

* Use the HTTP **DELETE** method in order to remove models
* The request is defined by API call ``internationalization.language.api.language.ILanguageService.remove``
* Delete the entity :ref:`entity-internationalization.language.api.language.Language` based on **Language.Code**.


::

   Remove the provided language code from the system.


Response
-------------------------------------
Provides a 204 delete successful code if the model associated with the identifier has been removed, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html#sec9.6 in case
of problems it will return a 400 cannot delete code.