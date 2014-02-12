.. _headers_parameters:

Headers as Parameters 
==========================================================

{% if data['headersAsParam'] -%}
This headers are allowed to be provided as parameters in order to compensate for restrictive browsers.

{% for name in data['headersAsParam'] -%}
* :ref:`header-{{ name }}`
{% endfor %}
* :ref:`header-X-Filter` this is in the case of **assemblage** package or a proxy is present and allows the header as a parameter.
* ``Authorization`` this is in the case of **gateway** package or a proxy is present and allows the header as a parameter.
{% else -%}
The application is not configured to allow headers to be provided as parameters, usually is enabled by default but in order to enable this
go in the *application.properties* file and look for ``read_from_params`` and set it to ``True``, you might find multiple entries for this configuration if you have installed the 
**assemblage** package or/and  **gateway** package. In the case of **assemblage** it refers to the :ref:`header-X-Filter` header in order to be allowed or not as parameter and in case of **gateway**
it refers to ``Authorization`` header.
{%- endif %}
