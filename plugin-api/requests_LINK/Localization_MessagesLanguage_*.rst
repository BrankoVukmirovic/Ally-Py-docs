.. _reuqest-LINK-Localization/MessagesLanguage/*:

**Localization/MessagesLanguage/***
==========================================================

* Use the HTTP **PUT** method with no content body in order to link
* The request is defined by API call ``internationalization.api.po_file.IInternationlizationFileService.updatePOFile``
* The request will link, each entry matches a **\*** in their respective order:

 * The model :ref:`entity-internationalization.language.api.language.Language` uniquelly identified by **Language.Code**.


::

   Update a PO file for specified locale or upload new locale if doesn't exist. If name is None, file will be uploaded a global PO file.
   
   @param locale: Language.Code
       The locale for which to return the translation.
   @param name: string
       The name of the plugin


Response
-------------------------------------
Provides a 200 successful code in case the model entities have been successfully linked, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html#sec9.7 in case
the provided model identifiers are invalid it will return a 400 cannot find code.