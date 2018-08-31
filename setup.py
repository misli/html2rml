#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import setup


setup(
    name='html2rml',
    version='0.1.0',
    description='Simple HTML to RML converter',
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
