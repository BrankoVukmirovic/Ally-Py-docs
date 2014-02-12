.. _model-ACL/Compensate:

**ACL/Compensate**
==========================================================

The model is defined by the following API model classes.

.. _entity-acl.api.compensate.Compensate:

``acl.api.compensate.Compensate``
-------------------------------------------------------------------
::

   Contains data required for an ACL access compensate.
       Access -     the access that is being compensated.
       Path -       contains the path that the access maps to. The path contains beside the fixed string
                    names also markers like {1}, {2} ... {n} which represent the positions from the compensated request
                    path where values need to be placed.
       Mapping -    the mapping of positions, as a key the compensating access position and as a value the corresponding
                    compensated access position.



+----------+-------------------------+-------------+
| Property |           Type          | Description |
+==========+=========================+=============+
| Access   | :ref:`model-ACL/Access` |             |
+----------+-------------------------+-------------+
| Mapping  | Dict[int: int]          |             |
+----------+-------------------------+-------------+
| Path     | str                     |             |
+----------+-------------------------+-------------+





**Model paths**
-------------------------------------------------
* **Can be obtained (GET) using**

  * :ref:`reuqest-GET-ACL/Group/*/Access/*/Compensate`
  * :ref:`reuqest-GET-Security/Right/*/Access/*/Compensate`
* **There are no paths where you can insert (POST) this model**
* **There are no paths where you can update (PUT) this model**
* **There are no paths where you can delete (DELETE) this model**
* **There are no paths where you can link (PUT) this model**
* **There are no paths where you can unlinked (DELETE) this model**