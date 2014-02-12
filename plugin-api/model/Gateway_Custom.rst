.. _model-Gateway/Custom:

**Gateway/Custom**
==========================================================

The model is defined by the following API model classes.

.. _entity-gateway.api.gateway.Custom:

``gateway.api.gateway.Custom``
-------------------------------------------------------------------
::

   Provides the custom defined gateway.
       Name -      the unique name for the gateway.



+------------+----------------+----------------------------+
|  Property  |      Type      |         Description        |
+============+================+============================+
| Name       | str            | Is model unique identifier |
+------------+----------------+----------------------------+
| Clients    | List[str]      |                            |
+------------+----------------+----------------------------+
| Errors     | List[int]      |                            |
+------------+----------------+----------------------------+
| Exclude    | List[str]      |                            |
+------------+----------------+----------------------------+
| Filters    | List[str]      |                            |
+------------+----------------+----------------------------+
| Headers    | List[str]      |                            |
+------------+----------------+----------------------------+
| Host       | str            |                            |
+------------+----------------+----------------------------+
| Methods    | List[str]      |                            |
+------------+----------------+----------------------------+
| Navigate   | str            |                            |
+------------+----------------+----------------------------+
| Pattern    | str            |                            |
+------------+----------------+----------------------------+
| Protocol   | str            |                            |
+------------+----------------+----------------------------+
| PutHeaders | Dict[str: str] |                            |
+------------+----------------+----------------------------+





**Model paths**
-------------------------------------------------
* **Can be obtained (GET) using**

  * :ref:`reuqest-GET-Gateway/Custom/*`
  * :ref:`reuqest-GET-Gateway/Custom`
* **Can be inserted (POST) using**

  * :ref:`reuqest-POST-Gateway/Custom`
* **Can be updated (PUT) using**

  * :ref:`reuqest-PUT-Gateway/Custom/*`
* **Can be deleted (DELETE) using**

  * :ref:`reuqest-DELETE-Gateway/Custom/*`
* **There are no paths where you can link (PUT) this model**
* **There are no paths where you can unlinked (DELETE) this model**