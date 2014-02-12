.. _model-GUI/Action:

**GUI/Action**
==========================================================

The model is defined by the following API model classes.

.. _entity-gui.action.api.action.Action:

``gui.action.api.action.Action``
-------------------------------------------------------------------
::

   The object used to create and group actions 



+----------+------+--------------------------------------+
| Property | Type |              Description             |
+==========+======+======================================+
| Path     | str  | Is model unique identifier           |
+----------+------+--------------------------------------+
| Label    | str  |                                      |
+----------+------+--------------------------------------+
| NavBar   | str  |                                      |
+----------+------+--------------------------------------+
| Script   | str  | A URL to the location of the content |
+----------+------+--------------------------------------+





**Model paths**
-------------------------------------------------
* **Can be obtained (GET) using**

  * :ref:`reuqest-GET-ACL/Group/*/Action/*`
  * :ref:`reuqest-GET-GUI/Action/*`
  * :ref:`reuqest-GET-HR/User/*/Action/*`
  * :ref:`reuqest-GET-Security/Right/*/Action/*`
  * :ref:`reuqest-GET-ACL/Group/*/Action`
  * :ref:`reuqest-GET-ACL/Group/*/Action/*/SubAction`
  * :ref:`reuqest-GET-ACL/Group/*/AllAction`
  * :ref:`reuqest-GET-GUI/Action`
  * :ref:`reuqest-GET-GUI/Action/*/SubAction`
  * :ref:`reuqest-GET-GUI/AllAction`
  * :ref:`reuqest-GET-HR/User/*/Action`
  * :ref:`reuqest-GET-HR/User/*/Action/*/SubAction`
  * :ref:`reuqest-GET-HR/User/*/AllAction`
  * :ref:`reuqest-GET-Security/Right/*/Action`
  * :ref:`reuqest-GET-Security/Right/*/Action/*/SubAction`
  * :ref:`reuqest-GET-Security/Right/*/AllAction`
* **Can be inserted (POST) using**

  * :ref:`reuqest-POST-GUI/Action`
* **Can be updated (PUT) using**

  * :ref:`reuqest-PUT-GUI/Action/*`
* **Can be deleted (DELETE) using**

  * :ref:`reuqest-DELETE-GUI/Action/*`
* **Can be linked (PUT) using**

  * :ref:`reuqest-LINK-ACL/Group/*/Action/*`
  * :ref:`reuqest-LINK-Security/Right/*/Action/*`
* **Can be unlinked (DELETE) using**

  * :ref:`reuqest-UNLINK-ACL/Group/*/Action/*`
  * :ref:`reuqest-UNLINK-Security/Right/*/Action/*`