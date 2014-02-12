.. _reuqest-PUT-Gateway/Custom/*:

**Gateway/Custom/***
==========================================================

* Use the HTTP **PUT** method in order to update the model :ref:`entity-gateway.api.gateway.Custom`
* The request is defined by API call ``gateway.api.gateway.IGatewayService.update``
* The updated model is identified by:

 * The model :ref:`entity-gateway.api.gateway.Custom` uniquelly identified by **Custom.Name**.

::

   Update the entity.
   
   @param entity: Entity
       The entity to be updated.

Content properties
-------------------------------------
This are the available model properties.

+------------+----------------------+-------------+
|  Property  |        Accepts       | Description |
+============+======================+=============+
| Clients    | * **List[str]**      |             |
+------------+----------------------+-------------+
| Errors     | * **List[int]**      |             |
+------------+----------------------+-------------+
| Exclude    | * **List[str]**      |             |
+------------+----------------------+-------------+
| Filters    | * **List[str]**      |             |
+------------+----------------------+-------------+
| Headers    | * **List[str]**      |             |
+------------+----------------------+-------------+
| Host       | * **str**            |             |
+------------+----------------------+-------------+
| Methods    | * **List[str]**      |             |
+------------+----------------------+-------------+
| Navigate   | * **str**            |             |
+------------+----------------------+-------------+
| Pattern    | * **str**            |             |
+------------+----------------------+-------------+
| Protocol   | * **str**            |             |
+------------+----------------------+-------------+
| PutHeaders | * **Dict[str: str]** |             |
+------------+----------------------+-------------+



Response
-------------------------------------
Provides a 200 successful updated code in case the model entity has been successfully inserted, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html#sec9.6 in case
of update problems a 400 code is provided with explanations about the problem.