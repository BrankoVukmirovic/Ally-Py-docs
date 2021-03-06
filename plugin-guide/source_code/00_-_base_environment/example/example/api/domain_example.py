'''
Created on Jun 12, 2013

@package: example
@copyright: 2013 Sourcefabric o.p.s.
@license: http://www.gnu.org/licenses/gpl-3.0.txt
@author: Martin Saturka

Provides the decorator to be used by the models in the example domain.
'''

from functools import partial
from ally.api.config import model

# --------------------------------------------------------------------

DOMAIN_EXAMPLE = 'Example/'
modelExample = partial(model, domain=DOMAIN_EXAMPLE)

