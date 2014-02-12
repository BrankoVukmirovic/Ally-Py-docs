.. _reuqest-POST-ACL/Access:

**ACL/Access**
==========================================================

* Use the HTTP **POST** method in order to insert the model :ref:`entity-acl.api.access.Access`
* The request is defined by API call ``acl.api.access.IAccessService.insert``

::

   Insert the access.
   
   @param access: AccessCreate
       The access to be inserted.
   @return: integer
       The id assigned to the access

Content properties
-------------------------------------
This are the available model properties.

+------------------+----------------------+--------------------------------------------------------------+
|     Property     |        Accepts       |                          Description                         |
+==================+======================+==============================================================+
| Entries          | * **Dict[int: str]** |                                                              |
+------------------+----------------------+--------------------------------------------------------------+
| EntriesShadowed  | * **Dict[int: int]** |                                                              |
+------------------+----------------------+--------------------------------------------------------------+
| EntriesShadowing | * **Dict[int: int]** |                                                              |
+------------------+----------------------+--------------------------------------------------------------+
| Hash             | * **str**            |                                                              |
|                  |                      | Maximum text size is *50* characters long                    |
+------------------+----------------------+--------------------------------------------------------------+
| Method           | * **str**            |                                                              |
|                  |                      | Maximum text size is *20* characters long                    |
+------------------+----------------------+--------------------------------------------------------------+
| Output           | * **str**            |                                                              |
|                  |                      | Maximum text size is *255* characters long                   |
+------------------+----------------------+--------------------------------------------------------------+
| Path             | * **str**            |                                                              |
|                  |                      | Maximum text size is *255* characters long                   |
+------------------+----------------------+--------------------------------------------------------------+
| Priority         | * **int**            |                                                              |
+------------------+----------------------+--------------------------------------------------------------+
| Properties       | * **Dict[str: str]** |                                                              |
+------------------+----------------------+--------------------------------------------------------------+
| Shadowed         | * **int**            |                                                              |
|                  |                      | The provided value needs to be available at '*ACL/Access/**' |
+------------------+----------------------+--------------------------------------------------------------+
| Shadowing        | * **int**            |                                                              |
|                  |                      | The provided value needs to be available at '*ACL/Access/**' |
+------------------+----------------------+--------------------------------------------------------------+



Response
-------------------------------------
Provides a 201 successful created code in case the model entity has been successfully inserted, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html#sec9.5 in case
of creation problems a 400 code is provided with explanations about the problem.