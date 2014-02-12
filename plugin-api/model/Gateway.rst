.. _model-Gateway:

**Gateway**
==========================================================

The model is defined by the following API model classes.

.. _entity-gateway.api.gateway.Gateway:

``gateway.api.gateway.Gateway``
-------------------------------------------------------------------
::

   Provides the gateway.
       Filters -   contains a list of URIs that need to be called in order to allow the gateway Navigate. The filters
                   are provided as 'group:URI' where group is a number from 1 to n where n is the number of capture 
                   groups  obtained from the Pattern, the filter URI is allowed to have place holders of form '*'
                   where the provided group value will be injected. In order to validate navigation at least one filter
                   from the each group will have to return an allowed access, also pre populated parameters are allowed
                   for filter URI.
       Host -      The host where the request needs to be resolved, if not provided the request will be delegated to the
                   default host.
       Protocol -  The protocol to be used in the communication with the server that handles the request, if not provided
                   the request will be delegated using the default protocol.
       Navigate -  A pattern like string of forms like '*', 'resources/*' or 'redirect/Model/{1}'. The pattern is allowed to
                   have place holders and also the '*' which stands for the actual called URI, also parameters are allowed
                   for navigate URI, the parameters will be appended to the actual parameters.
       PutHeaders -The headers to be put on the forwarded requests.
       Exclude -   The list of index block names to be excluded from the response.



+------------+----------------+-------------+
|  Property  |      Type      | Description |
+============+================+=============+
| Clients    | List[str]      |             |
+------------+----------------+-------------+
| Errors     | List[int]      |             |
+------------+----------------+-------------+
| Exclude    | List[str]      |             |
+------------+----------------+-------------+
| Filters    | List[str]      |             |
+------------+----------------+-------------+
| Headers    | List[str]      |             |
+------------+----------------+-------------+
| Host       | str            |             |
+------------+----------------+-------------+
| Methods    | List[str]      |             |
+------------+----------------+-------------+
| Navigate   | str            |             |
+------------+----------------+-------------+
| Pattern    | str            |             |
+------------+----------------+-------------+
| Protocol   | str            |             |
+------------+----------------+-------------+
| PutHeaders | Dict[str: str] |             |
+------------+----------------+-------------+





**Model paths**
-------------------------------------------------
* **Can be obtained (GET) using**

  * :ref:`reuqest-GET-ACL/Group/*/Gateway`
  * :ref:`reuqest-GET-Gateway`
  * :ref:`reuqest-GET-Security/Login/*/Gateway`
* **There are no paths where you can insert (POST) this model**
* **There are no paths where you can update (PUT) this model**
* **There are no paths where you can delete (DELETE) this model**
* **There are no paths where you can link (PUT) this model**
* **There are no paths where you can unlinked (DELETE) this model**