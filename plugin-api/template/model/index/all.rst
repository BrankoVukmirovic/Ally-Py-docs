@require(models)
.. _models:

Welcome to Plugins API models documentation!
==========================================================

Contents:

.. toctree::
   :maxdepth: 2

@for model in models:
   model_api_@model['API'].replace('.', '_')!s.rst
@end

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`