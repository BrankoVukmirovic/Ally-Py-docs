.. _model-Security/Right:

**Security/Right**
==========================================================

The model is defined by the following API model classes.

.. _entity-security.api.right.Right:

``security.api.right.Right``
-------------------------------------------------------------------
::

   Provides the right data.



+-------------+---------------------------------+----------------------------+
|   Property  |               Type              |         Description        |
+=============+=================================+============================+
| Id          | int                             | Is model unique identifier |
+-------------+---------------------------------+----------------------------+
| Description | str                             |                            |
+-------------+---------------------------------+----------------------------+
| Name        | str                             |                            |
+-------------+---------------------------------+----------------------------+
| Type        | :ref:`model-Security/RightType` |                            |
+-------------+---------------------------------+----------------------------+





**Model paths**
-------------------------------------------------
* **Can be obtained (GET) using**

  * :ref:`reuqest-GET-Security/Right/*`
  * :ref:`reuqest-GET-ACL/Access/*/Right`
  * :ref:`reuqest-GET-HR/User/*/Right`
  * :ref:`reuqest-GET-HR/User/*/RightType/*/Right`
  * :ref:`reuqest-GET-RBAC/Role/*/Right`
  * :ref:`reuqest-GET-RBAC/Role/*/RightType/*/Right`
  * :ref:`reuqest-GET-Security/Right`
  * :ref:`reuqest-GET-Security/RightType/*/Right`
* **Can be inserted (POST) using**

  * :ref:`reuqest-POST-Security/Right`
* **Can be updated (PUT) using**

  * :ref:`reuqest-PUT-Security/Right/*`
* **Can be deleted (DELETE) using**

  * :ref:`reuqest-DELETE-Security/Right/*`
* **Can be linked (PUT) using**

  * :ref:`reuqest-LINK-HR/User/*/Right/*`
  * :ref:`reuqest-LINK-RBAC/Role/*/Right/*`
  * :ref:`reuqest-LINK-Security/Right/*/Access/*`
  * :ref:`reuqest-LINK-Security/Right/*/Access/*/CompensateAccess/*`
  * :ref:`reuqest-LINK-Security/Right/*/Access/*/Entry/*/Filter/*`
  * :ref:`reuqest-LINK-Security/Right/*/Access/*/Filter/*`
  * :ref:`reuqest-LINK-Security/Right/*/Action/*`
* **Can be unlinked (DELETE) using**

  * :ref:`reuqest-UNLINK-HR/User/*/Right/*`
  * :ref:`reuqest-UNLINK-RBAC/Role/*/Right/*`
  * :ref:`reuqest-UNLINK-Security/Right/*/Access/*`
  * :ref:`reuqest-UNLINK-Security/Right/*/Access/*/CompensateAccess/*`
  * :ref:`reuqest-UNLINK-Security/Right/*/Access/*/Entry/*/Filter/*`
  * :ref:`reuqest-UNLINK-Security/Right/*/Access/*/Property/*/Filter/*`
  * :ref:`reuqest-UNLINK-Security/Right/*/Action/*`