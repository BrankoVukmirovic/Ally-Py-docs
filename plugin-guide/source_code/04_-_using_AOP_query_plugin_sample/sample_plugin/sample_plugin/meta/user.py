'''
Created on Mar 30, 2012

@package: simple plugin sample
@copyright: 2011 Sourcefabric o.p.s.
@license: http://www.gnu.org/licenses/gpl-3.0.txt
@author: Gabriel Nistor

Mapping for the user model.
'''

from ally.support.sqlalchemy.mapper import mapperModel
from sample_plugin.api.user import User
from sample_plugin.meta import meta
from sqlalchemy.schema import Table, Column
from sqlalchemy.types import String, Integer

# --------------------------------------------------------------------

table = Table('sample_user', meta,
               Column('id', Integer, primary_key=True, key='Id'),
               Column('name', String(20), nullable=False, key='Name'))

# map User entity to defined table (above)
User = mapperModel(User, table)
