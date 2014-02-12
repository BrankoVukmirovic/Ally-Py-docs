.. _model-ACL/Property:

**ACL/Property**
==========================================================

The model is defined by the following API model classes.

.. _entity-acl.api.access.Property:

``acl.api.access.Property``
-------------------------------------------------------------------
::

   The input model property associated with an access.
   
   Name -            the property name.
   Signature -       the type signature associated with the input model property.



+-----------+------+----------------------------+
|  Property | Type |         Description        |
+===========+======+============================+
| Name      | str  | Is model unique identifier |
+-----------+------+----------------------------+
| Signature | str  |                            |
+-----------+------+----------------------------+





**Model paths**
-------------------------------------------------
* **Can be obtained (GET) using**

  * :ref:`reuqest-GET-ACL/Access/*/Property/*`
  * :ref:`reuqest-GET-ACL/Group/*/Access/*/Property/*`
  * :ref:`reuqest-GET-Security/Right/*/Access/*/Property/*`
  * :ref:`reuqest-GET-ACL/Access/*/Property`
  * :ref:`reuqest-GET-ACL/Group/*/Access/*/Property`
  * :ref:`reuqest-GET-Security/Right/*/Access/*/Property`
* **There are no paths where you can insert (POST) this model**
* **Can be updated (PUT) using**

  * :ref:`reuqest-PUT-ACL/Group/*/Access/*/Filter/*/Property/*`
  * :ref:`reuqest-PUT-Security/Right/*/Access/*/Filter/*/Property/*`
* **There are no paths where you can delete (DELETE) this model**
* **There are no paths where you can link (PUT) this model**
* **Can be unlinked (DELETE) using**

  * :ref:`reuqest-UNLINK-ACL/Group/*/Access/*/Property/*/Filter/*`
  * :ref:`reuqest-UNLINK-Security/Right/*/Access/*/Property/*/Filter/*`