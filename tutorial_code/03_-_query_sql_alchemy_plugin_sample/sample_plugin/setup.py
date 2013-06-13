'''
Created on June 13, 2013

@package: sample plugin
@copyright: 2013 Sourcefabric o.p.s.
@license: http://www.gnu.org/licenses/gpl-3.0.txt
@author: Martin Saturka
'''

# --------------------------------------------------------------------

from setuptools import setup, find_packages

# --------------------------------------------------------------------

setup(
    name="sample_plugin",
    version="1.0",
    packages=find_packages(),
    install_requires=['ally_api >= 1.0', 'ally_core_sqlalchemy >= 1.0'],
    platforms=['all'],
    test_suite='test',
    zip_safe=True,

    # metadata for upload to PyPI
    author="Gabriel Nistor",
    author_email="gabriel.nistor@sourcefabric.org",
    description="Simple sample plugin",
    long_description='Simple sample management functionality (model, service)',
    license="GPL v3",
    keywords="Ally REST framework plugin example",
    url="http://www.sourcefabric.org/en/superdesk/", # project home page
)
