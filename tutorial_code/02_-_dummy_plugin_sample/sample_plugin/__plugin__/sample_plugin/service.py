'''
Created on Mar 29, 2012

@package: simple plugin sample
@copyright: 2011 Sourcefabric o.p.s.
@license: http://www.gnu.org/licenses/gpl-3.0.txt
@author: Gabriel Nistor

Contains the services setups.
'''

from __plugin__.plugin.registry import registerService
from ally.container import ioc
from sample_plugin.api.user import IUserService
from sample_plugin.impl.user import UserService

# --------------------------------------------------------------------

@ioc.entity
def userService() -> IUserService:
    b = UserService()
    return b

@ioc.start
def register():
    registerService(userService())