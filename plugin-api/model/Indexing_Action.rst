.. _model-Indexing/Action:

**Indexing/Action**
==========================================================

The model is defined by the following API model classes.

.. _entity-indexing.api.indexing.Action:

``indexing.api.indexing.Action``
-------------------------------------------------------------------
::

   Provides the action of a block, as defined in @see: ally.indexing.spec.model.Action



+----------+-----------+----------------------------+
| Property |    Type   |         Description        |
+==========+===========+============================+
| Id       | int       | Is model unique identifier |
+----------+-----------+----------------------------+
| Before   | List[str] |                            |
+----------+-----------+----------------------------+
| Final    | bool      |                            |
+----------+-----------+----------------------------+
| Name     | str       |                            |
+----------+-----------+----------------------------+
| Rewind   | bool      |                            |
+----------+-----------+----------------------------+





**Model paths**
-------------------------------------------------
* **Can be obtained (GET) using**

  * :ref:`reuqest-GET-ACL/Access/*/Action/*`
  * :ref:`reuqest-GET-ACL/Group/*/Access/*/Action/*`
  * :ref:`reuqest-GET-ACL/Group/*/Access/*/Entry/*/Action/*`
  * :ref:`reuqest-GET-ACL/Group/*/Access/*/Property/*/Action/*`
  * :ref:`reuqest-GET-ACL/Group/*/Action/*/Action/*`
  * :ref:`reuqest-GET-GUI/Action/*/Action/*`
  * :ref:`reuqest-GET-HR/User/*/Action/*/Action/*`
  * :ref:`reuqest-GET-HR/User/*/RightType/*/Action/*`
  * :ref:`reuqest-GET-Indexing/Action/*`
  * :ref:`reuqest-GET-Indexing/Block/*/Action/*`
  * :ref:`reuqest-GET-RBAC/Role/*/Action/*`
  * :ref:`reuqest-GET-RBAC/Role/*/RightType/*/Action/*`
  * :ref:`reuqest-GET-Security/Right/*/Access/*/Action/*`
  * :ref:`reuqest-GET-Security/Right/*/Access/*/Entry/*/Action/*`
  * :ref:`reuqest-GET-Security/Right/*/Access/*/Property/*/Action/*`
  * :ref:`reuqest-GET-Security/Right/*/Action/*/Action/*`
  * :ref:`reuqest-GET-Security/RightType/*/Action/*`
  * :ref:`reuqest-GET-Indexing/Block/*/Action`
* **There are no paths where you can insert (POST) this model**
* **There are no paths where you can update (PUT) this model**
* **There are no paths where you can delete (DELETE) this model**
* **There are no paths where you can link (PUT) this model**
* **There are no paths where you can unlinked (DELETE) this model**