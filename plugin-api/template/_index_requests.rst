.. _{{ method }} requests:

{{ method }} requests
==========================================================

{{ description }}

Contents:

.. toctree::
   :maxdepth: 1

{% for request in data['methods'].get(method, ()) -%}
   {% set path = 'requests_%s/%s.rst' % (method, request['path'].replace('/', '_')) -%}
   {% if render('_request_%s.rst' % method, path, request=request, data=data)  %}
   {{ path -}}
   {%- endif -%}
{% endfor %}
