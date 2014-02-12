.. _model-RBAC/Role:

**RBAC/Role**
==========================================================

The model is defined by the following API model classes.

.. _entity-security.rbac.api.role.Role:

``security.rbac.api.role.Role``
-------------------------------------------------------------------
::

   The role model.



+-------------+------+----------------------------+
|   Property  | Type |         Description        |
+=============+======+============================+
| Name        | str  | Is model unique identifier |
+-------------+------+----------------------------+
| Description | str  |                            |
+-------------+------+----------------------------+





**Model paths**
-------------------------------------------------
* **Can be obtained (GET) using**

  * :ref:`reuqest-GET-RBAC/Role/*`
  * :ref:`reuqest-GET-HR/User/*/Role`
  * :ref:`reuqest-GET-RBAC/Role`
  * :ref:`reuqest-GET-RBAC/Role/*/SubRole`
* **Can be inserted (POST) using**

  * :ref:`reuqest-POST-RBAC/Role`
* **Can be updated (PUT) using**

  * :ref:`reuqest-PUT-RBAC/Role/*`
* **Can be deleted (DELETE) using**

  * :ref:`reuqest-DELETE-RBAC/Role/*`
  * :ref:`reuqest-DELETE-RBAC/Role/*/SubRole/*`
* **Can be linked (PUT) using**

  * :ref:`reuqest-LINK-HR/User/*/Role/*`
  * :ref:`reuqest-LINK-RBAC/Role/*/Right/*`
  * :ref:`reuqest-LINK-RBAC/Role/*/SubRole/*`
* **Can be unlinked (DELETE) using**

  * :ref:`reuqest-UNLINK-HR/User/*/Role/*`
  * :ref:`reuqest-UNLINK-RBAC/Role/*/Right/*`