.. _model-Localization/Language:

**Localization/Language**
==========================================================

The model is defined by the following API model classes.

.. _entity-internationalization.language.api.language.Language:

``internationalization.language.api.language.Language``
-------------------------------------------------------------------
::

   Provides the language model.



+-----------+------+----------------------------+
|  Property | Type |         Description        |
+===========+======+============================+
| Code      | str  | Is model unique identifier |
+-----------+------+----------------------------+
| Name      | str  |                            |
+-----------+------+----------------------------+
| Script    | str  |                            |
+-----------+------+----------------------------+
| Territory | str  |                            |
+-----------+------+----------------------------+
| Variant   | str  |                            |
+-----------+------+----------------------------+





**Model paths**
-------------------------------------------------
* **Can be obtained (GET) using**

  * :ref:`reuqest-GET-ACL/Access/*/Language/*`
  * :ref:`reuqest-GET-ACL/Group/*/Access/*/Entry/*/Language/*`
  * :ref:`reuqest-GET-ACL/Group/*/Access/*/Language/*`
  * :ref:`reuqest-GET-ACL/Group/*/Access/*/Property/*/Language/*`
  * :ref:`reuqest-GET-ACL/Group/*/Action/*/Language/*`
  * :ref:`reuqest-GET-ACL/Group/*/Language/*`
  * :ref:`reuqest-GET-GUI/Action/*/Language/*`
  * :ref:`reuqest-GET-HR/User/*/Action/*/Language/*`
  * :ref:`reuqest-GET-HR/User/*/Language/*`
  * :ref:`reuqest-GET-HR/User/*/RightType/*/Language/*`
  * :ref:`reuqest-GET-Indexing/Action/*/Language/*`
  * :ref:`reuqest-GET-Indexing/Block/*/Language/*`
  * :ref:`reuqest-GET-Localization/Language/*`
  * :ref:`reuqest-GET-RBAC/Role/*/Language/*`
  * :ref:`reuqest-GET-RBAC/Role/*/RightType/*/Language/*`
  * :ref:`reuqest-GET-Security/Right/*/Access/*/Entry/*/Language/*`
  * :ref:`reuqest-GET-Security/Right/*/Access/*/Language/*`
  * :ref:`reuqest-GET-Security/Right/*/Access/*/Property/*/Language/*`
  * :ref:`reuqest-GET-Security/Right/*/Action/*/Language/*`
  * :ref:`reuqest-GET-Security/Right/*/Language/*`
  * :ref:`reuqest-GET-Security/RightType/*/Language/*`
  * :ref:`reuqest-GET-Localization/AvailableLanguage`
  * :ref:`reuqest-GET-Localization/Language`
* **There are no paths where you can insert (POST) this model**
* **There are no paths where you can update (PUT) this model**
* **Can be deleted (DELETE) using**

  * :ref:`reuqest-DELETE-Localization/Language/*`
* **Can be linked (PUT) using**

  * :ref:`reuqest-LINK-Localization/Language/*`
  * :ref:`reuqest-LINK-Localization/Language/*/MessagesPO/*`
  * :ref:`reuqest-LINK-Localization/MessagesLanguage/*`
* **There are no paths where you can unlinked (DELETE) this model**