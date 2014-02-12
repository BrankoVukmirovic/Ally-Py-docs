.. _models:

Available API models
==========================================================

This are the available models from the API. 

Contents:

.. toctree::
   :maxdepth: 1

{% for model in data['models'] -%}
   {% set path = 'model/%s.rst' % model['name'].replace('/', '_') -%}
   {% if render('_model.rst', path, model=model, data=data)  %}
   {{ path -}}
   {%- endif -%}
{% endfor %}
