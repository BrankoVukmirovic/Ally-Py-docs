'''
Created on Jun 12, 2013

@package: example
@copyright: 2013 Sourcefabric o.p.s.
@license: http://www.gnu.org/licenses/gpl-3.0.txt
@author: Martin Saturka

Provides the database settings for the example database.
'''

from ally.container import ioc, support
from ally.container.binder_op import bindValidations
from ally.support.sqlalchemy.mapper import mappingsOf
from ally.support.sqlalchemy.session import bindSession
from sql_alchemy import database_config
from sql_alchemy.database_config import alchemySessionCreator, metas
from example.meta.metadata_example import meta

# --------------------------------------------------------------------

support.include(database_config)

# --------------------------------------------------------------------

@ioc.replace(database_url)
def database_url():
    '''This database URL is used for the example tables'''
    return 'sqlite:///workspace/shared/example.db'

@ioc.before(metas)
def updateMetasForExample(): metas().append(meta)

# --------------------------------------------------------------------

def bindExampleSession(proxy): bindSession(proxy, alchemySessionCreator())
def bindExampleValidations(proxy): bindValidations(proxy, mappingsOf(meta))
