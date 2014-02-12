.. _model-HR/Person:

**HR/Person**
==========================================================

The model is defined by the following API model classes.

.. _entity-superdesk.person.api.person.Person:

``superdesk.person.api.person.Person``
-------------------------------------------------------------------
::

   Provides the person model.



+-------------+------+----------------------------+
|   Property  | Type |         Description        |
+=============+======+============================+
| Id          | int  | Is model unique identifier |
+-------------+------+----------------------------+
| Address     | str  |                            |
+-------------+------+----------------------------+
| EMail       | str  |                            |
+-------------+------+----------------------------+
| FirstName   | str  |                            |
+-------------+------+----------------------------+
| FullName    | str  |                            |
+-------------+------+----------------------------+
| LastName    | str  |                            |
+-------------+------+----------------------------+
| PhoneNumber | str  |                            |
+-------------+------+----------------------------+





**Model paths**
-------------------------------------------------
* **Can be obtained (GET) using**

  * :ref:`reuqest-GET-HR/Person/*`
  * :ref:`reuqest-GET-HR/Person`
* **Can be inserted (POST) using**

  * :ref:`reuqest-POST-HR/Person`
* **Can be updated (PUT) using**

  * :ref:`reuqest-PUT-HR/Person/*`
* **Can be deleted (DELETE) using**

  * :ref:`reuqest-DELETE-HR/Person/*`
* **There are no paths where you can link (PUT) this model**
* **There are no paths where you can unlinked (DELETE) this model**