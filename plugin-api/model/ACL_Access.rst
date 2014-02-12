.. _model-ACL/Access:

**ACL/Access**
==========================================================

The model is defined by the following API model classes.

.. _entity-acl.api.access.Access:

``acl.api.access.Access``
-------------------------------------------------------------------
::

   The access model contains data that relates to an available REST resource URI that access can be granted based on.
   
   :Attribute Id: The unique identifier of the access.
   :Attribute Path: Contains the path that the access maps to. The path contains beside the fixed string names 
                    also markers '*' for where dynamic path elements are expected.
   :Attribute Method: The HTTP method name that this access maps to.
   :Attribute Shadowing: The access that this access is actually shadowing, this means that the access path is just a reroute
                         for the shadowing access.



+-----------+-------------------------+----------------------------+
|  Property |           Type          |         Description        |
+===========+=========================+============================+
| Id        | int                     | Is model unique identifier |
+-----------+-------------------------+----------------------------+
| Hash      | str                     |                            |
+-----------+-------------------------+----------------------------+
| Method    | str                     |                            |
+-----------+-------------------------+----------------------------+
| Output    | str                     |                            |
+-----------+-------------------------+----------------------------+
| Path      | str                     |                            |
+-----------+-------------------------+----------------------------+
| Priority  | int                     |                            |
+-----------+-------------------------+----------------------------+
| Shadowed  | :ref:`model-ACL/Access` |                            |
+-----------+-------------------------+----------------------------+
| Shadowing | :ref:`model-ACL/Access` |                            |
+-----------+-------------------------+----------------------------+





**Model paths**
-------------------------------------------------
* **Can be obtained (GET) using**

  * :ref:`reuqest-GET-ACL/Access/*`
  * :ref:`reuqest-GET-ACL/Group/*/Access/*`
  * :ref:`reuqest-GET-Security/Right/*/Access/*`
  * :ref:`reuqest-GET-ACL/Access`
  * :ref:`reuqest-GET-ACL/Group/*/Access`
  * :ref:`reuqest-GET-Security/Right/*/Access`
* **Can be inserted (POST) using**

  * :ref:`reuqest-POST-ACL/Access`
* **There are no paths where you can update (PUT) this model**
* **Can be deleted (DELETE) using**

  * :ref:`reuqest-DELETE-ACL/Access/*`
* **Can be linked (PUT) using**

  * :ref:`reuqest-LINK-ACL/Group/*/Access/*`
  * :ref:`reuqest-LINK-ACL/Group/*/Access/*/CompensateAccess/*`
  * :ref:`reuqest-LINK-ACL/Group/*/Access/*/Entry/*/Filter/*`
  * :ref:`reuqest-LINK-ACL/Group/*/Access/*/Filter/*`
  * :ref:`reuqest-LINK-Security/Right/*/Access/*`
  * :ref:`reuqest-LINK-Security/Right/*/Access/*/CompensateAccess/*`
  * :ref:`reuqest-LINK-Security/Right/*/Access/*/Entry/*/Filter/*`
  * :ref:`reuqest-LINK-Security/Right/*/Access/*/Filter/*`
* **Can be unlinked (DELETE) using**

  * :ref:`reuqest-UNLINK-ACL/Group/*/Access/*`
  * :ref:`reuqest-UNLINK-ACL/Group/*/Access/*/CompensateAccess/*`
  * :ref:`reuqest-UNLINK-ACL/Group/*/Access/*/Entry/*/Filter/*`
  * :ref:`reuqest-UNLINK-ACL/Group/*/Access/*/Property/*/Filter/*`
  * :ref:`reuqest-UNLINK-Security/Right/*/Access/*`
  * :ref:`reuqest-UNLINK-Security/Right/*/Access/*/CompensateAccess/*`
  * :ref:`reuqest-UNLINK-Security/Right/*/Access/*/Entry/*/Filter/*`
  * :ref:`reuqest-UNLINK-Security/Right/*/Access/*/Property/*/Filter/*`