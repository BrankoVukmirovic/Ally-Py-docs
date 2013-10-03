.. _model:

**ACL/Filter**
==========================================================

Python model path: ``acl.api.filter.Filter``

**Description**

Contains data required for an ACL filter.
    Path -       contains the path that the filter maps to. The path contains beside the fixed string
                 names also markers '*' for where the filtered values or injected values will be placed.
    Hash -       the hash that represents the full aspect of the filter.
    Signature -  the type signature associated with the target path entry.

**Properties**

==== ==================== ====================
Id   Name                 Type
==== ==================== ====================
\*   Name                 str
\    Path                 str
\    Signature            str
==== ==================== ====================