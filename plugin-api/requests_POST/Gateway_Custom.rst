.. _reuqest-POST-Gateway/Custom:

**Gateway/Custom**
==========================================================

* Use the HTTP **POST** method in order to insert the model :ref:`entity-gateway.api.gateway.Custom`
* The request is defined by API call ``gateway.api.gateway.IGatewayService.insert``

::

   Insert the entity.
   
   @param entity: Entity
       The entity to be inserted.
   @return: object
       The identifier of the entity

Content properties
-------------------------------------
This are the available model properties.

+------------+----------------------+-------------------------+
|  Property  |        Accepts       |       Description       |
+============+======================+=========================+
| Name       | * **str**            |                         |
|            |                      | Represents the model id |
+------------+----------------------+-------------------------+
| Clients    | * **List[str]**      |                         |
+------------+----------------------+-------------------------+
| Errors     | * **List[int]**      |                         |
+------------+----------------------+-------------------------+
| Exclude    | * **List[str]**      |                         |
+------------+----------------------+-------------------------+
| Filters    | * **List[str]**      |                         |
+------------+----------------------+-------------------------+
| Headers    | * **List[str]**      |                         |
+------------+----------------------+-------------------------+
| Host       | * **str**            |                         |
+------------+----------------------+-------------------------+
| Methods    | * **List[str]**      |                         |
+------------+----------------------+-------------------------+
| Navigate   | * **str**            |                         |
+------------+----------------------+-------------------------+
| Pattern    | * **str**            |                         |
+------------+----------------------+-------------------------+
| Protocol   | * **str**            |                         |
+------------+----------------------+-------------------------+
| PutHeaders | * **Dict[str: str]** |                         |
+------------+----------------------+-------------------------+



Response
-------------------------------------
Provides a 201 successful created code in case the model entity has been successfully inserted, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html#sec9.5 in case
of creation problems a 400 code is provided with explanations about the problem.