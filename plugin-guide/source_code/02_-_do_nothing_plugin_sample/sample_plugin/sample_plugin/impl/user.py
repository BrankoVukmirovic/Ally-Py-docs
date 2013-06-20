'''
Created on Mar 29, 2012

@package: simple plugin sample
@copyright: 2011 Sourcefabric o.p.s.
@license: http://www.gnu.org/licenses/gpl-3.0.txt
@author: Gabriel Nistor

Simple implementation for the user APIs.
'''

from sample_plugin.api.user import IUserService
from ally.container.ioc import injected
from ally.container.support import setup

# --------------------------------------------------------------------

@injected
@setup(IUserService, name='userService')
class UserService(IUserService):
    '''
    Implementation for @see: IUserService
    '''
    
    def getUsers(self):
        '''
        @see: IUserService.getUsers
        '''
        return []
