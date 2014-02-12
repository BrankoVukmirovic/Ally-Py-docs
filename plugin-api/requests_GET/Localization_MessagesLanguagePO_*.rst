.. _reuqest-GET-Localization/MessagesLanguagePO/*:

**Localization/MessagesLanguagePO/***
==========================================================

* Use the HTTP **GET** method
* The request is defined by API call ``internationalization.api.po_file.IInternationlizationFileService.getPOFile``

  
* The request will GET a ``Reference`` property o model :ref:`entity-internationalization.api.po_file.PO`

::

   Provides the PO file for the plugin and the given locale. If name is None, global PO file will be provided.
   
   
   @param locale: Language.Code
       The locale for which to return the translation.
   @param name: string
       The name of the plugin
   @return: Reference
       The reference to the content of the PO file.


URL parameters
-------------------------------------
Each entry matches a **\*** in their respective order.

* The unique identifier **Language.Code** from :ref:`entity-internationalization.language.api.language.Language`.


Query parameters
-------------------------------------
There are no query parameters available for this request except for global :ref:`headers_parameters`.
