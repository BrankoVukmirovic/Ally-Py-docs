.. _model:

**ACL/Group**
==========================================================

Python model path: ``acl.api.group.Group``

**Description**

Defines the group of ACL access.
    Name -           the group unique name.
    IsAnonymous -    if true it means that the group should be delivered for anonymous access.
    Description -    a description explaining the group.

**Properties**

==== ==================== ====================
Id   Name                 Type
==== ==================== ====================
\*   Name                 str
\    Description          str
\    IsAnonymous          bool
==== ==================== ====================