'''
Created on Mar 29, 2012

@package: example user
@copyright: 2013 Sourcefabric o.p.s.
@license: http://www.gnu.org/licenses/gpl-3.0.txt
@author: Gabriel Nistor

The API descriptions for user sample.
'''

from ally.api.config import service, query, call
from ally.api.criteria import AsLikeOrdered
from ally.api.type import Iter
from example.api.domain_example import modelExample
from example.user.api.user_type import UserType
from ally.support.api.entity import Entity, QEntity, IEntityService

# --------------------------------------------------------------------

@modelExample
class User(Entity):
    '''
    The user model.
    '''
    Name = str
    Type = UserType

# --------------------------------------------------------------------

@query(User)
class QUser(QEntity):
    '''
    The user model query object.
    '''
    name = AsLikeOrdered

# --------------------------------------------------------------------

@service((Entity, User), (QEntity, QUser))
class IUserService(IEntityService):
    '''
    The user service.
    '''

    @call
    def getUsersByType(self, typeId:UserType.Id, offset:int=None, limit:int=None, q:QUser=None) -> Iter(User):
        '''
        Provides the users that have the specified type id.
        '''
