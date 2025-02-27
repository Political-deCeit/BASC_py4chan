#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""4chan Python Library.

BASC-py4chan is a Python library that gives access to the 4chan API
and an object-oriented way to browse and get board and thread
information quickly and easily.

This program is free software. It comes without any warranty, to
the extent permitted by applicable law. You can redistribute it
and/or modify it under the terms of the Do What The Fuck You Want
To Public License, Version 2, as published by Sam Hocevar. See
the LICENSE file for more details.
"""

from setuptools import setup

setup(
    name='BASC-py4chan',
    version='1.0.1',
    description=("Python 4chan API Wrapper. Improved version of Edgeworth's "
                 "original py-4chan wrapper."),
    license=open('LICENSE').read(),
    author='r',
    author_email='',
    url='https://github.com/Political-deCeit/BASC_py4chan',
    packages=['basc_py4chan'],
    package_dir={
        'basc_py4chan': 'basc_py4chan',
    },
    package_data={'': ['LICENSE']},
    install_requires=['requests >= 1.0.0'],
    keywords='4chan api',
)
