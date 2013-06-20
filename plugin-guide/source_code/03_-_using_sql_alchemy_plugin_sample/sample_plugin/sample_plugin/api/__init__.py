'''
Created on Mar 29, 2012

@package: simple plugin sample
@copyright: 2011 Sourcefabric o.p.s.
@license: http://www.gnu.org/licenses/gpl-3.0.txt
@author: Gabriel Nistor

The package where all the api modules will be found.
'''

from functools import partial
from ally.api.config import model

# --------------------------------------------------------------------

modelSample = partial(model, domain='Sample')
