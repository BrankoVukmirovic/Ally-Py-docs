.. _reuqest-LINK-Localization/TemplatePO/*:

**Localization/TemplatePO/***
==========================================================

* Use the HTTP **PUT** method with no content body in order to link
* The request is defined by API call ``internationalization.api.po_file.IInternationlizationFileService.updatePOTFile``
* The request will link, each entry matches a **\*** in their respective order:

 * The model :ref:`entity-internationalization.api.po_file.PO` uniquelly identified by **PO.Name**.


::

   Insert a POT file for the specified plugin, overwrite if exists.
   
   @param name: string
       The name of the plugin
   @param content: Content
       The content of POT file
   @return name: string
       The name of inserted POT


Response
-------------------------------------
Provides a 200 successful code in case the model entities have been successfully linked, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html#sec9.7 in case
the provided model identifiers are invalid it will return a 400 cannot find code.