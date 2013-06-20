'''
Created on Mar 30, 2012

@package: example user
@copyright: 2013 Sourcefabric o.p.s.
@license: http://www.gnu.org/licenses/gpl-3.0.txt
@author: Gabriel Nistor

Mapping for the user model.
'''

from example.user.api.user import User
from example.user.meta.user_type import UserTypeMapped
from ally.support.sqlalchemy.mapper import validate
from sqlalchemy.dialects.mysql.base import INTEGER
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import String
from example.meta.metadata_example import Base

# --------------------------------------------------------------------

@validate
class UserMapped(Base, User):
    __tablename__ = 'user'
    __table_args__ = dict(mysql_engine='InnoDB', mysql_charset='utf8')

    Id = Column('id', INTEGER(unsigned=True), primary_key=True)
    Name = Column('name', String(20), nullable=False)
    Type = Column('fk_user_type', ForeignKey(UserTypeMapped.Id, ondelete='RESTRICT'), nullable=False)

