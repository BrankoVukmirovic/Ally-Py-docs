@require(model)
.. _model:

**@model['Name']**
==========================================================

Python model path: ``@model['API']``

**Description**

@model['Description']

**Properties**

==== ==================== ====================
Id   Name                 Type
==== ==================== ====================
@for prop in model['ModelProperty']['ModelProperty']:
@if prop['IsId']:
\*   \
@else:
\    \
@endif
@prop['Name'].ljust(20, ' ') @prop['Type']
@end
==== ==================== ====================