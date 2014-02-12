.. _headers:

Headers
==========================================================

The headers recognized by the application.


.. _header-Accept:

Accept
-------------------------------------
Possible value(s) for the header are:

 * *xml*
 * *text/xml*
 * *text/json*
 * *application/x-www-form-urlencoded*
 * *json*
 * *application/xml*
 * *application/json*
 * *text/plain*

The accepted encodings, based on http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html
The simple mime types (the ones with no slash) can be provided as URL extension

.. _header-Content-Type:

Content-Type
-------------------------------------
Same as '*Accept*' header but is to provide the input content encoding

.. _header-X-HTTP-Method-Override:

X-HTTP-Method-Override
-------------------------------------
Used in order to override the actual HTTP method to the specified method
The header value can also be provided as a parameter

.. _header-TimeZone:

TimeZone
-------------------------------------
The time zone to render the time stamps in, as an example:

  * *Africa/Abidjan*
  * *Brazil/Acre*
  * *CET*
  * *EET*
  * *GB*
  * *HST*
  * *Iceland*
  * *Jamaica*
  * *Kwajalein*
  * *Libya*
  * *MET*
  * *NZ*
  * *PRC*
  * *ROC*
  * *Singapore*
  * *Turkey*
  * *UCT*
  * *W-SU*
  * *Zulu*
 
The default time zone is *UTC*
The header value can also be provided as a parameter

.. _header-Content-TimeZone:

Content-TimeZone
-------------------------------------
Same as '*TimeZone*' but for parsed content
The header value can also be provided as a parameter

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