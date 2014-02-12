{% import '_definition.rst' as definition -%}
.. _reuqest-DELETE-{{ request['path'] }}:

**{{ request['path'] }}**
==========================================================

* Use the HTTP **DELETE** method in order to remove models
* The request is defined by API call ``{{ request['call'] }}``
* Delete the entity :ref:`entity-{{ request['path_params'][0]['entity']['name'] }}` based on **{{ request['path_params'][0]['name'] }}**.


::

{{ ident(request['doc']) }}


Response
-------------------------------------
Provides a 204 delete successful code if the model associated with the identifier has been removed, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html#sec9.6 in case
of problems it will return a 400 cannot delete code.