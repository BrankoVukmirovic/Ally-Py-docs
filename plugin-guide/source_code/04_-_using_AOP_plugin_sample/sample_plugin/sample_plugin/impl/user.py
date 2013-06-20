'''
Created on Mar 29, 2012

@package: simple plugin sample
@copyright: 2011 Sourcefabric o.p.s.
@license: http://www.gnu.org/licenses/gpl-3.0.txt
@author: Gabriel Nistor

Simple implementation for the user APIs.
'''

from sample_plugin.api.user import IUserService
from ally.support.sqlalchemy.session import SessionSupport
from ally.container.ioc import injected
from ally.container.support import setup
from sample_plugin.meta.user import User
from sqlalchemy.exc import SQLAlchemyError
import logging

# --------------------------------------------------------------------

log = logging.getLogger(__name__)

# --------------------------------------------------------------------

@injected
@setup(IUserService, name='userService')
class UserService(IUserService, SessionSupport):
    '''
    Implementation for @see: IUserService
    '''
    
    def getUsers(self):
        '''
        @see: IUserService.getUsers
        '''
        return self.session().query(User).all()
        
    def insert(self, user):
        '''
        @see: IUserService.insert
        '''
        mapped = User()
        if User.Name in user: mapped.Name = user.Name
        try:
            self.session().add(mapped)
            self.session().flush((mapped,))
        except SQLAlchemyError:
            log.exception('Could not insert %s' % user)
        return mapped.Id