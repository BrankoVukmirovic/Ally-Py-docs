.. _reuqest-DELETE-ACL/Access/*:

**ACL/Access/***
==========================================================

* Use the HTTP **DELETE** method in order to remove models
* The request is defined by API call ``acl.api.access.IAccessService.delete``
* Delete the entity :ref:`entity-acl.api.access.Access` based on **Access.Id**.


::

   Delete the access for the provided id.
   
   @param id: integer
       The id of the access to be deleted.
   @return: boolean
       True if the delete is successful, false otherwise.


Response
-------------------------------------
Provides a 204 delete successful code if the model associated with the identifier has been removed, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html#sec9.6 in case
of problems it will return a 400 cannot delete code.