.. _model-ACL/Group:

**ACL/Group**
==========================================================

The model is defined by the following API model classes.

.. _entity-acl.api.group.Group:

``acl.api.group.Group``
-------------------------------------------------------------------
::

   Defines the group of ACL access.
       Name -           the group unique name.
       IsAnonymous -    if true it means that the group should be delivered for anonymous access.
       Description -    a description explaining the group.



+-------------+------+----------------------------+
|   Property  | Type |         Description        |
+=============+======+============================+
| Name        | str  | Is model unique identifier |
+-------------+------+----------------------------+
| Description | str  |                            |
+-------------+------+----------------------------+
| IsAnonymous | bool |                            |
+-------------+------+----------------------------+





**Model paths**
-------------------------------------------------
* **Can be obtained (GET) using**

  * :ref:`reuqest-GET-ACL/Group/*`
  * :ref:`reuqest-GET-ACL/Access/*/Group`
  * :ref:`reuqest-GET-ACL/Group`
* **Can be inserted (POST) using**

  * :ref:`reuqest-POST-ACL/Group`
* **Can be updated (PUT) using**

  * :ref:`reuqest-PUT-ACL/Group/*`
* **Can be deleted (DELETE) using**

  * :ref:`reuqest-DELETE-ACL/Group/*`
* **Can be linked (PUT) using**

  * :ref:`reuqest-LINK-ACL/Group/*/Access/*`
  * :ref:`reuqest-LINK-ACL/Group/*/Access/*/CompensateAccess/*`
  * :ref:`reuqest-LINK-ACL/Group/*/Access/*/Entry/*/Filter/*`
  * :ref:`reuqest-LINK-ACL/Group/*/Access/*/Filter/*`
  * :ref:`reuqest-LINK-ACL/Group/*/Action/*`
* **Can be unlinked (DELETE) using**

  * :ref:`reuqest-UNLINK-ACL/Group/*/Access/*`
  * :ref:`reuqest-UNLINK-ACL/Group/*/Access/*/CompensateAccess/*`
  * :ref:`reuqest-UNLINK-ACL/Group/*/Access/*/Entry/*/Filter/*`
  * :ref:`reuqest-UNLINK-ACL/Group/*/Access/*/Property/*/Filter/*`
  * :ref:`reuqest-UNLINK-ACL/Group/*/Action/*`