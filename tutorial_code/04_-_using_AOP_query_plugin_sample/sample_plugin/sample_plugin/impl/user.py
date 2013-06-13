'''
Created on Mar 29, 2012

@package: simple plugin sample
@copyright: 2011 Sourcefabric o.p.s.
@license: http://www.gnu.org/licenses/gpl-3.0.txt
@author: Gabriel Nistor

Simple implementation for the user APIs.
'''

from ally.support.sqlalchemy.session import SessionSupport
from sample_plugin.api.user import IUserService, QUser
from sample_plugin.meta.user import User
from ally.container.ioc import injected
from ally.container.support import setup
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql.expression import desc
from sqlalchemy.sql.operators import like_op
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
    
    def getUsers(self, offset=None, limit=None, q=None):
        '''
        @see: IUserService.getUsers
        '''
        sql = self.session().query(User)
        if q:
            if QUser.name.like in q:
                sql = sql.filter(like_op(User.Name, q.name.like))
            if QUser.name.ascending in q:
                sql = sql.order_by(User.Name if q.name.ascending else desc(User.Name))
        if offset: sql = sql.offset(offset)
        if limit: sql = sql.limit(limit)
        return sql.all()
        
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
