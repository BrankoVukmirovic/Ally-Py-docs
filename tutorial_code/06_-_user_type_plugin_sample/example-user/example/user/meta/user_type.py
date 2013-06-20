'''
Created on Apr 9, 2012

@package: example user
@copyright: 2013 Sourcefabric o.p.s.
@license: http://www.gnu.org/licenses/gpl-3.0.txt
@author: Gabriel Nistor

Mapping for the user type model.
'''

from example.user.api.user_type import UserType
from ally.support.sqlalchemy.mapper import validate
from sqlalchemy.dialects.mysql.base import INTEGER
from sqlalchemy.schema import Column
from sqlalchemy.types import String
from example.meta.metadata_example import Base

# --------------------------------------------------------------------

@validate
class UserTypeMapped(Base, UserType):
    __tablename__ = 'user_type'
    __table_args__ = dict(mysql_engine='InnoDB', mysql_charset='utf8')

    Id = Column('id', INTEGER(unsigned=True), primary_key=True)
    Name = Column('name', String(20), nullable=False, unique=True)

