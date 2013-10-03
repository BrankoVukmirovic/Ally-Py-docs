.. _model:

**ACL/Compensate**
==========================================================

Python model path: ``acl.api.compensate.Compensate``

**Description**

Contains data required for an ACL access compensate.
    Access -     the access that is being compensated.
    Path -       contains the path that the access maps to. The path contains beside the fixed string
                 names also markers like {1}, {2} ... {n} which represent the positions from the compensated request
                 path where values need to be placed.
    Mapping -    the mapping of positions, as a key the compensating access position and as a value the corresponding
                 compensated access position.

**Properties**

==== ==================== ====================
Id   Name                 Type
==== ==================== ====================
\    Access               Access.Id
\    Mapping              Dict[int: int]
\    Path                 str
==== ==================== ====================