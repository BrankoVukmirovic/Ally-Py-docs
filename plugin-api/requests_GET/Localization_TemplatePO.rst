.. _reuqest-GET-Localization/TemplatePO:

**Localization/TemplatePO**
==========================================================

* Use the HTTP **GET** method
* The request is defined by API call ``internationalization.api.po_file.IInternationlizationFileService.getPOTFile``

  
* The request will GET a ``Reference`` property o model :ref:`entity-internationalization.api.po_file.PO`

::

   Provides the POT file for the specified plugin. If name is None the global POT file will be provided.
   
   @param name: string
       The name of the plugin
   @return: Reference
       The reference to the content of the POT file.




Query parameters
-------------------------------------
There are no query parameters available for this request except for global :ref:`headers_parameters`.
