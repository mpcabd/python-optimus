# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['optimus_id']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'optimus-id',
    'version': '0.2.2',
    'description': "Transform internal id's to obfuscated integers using Knuth's integer hash",
    'long_description': None,
    'author': 'gazorby',
    'author_email': 'gazorby@pm.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
