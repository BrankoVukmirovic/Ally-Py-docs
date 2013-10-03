.. _model:

**ACL/Entry**
==========================================================

Python model path: ``acl.api.access.Entry``

**Description**

The path entry that corresponds to a '*' dynamic path input.
    Position -           the position of the entry in the access path.
    Shadowing -          the position that this entry is shadowing.
    Shadowed -           the position of the shadowed entry, also it means that the values belonging to it 
                         will not be actually used by the access path request.
    Signature -          the type signature associated with the path entry.

**Properties**

==== ==================== ====================
Id   Name                 Type
==== ==================== ====================
\*   Position             int
\    Shadowed             int
\    Shadowing            int
\    Signature            str
==== ==================== ====================