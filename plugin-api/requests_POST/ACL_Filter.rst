.. _reuqest-POST-ACL/Filter:

**ACL/Filter**
==========================================================

* Use the HTTP **POST** method in order to insert the model :ref:`entity-acl.api.filter.Filter`
* The request is defined by API call ``acl.api.filter.IFilterService.insert``

::

   Insert the filter.
   
   @param filter: Filter
       The filter to be inserted.
   @return: string
       The name of the filter.

Content properties
-------------------------------------
This are the available model properties.

+-----------+-----------+--------------------------------------------+
|  Property |  Accepts  |                 Description                |
+===========+===========+============================================+
| Name      | * **str** |                                            |
|           |           | Represents the model id                    |
|           |           | Maximum text size is *255* characters long |
+-----------+-----------+--------------------------------------------+
| Path      | * **str** |                                            |
|           |           | Maximum text size is *255* characters long |
+-----------+-----------+--------------------------------------------+
| Signature | * **str** |                                            |
|           |           | Maximum text size is *255* characters long |
+-----------+-----------+--------------------------------------------+



Response
-------------------------------------
Provides a 201 successful created code in case the model entity has been successfully inserted, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html#sec9.5 in case
of creation problems a 400 code is provided with explanations about the problem.