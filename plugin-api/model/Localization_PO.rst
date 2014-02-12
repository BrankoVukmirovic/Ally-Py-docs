.. _model-Localization/PO:

**Localization/PO**
==========================================================

The model is defined by the following API model classes.

.. _entity-internationalization.api.po_file.PO:

``internationalization.api.po_file.PO``
-------------------------------------------------------------------
::

   Model for a PO file.



+-----------+------+--------------------------------------+
|  Property | Type |              Description             |
+===========+======+======================================+
| Name      | str  | Is model unique identifier           |
+-----------+------+--------------------------------------+
| Reference | str  | A URL to the location of the content |
+-----------+------+--------------------------------------+





**Model paths**
-------------------------------------------------
* **Can be obtained (GET) using**

  * :ref:`reuqest-GET-Localization/Language/*/MessagesPO/*`
  * :ref:`reuqest-GET-Localization/MessagesLanguagePO/*`
  * :ref:`reuqest-GET-Localization/TemplatePO`
  * :ref:`reuqest-GET-Localization/TemplatePO/*`
* **There are no paths where you can insert (POST) this model**
* **There are no paths where you can update (PUT) this model**
* **There are no paths where you can delete (DELETE) this model**
* **Can be linked (PUT) using**

  * :ref:`reuqest-LINK-Localization/Language/*/MessagesPO/*`
  * :ref:`reuqest-LINK-Localization/MessagesLanguage/*`
  * :ref:`reuqest-LINK-Localization/TemplatePO/*`
* **There are no paths where you can unlinked (DELETE) this model**