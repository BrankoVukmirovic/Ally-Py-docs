.. _model-Indexing/Perform:

**Indexing/Perform**
==========================================================

The model is defined by the following API model classes.

.. _entity-indexing.api.indexing.Perform:

``indexing.api.indexing.Perform``
-------------------------------------------------------------------
::

   Provides the perform of an action, as defined in @see: ally.indexing.spec.model.Perform



+----------+----------------+----------------------------+
| Property |      Type      |         Description        |
+==========+================+============================+
| Id       | int            | Is model unique identifier |
+----------+----------------+----------------------------+
| Actions  | List[str]      |                            |
+----------+----------------+----------------------------+
| Escapes  | Dict[str: str] |                            |
+----------+----------------+----------------------------+
| Flags    | List[str]      |                            |
+----------+----------------+----------------------------+
| Index    | str            |                            |
+----------+----------------+----------------------------+
| Key      | str            |                            |
+----------+----------------+----------------------------+
| Name     | str            |                            |
+----------+----------------+----------------------------+
| Value    | str            |                            |
+----------+----------------+----------------------------+
| Verb     | str            |                            |
+----------+----------------+----------------------------+





**Model paths**
-------------------------------------------------
* **Can be obtained (GET) using**

  * :ref:`reuqest-GET-ACL/Access/*/Perform/*`
  * :ref:`reuqest-GET-ACL/Group/*/Access/*/Entry/*/Perform/*`
  * :ref:`reuqest-GET-ACL/Group/*/Access/*/Perform/*`
  * :ref:`reuqest-GET-ACL/Group/*/Access/*/Property/*/Perform/*`
  * :ref:`reuqest-GET-ACL/Group/*/Action/*/Perform/*`
  * :ref:`reuqest-GET-ACL/Group/*/Perform/*`
  * :ref:`reuqest-GET-GUI/Action/*/Perform/*`
  * :ref:`reuqest-GET-HR/User/*/Action/*/Perform/*`
  * :ref:`reuqest-GET-HR/User/*/Perform/*`
  * :ref:`reuqest-GET-HR/User/*/RightType/*/Perform/*`
  * :ref:`reuqest-GET-Indexing/Action/*/Perform/*`
  * :ref:`reuqest-GET-Indexing/Block/*/Perform/*`
  * :ref:`reuqest-GET-Indexing/Perform/*`
  * :ref:`reuqest-GET-RBAC/Role/*/Perform/*`
  * :ref:`reuqest-GET-RBAC/Role/*/RightType/*/Perform/*`
  * :ref:`reuqest-GET-Security/Right/*/Access/*/Entry/*/Perform/*`
  * :ref:`reuqest-GET-Security/Right/*/Access/*/Perform/*`
  * :ref:`reuqest-GET-Security/Right/*/Access/*/Property/*/Perform/*`
  * :ref:`reuqest-GET-Security/Right/*/Action/*/Perform/*`
  * :ref:`reuqest-GET-Security/Right/*/Perform/*`
  * :ref:`reuqest-GET-Security/RightType/*/Perform/*`
  * :ref:`reuqest-GET-Indexing/Action/*/Perform`
* **There are no paths where you can insert (POST) this model**
* **There are no paths where you can update (PUT) this model**
* **There are no paths where you can delete (DELETE) this model**
* **There are no paths where you can link (PUT) this model**
* **There are no paths where you can unlinked (DELETE) this model**