{% import '_definition.rst' as definition -%}
.. _reuqest-{{ request['method'] }}-{{ request['path'] }}:

**{{ request['path'] }}**
==========================================================

* Use the HTTP **DELETE** method in order to unlink
* The request is defined by API call ``{{ request['call'] }}``
* The request will link, each entry matches a **\*** in their respective order:
{% for param in request['path_params'] %}
 * The model :ref:`entity-{{ param['entity']['name'] }}` uniquelly identified by **{{ param['name'] }}**.
{%- endfor %}


::

{{ ident(request['doc']) }}


Response
-------------------------------------
Provides a 204 delete successful code in case the model entities have been successfully unlinked, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html#sec9.7 in case
the provided model identifiers are invalid or not linked it will return a 400 cannot find code.