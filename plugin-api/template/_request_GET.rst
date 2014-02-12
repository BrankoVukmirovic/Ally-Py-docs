{% import '_definition.rst' as definition -%}
.. _reuqest-GET-{{ request['path'] }}:

**{{ request['path'] }}**
==========================================================

* Use the HTTP **GET** method
* The request is defined by API call ``{{ request['call'] }}``
{% set flags = request['flags'] -%}
{% if 'isCollection' in flags -%}
  {% if 'isModel' in flags %}
* The request will GET a collection of models :ref:`entity-{{ request['entity']['name'] }}`
  {%- else -%}
    {% if 'isModelRef' in flags %}
* The request will GET a collection of references to models :ref:`entity-{{ request['entity']['name'] }}`
    {%- else %}
* The request will GET a collection of ``{{ request['property'] }}`` properties of models :ref:`entity-{{ request['entity']['name'] }}`
    {%- endif -%}
  {%- endif -%}
{%- else %}
  {% if 'isModel' in flags %}
* The request will GET a model :ref:`entity-{{ request['entity']['name'] }}`
  {%- else -%}
    {% if 'isModelRef' in flags %}
* The request will GET a reference to model :ref:`entity-{{ request['entity']['name'] }}`
    {%- else %}
* The request will GET a ``{{ request['property'] }}`` property o model :ref:`entity-{{ request['entity']['name'] }}`
    {%- endif -%}
  {%- endif -%}
{% endif %}

::

{{ ident(request['doc']) }}


{% if request['path_params'] -%}
URL parameters
-------------------------------------
Each entry matches a **\*** in their respective order.

{% for param in request['path_params'] -%}
* The unique identifier **{{ param['name'] }}** from :ref:`entity-{{ param['entity']['name'] }}`.
{% endfor -%}
{% endif %}

Query parameters
-------------------------------------
{%- if 'parameters' in request %}
This are the available query parameters, also check the global :ref:`headers_parameters`.

{% set table = TextTable('Parameter', 'Accepts', 'Description') -%}
{% for name, defin in request['parameters'].items() -%}
  {% if 'enumeration' in defin -%}
    {% set accepts = 'One of:\n\n%s' % '\n'.join(transform(defin['enumeration'], '* *%s*')) -%}
  {% else -%}
    {% if 'types' in defin -%}
      {% set accepts = '\n'.join(transform(defin['types'], '* **%s**')) -%}
    {% endif -%}
  {% endif -%}
  {% do table.add(name, accepts, definition.description(defin['description'])) -%}
{% endfor -%}
{{ table.render() }}
{% else %}
There are no query parameters available for this request except for global :ref:`headers_parameters`.
{% endif %}