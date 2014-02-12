{% import '_definition.rst' as definition -%}
.. _reuqest-{{ request['method'] }}-{{ request['path'] }}:

**{{ request['path'] }}**
==========================================================

* Use the HTTP **POST** method in order to insert the model :ref:`entity-{{ request['entity']['name'] }}`
* The request is defined by API call ``{{ request['call'] }}``
{%- if request['path_params'] %}
* The inserted model will be linked with:
{% for param in request['path_params'] %}
 * The model :ref:`entity-{{ param['entity']['name'] }}` uniquelly identified by **{{ param['name'] }}**.
{%- endfor %}
{%- endif %}

::

{{ ident(request['doc']) }}

Content properties
-------------------------------------
{%- if 'properties' in request %}
This are the available model properties.

{% set table = TextTable('Property', 'Accepts', 'Description') -%}
{% for name, defin in request['properties'].items() -%}
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
There are no model properties required for this request.
{% endif %}

Response
-------------------------------------
Provides a 201 successful created code in case the model entity has been successfully inserted, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html#sec9.5 in case
of creation problems a 400 code is provided with explanations about the problem.