.. _model-Security/Login:

**Security/Login**
==========================================================

The model is defined by the following API model classes.

.. _entity-superdesk.security.api.authentication.Login:

``superdesk.security.api.authentication.Login``
-------------------------------------------------------------------
::

   The login model.



+------------+----------------------+----------------------------+
|  Property  |         Type         |         Description        |
+============+======================+============================+
| Session    | str                  | Is model unique identifier |
+------------+----------------------+----------------------------+
| AccessedOn | datetime             |                            |
+------------+----------------------+----------------------------+
| CreatedOn  | datetime             |                            |
+------------+----------------------+----------------------------+
| User       | :ref:`model-HR/User` |                            |
+------------+----------------------+----------------------------+





**Model paths**
-------------------------------------------------
* **There are no paths where you can obtain (GET) this model**
* **Can be inserted (POST) using**

  * :ref:`reuqest-POST-Security/Login`
* **There are no paths where you can update (PUT) this model**
* **There are no paths where you can delete (DELETE) this model**
* **There are no paths where you can link (PUT) this model**
* **There are no paths where you can unlinked (DELETE) this model**