'''
Created on Mar 29, 2012

@package: example user
@copyright: 2013 Sourcefabric o.p.s.
@license: http://www.gnu.org/licenses/gpl-3.0.txt
@author: Gabriel Nistor

Simple implementation for the user APIs.
'''

from example.user.api.user import IUserService, QUser
from example.user.meta.user import UserMapped
from sql_alchemy.impl.entity import EntityServiceAlchemy
from ally.container.ioc import injected
from ally.container.support import setup

# --------------------------------------------------------------------

@injected
@setup(IUserService, name='userService')
class UserServiceAlchemy(EntityServiceAlchemy, IUserService):
    '''
    Implementation for @see: IUserService
    '''

    def __init__(self):
        EntityServiceAlchemy.__init__(self, UserMapped, QUser)

    def getUsersByType(self, typeId, offset=None, limit=None, q=None):
        '''
        @see: IUserService.getUsersByType
        '''
        return self._getAll(UserMapped.Type == typeId, q, offset, limit)

