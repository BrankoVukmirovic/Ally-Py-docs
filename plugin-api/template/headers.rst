{% import '_definition.rst' as definition -%}
.. _headers:

Headers
==========================================================

The headers recognized by the application.
{% for name, defin in data['headers'].items() %}

.. _header-{{ name }}:

{{ name }}
-------------------------------------
  {%- if 'types' in defin -%}
Available type(s) for the header are:
{% for value in defin['types'] %}
 * **{{ value }}**
    {%- endfor %}
{% endif -%}
  
  {% if 'enumeration' in defin %}
Possible value(s) for the header are:
{% for value in defin['enumeration'] %}
 * *{{ value }}*
    {%- endfor %}
{% endif -%}
  
  {{ definition.description(defin['description']) -}}

{% endfor %}

.. _header-X-Filter:

X-Filter
-------------------------------------

This header is available only if the application is started with assemblage option on, by default this is activated if you have the **assemblage** package installed, if not in order to enable this
go in the *application.properties* file and look for ``server_provide_assemblage`` configuration and change it accordingly.
This header can also be provided as a parameter if the *assemblage* proxy is configured to allow that.

This header allows for data aggregation, a simple example:

.. code-block:: json

    {
      "Id":1,
      "Name":"Right1",
      "Type":{"href":"http://localhost:8080/resources/Security/RightType/Sample/","Name":"Sample"},
    }

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <Right>
      <Id>1</Id>
      <Name>Right1</Name>
      <Type href="http://localhost:8080/resources/Security/RightType/Sample/">
	<Name>Sample</Name>
      </Type>
    </Right>
    
    
So here we have a *Right* model that contains a *Type*, in order to get also the *Type* ...