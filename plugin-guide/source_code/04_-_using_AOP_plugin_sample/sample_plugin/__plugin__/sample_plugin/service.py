'''
Created on Mar 29, 2012

@package: simple plugin sample
@copyright: 2011 Sourcefabric o.p.s.
@license: http://www.gnu.org/licenses/gpl-3.0.txt
@author: Gabriel Nistor

Contains the services setups.
'''

from __plugin__.plugin.registry import addService
from __plugin__.sample_plugin.db_sample import alchemySessionCreator
from ally.container import support
from ally.support.sqlalchemy.session import bindSession

# --------------------------------------------------------------------

API, IMPL = 'sample_plugin.api.**.I*Service', 'sample_plugin.impl.**.*'

support.createEntitySetup(API, IMPL)

def bindSampleSession(proxy): bindSession(proxy, alchemySessionCreator())
support.listenToEntities(IMPL, listeners=addService(bindSampleSession,))

support.loadAllEntities(API)
