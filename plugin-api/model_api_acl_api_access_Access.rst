.. _model:

**ACL/Access**
==========================================================

Python model path: ``acl.api.access.Access``

**Description**

Contains data required for an ACL access.
    Id -         the id of the access.
    Path -       contains the path that the access maps to. The path contains beside the fixed string
                 names also markers '*' for where dynamic path elements are expected.
    Method -     the method name that this access maps to.
    Shadowing -  the access that this access is actually shadowing, this means that the access path is just a reroute
                 for the shadowing access.
    Shadowed -   the access that this access is shadowed, this means that this access is overridden by the shadow in
                 required cases.
    Priority -   the ACL priority when constructing gateways on it.
    Output -     the output type signature for access.
    Hash -       the hash that represents the full aspect of the access.

**Properties**

==== ==================== ====================
Id   Name                 Type
==== ==================== ====================
\*   Id                   int
\    Hash                 str
\    Method               str
\    Output               str
\    Path                 str
\    Priority             int
\    Shadowed             Access.Id
\    Shadowing            Access.Id
==== ==================== ====================