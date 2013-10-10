{% macro transform(value, ident='\n') -%}

  {% if isColl(value) -%}
    {% for item in value -%}
{{ ident }} * *{{ item }}*
    {%- endfor -%}
{{ ident }}
  {%- else -%}
*{{ value }}*
  {%- endif -%}
  
{% endmacro %}

{% macro description(descriptions, ident='\n') -%}

  {% for desc, data in descriptions -%}
    {% set tdata = {} -%}
    {% for key, value in data.items() -%}
      {% do tdata.update({key: transform(value, ident=ident + ' ')}) -%}
    {% endfor -%}
{{ ident }}{{ upperFirst(desc % tdata)}}
  {%- endfor -%}
  
{% endmacro %}