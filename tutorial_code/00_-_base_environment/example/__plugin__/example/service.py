'''
Created on Jun 12, 2013

@package: example
@copyright: 2013 Sourcefabric o.p.s.
@license: http://www.gnu.org/licenses/gpl-3.0.txt
@author: Martin Saturka

Contains the services for superdesk.
'''

from ..plugin.registry import addService
from .db_example import bindExampleSession, bindExampleValidations
from ally.container import support, bind, ioc
from itertools import chain

# --------------------------------------------------------------------

SERVICES = 'example.*.api.**.I*Service'

# this provides the (start/rollback/commit) session processing
@ioc.entity
def binders(): return [bindExampleSession]

# this provides validation of input data against database structure and content
@ioc.entity
def bindersService(): return list(chain((bindExampleValidations,), binders()))

# inner binding; for implementation services together with alchemy database classes
bind.bindToEntities('example.*.impl.**.*Alchemy', binders=binders)
# inner binding; for implementation services
support.createEntitySetup('example.*.impl.**.*')
# outer binding; for API registering
support.listenToEntities(SERVICES, listeners=addService(bindersService))
# outer binding; assuring that all APIs are registered
support.loadAllEntities(SERVICES)

# --------------------------------------------------------------------
