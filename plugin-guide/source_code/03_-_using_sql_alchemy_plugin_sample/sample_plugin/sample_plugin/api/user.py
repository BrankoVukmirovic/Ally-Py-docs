'''
Created on Mar 29, 2012

@package: simple plugin sample
@copyright: 2011 Sourcefabric o.p.s.
@license: http://www.gnu.org/licenses/gpl-3.0.txt
@author: Gabriel Nistor

The API descriptions for user sample.
'''

from ally.api.config import service, call
from ally.api.type import Iter
from sample_plugin.api import modelSample

# --------------------------------------------------------------------

@modelSample(id='Id')
class User:
    '''
    The user model.
    '''
    Id = int
    Name = str

# --------------------------------------------------------------------

@service
class IUserService:
    '''
    The user service.
    '''
    
    @call
    def getUsers(self) -> Iter(User):
        '''
        Provides all the users.
        '''
    
    @call
    def insert(self, user:User) -> User.Id:
        '''
        Persist the user model.
        '''
