#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    long_description = readme.read()

setup(
    name='html2rml',
    version='0.2.0',
    description='Simple HTML to RML converter',
    long_description=long_description,
    author='Jakub Dorňák',
    author_email='jakub.dornak@misli.cz',
    license='BSD',
    url='https://github.com/misli/html2rml',
    py_modules=['html2rml'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 2.7',
    ],
)
