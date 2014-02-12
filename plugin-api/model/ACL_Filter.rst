.. _model-ACL/Filter:

**ACL/Filter**
==========================================================

The model is defined by the following API model classes.

.. _entity-acl.api.filter.Filter:

``acl.api.filter.Filter``
-------------------------------------------------------------------
::

   Contains data required for an ACL filter.
       Path -       contains the path that the filter maps to. The path contains beside the fixed string
                    names also markers '*' for where the filtered values or injected values will be placed.
       Hash -       the hash that represents the full aspect of the filter.
       Signature -  the type signature associated with the target path entry.



+-----------+------+----------------------------+
|  Property | Type |         Description        |
+===========+======+============================+
| Name      | str  | Is model unique identifier |
+-----------+------+----------------------------+
| Path      | str  |                            |
+-----------+------+----------------------------+
| Signature | str  |                            |
+-----------+------+----------------------------+





**Model paths**
-------------------------------------------------
* **Can be obtained (GET) using**

  * :ref:`reuqest-GET-ACL/Filter/*`
  * :ref:`reuqest-GET-ACL/Filter`
  * :ref:`reuqest-GET-ACL/Group/*/Access/*/Entry/*/Filter`
  * :ref:`reuqest-GET-ACL/Group/*/Access/*/Property/*/Filter`
  * :ref:`reuqest-GET-Security/Right/*/Access/*/Entry/*/Filter`
  * :ref:`reuqest-GET-Security/Right/*/Access/*/Property/*/Filter`
* **Can be inserted (POST) using**

  * :ref:`reuqest-POST-ACL/Filter`
* **There are no paths where you can update (PUT) this model**
* **Can be deleted (DELETE) using**

  * :ref:`reuqest-DELETE-ACL/Filter/*`
* **Can be linked (PUT) using**

  * :ref:`reuqest-LINK-ACL/Group/*/Access/*/Entry/*/Filter/*`
  * :ref:`reuqest-LINK-ACL/Group/*/Access/*/Filter/*`
  * :ref:`reuqest-LINK-Security/Right/*/Access/*/Entry/*/Filter/*`
  * :ref:`reuqest-LINK-Security/Right/*/Access/*/Filter/*`
* **Can be unlinked (DELETE) using**

  * :ref:`reuqest-UNLINK-ACL/Group/*/Access/*/Entry/*/Filter/*`
  * :ref:`reuqest-UNLINK-ACL/Group/*/Access/*/Property/*/Filter/*`
  * :ref:`reuqest-UNLINK-Security/Right/*/Access/*/Entry/*/Filter/*`
  * :ref:`reuqest-UNLINK-Security/Right/*/Access/*/Property/*/Filter/*`