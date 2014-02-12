{% import '_definition.rst' as definition -%}
.. _reuqest-{{ request['method'] }}-{{ request['path'] }}:

**{{ request['path'] }}**
==========================================================

{{ request['doc'] }}


 * The request is defined by API call ``{{ request['call'] }}``
{% block description %}{% endblock %}

URL parameters
-------------------------------------
{{ request['url'] }}


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