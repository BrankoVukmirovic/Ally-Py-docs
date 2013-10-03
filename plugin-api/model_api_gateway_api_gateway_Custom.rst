.. _model:

**Gateway/Custom**
==========================================================

Python model path: ``gateway.api.gateway.Custom``

**Description**

Provides the custom defined gateway.
    Name -      the unique name for the gateway.

**Properties**

==== ==================== ====================
Id   Name                 Type
==== ==================== ====================
\*   Name                 str
\    Clients              List[str]
\    Errors               List[int]
\    Exclude              List[str]
\    Filters              List[str]
\    Headers              List[str]
\    Host                 str
\    Methods              List[str]
\    Navigate             str
\    Pattern              str
\    Protocol             str
\    PutHeaders           Dict[str: str]
==== ==================== ====================