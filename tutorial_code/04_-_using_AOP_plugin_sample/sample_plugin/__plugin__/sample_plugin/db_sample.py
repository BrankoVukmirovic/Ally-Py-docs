'''
Created on Mar 30, 2012

@package: simple plugin sample
@copyright: 2011 Sourcefabric o.p.s.
@license: http://www.gnu.org/licenses/gpl-3.0.txt
@author: Gabriel Nistor

Contains the database setup for the samples.
'''

from ally.container import ioc
from sample_plugin.meta import meta
from sqlalchemy.engine import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm.session import sessionmaker

# --------------------------------------------------------------------

@ioc.config
def database_url():
    '''The database URL for the samples'''
    return 'sqlite:///sample.db'

@ioc.entity
def alchemyEngine() -> Engine:
    engine = create_engine(database_url())
    return engine

@ioc.entity
def alchemySessionCreator():
    return sessionmaker(bind=alchemyEngine())

@ioc.start
def createTables():
    meta.create_all(alchemyEngine())
