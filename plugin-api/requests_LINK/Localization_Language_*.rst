.. _reuqest-LINK-Localization/Language/*:

**Localization/Language/***
==========================================================

* Use the HTTP **PUT** method with no content body in order to link
* The request is defined by API call ``internationalization.language.api.language.ILanguageService.add``
* The request will link, each entry matches a **\*** in their respective order:

 * The model :ref:`entity-internationalization.language.api.language.Language` uniquelly identified by **Language.Code**.


::

   Add the provided language code as a system available language.
   This makes the language available also for other resources.


Response
-------------------------------------
Provides a 200 successful code in case the model entities have been successfully linked, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html#sec9.7 in case
the provided model identifiers are invalid it will return a 400 cannot find code.