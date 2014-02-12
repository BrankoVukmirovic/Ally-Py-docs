.. _model-ACL/Entry:

**ACL/Entry**
==========================================================

The model is defined by the following API model classes.

.. _entity-acl.api.access.Entry:

``acl.api.access.Entry``
-------------------------------------------------------------------
::

   The path entry that corresponds to a '*' dynamic path input.
   
   :Position: The position of the entry in the access path.
   
   :Shadowing: The position that this entry is shadowing.
   
   :Shadowed: The position of the shadowed entry, also it means that the values belonging to it 
              will not be actually used by the access path request.
              
   :Signature: The type signature associated with the path entry.



+-----------+------+----------------------------+
|  Property | Type |         Description        |
+===========+======+============================+
| Position  | int  | Is model unique identifier |
+-----------+------+----------------------------+
| Shadowed  | int  |                            |
+-----------+------+----------------------------+
| Shadowing | int  |                            |
+-----------+------+----------------------------+
| Signature | str  |                            |
+-----------+------+----------------------------+





**Model paths**
-------------------------------------------------
* **Can be obtained (GET) using**

  * :ref:`reuqest-GET-ACL/Access/*/Entry/*`
  * :ref:`reuqest-GET-ACL/Group/*/Access/*/Entry/*`
  * :ref:`reuqest-GET-Security/Right/*/Access/*/Entry/*`
  * :ref:`reuqest-GET-ACL/Access/*/Entry`
  * :ref:`reuqest-GET-ACL/Group/*/Access/*/Entry`
  * :ref:`reuqest-GET-Security/Right/*/Access/*/Entry`
* **There are no paths where you can insert (POST) this model**
* **There are no paths where you can update (PUT) this model**
* **There are no paths where you can delete (DELETE) this model**
* **Can be linked (PUT) using**

  * :ref:`reuqest-LINK-ACL/Group/*/Access/*/Entry/*/Filter/*`
  * :ref:`reuqest-LINK-Security/Right/*/Access/*/Entry/*/Filter/*`
* **Can be unlinked (DELETE) using**

  * :ref:`reuqest-UNLINK-ACL/Group/*/Access/*/Entry/*/Filter/*`
  * :ref:`reuqest-UNLINK-Security/Right/*/Access/*/Entry/*/Filter/*`