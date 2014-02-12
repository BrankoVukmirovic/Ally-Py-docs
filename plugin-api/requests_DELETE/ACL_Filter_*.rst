.. _reuqest-DELETE-ACL/Filter/*:

**ACL/Filter/***
==========================================================

* Use the HTTP **DELETE** method in order to remove models
* The request is defined by API call ``acl.api.filter.IFilterService.delete``
* Delete the entity :ref:`entity-acl.api.filter.Filter` based on **Filter.Name**.


::

   Delete the filter for the provided name.
   
   @param name: string
       The name of the filter to be deleted.
   @return: boolean
       True if the delete is successful, false otherwise.


Response
-------------------------------------
Provides a 204 delete successful code if the model associated with the identifier has been removed, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html#sec9.6 in case
of problems it will return a 400 cannot delete code.