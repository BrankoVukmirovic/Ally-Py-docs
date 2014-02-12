.. _model-{{ model['name'] }}:

**{{ model['name'] }}**
==========================================================

The model is defined by the following API model classes.

{% for entity in model['entities'] -%}
.. _entity-{{ entity['name'] }}:

``{{ entity['name'] }}``
-------------------------------------------------------------------
::

{{ ident(entity['doc']) }}



{% set table = TextTable('Property', 'Type', 'Description') -%}
{% for prop in entity['properties'] -%}
  {% set description = '' -%}
  {% if 'isId' in prop['flags'] -%}
    {% set description = 'Is model unique identifier' -%}
  {% endif -%}
  {% if 'isReference' in prop['flags'] -%}
    {% set description = 'A URL to the location of the content' -%}
  {% endif -%}
  {% if 'model' in prop -%}
    {% set ptype = ':ref:`model-' + prop['model']['name'] + '`' -%}
  {% else -%}
    {% set ptype = prop['type'] -%}
  {% endif -%}
  {% do table.add(prop['name'], ptype, description) -%}
{% endfor -%}
{{ table.render() }}

{% endfor %}


**Model paths**
-------------------------------------------------

{%- if 'GET' in model['methods'] %}
* **Can be obtained (GET) using**
{% for request in model['methods']['GET'] %}
  * :ref:`reuqest-GET-{{ request['path'] }}`
{%- endfor %}
{%- else %}
* **There are no paths where you can obtain (GET) this model**
{%- endif %}

{%- if 'POST' in model['methods'] %}
* **Can be inserted (POST) using**
{% for request in model['methods']['POST'] %}
  * :ref:`reuqest-POST-{{ request['path'] }}`
{%- endfor %}
{%- else %}
* **There are no paths where you can insert (POST) this model**
{%- endif %}

{%- if 'PUT' in model['methods'] %}
* **Can be updated (PUT) using**
{% for request in model['methods']['PUT'] %}
  * :ref:`reuqest-PUT-{{ request['path'] }}`
{%- endfor %}
{%- else %}
* **There are no paths where you can update (PUT) this model**
{%- endif %}

{%- if 'DELETE' in model['methods'] %}
* **Can be deleted (DELETE) using**
{% for request in model['methods']['DELETE'] %}
  * :ref:`reuqest-DELETE-{{ request['path'] }}`
{%- endfor %}
{%- else %}
* **There are no paths where you can delete (DELETE) this model**
{%- endif %}


{%- if 'LINK' in model['methods'] %}
* **Can be linked (PUT) using**
{% for request in model['methods']['LINK'] %}
  * :ref:`reuqest-LINK-{{ request['path'] }}`
{%- endfor %}
{%- else %}
* **There are no paths where you can link (PUT) this model**
{%- endif %}

{%- if 'UNLINK' in model['methods'] %}
* **Can be unlinked (DELETE) using**
{% for request in model['methods']['UNLINK'] %}
  * :ref:`reuqest-UNLINK-{{ request['path'] }}`
{%- endfor %}
{%- else %}
* **There are no paths where you can unlinked (DELETE) this model**
{%- endif %}