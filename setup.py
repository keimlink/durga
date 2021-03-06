#!/usr/bin/env python
# -*- coding: utf-8 -*-
from codecs import open

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

dev_requires = [
    'bumpversion==0.5.1',
    'pdbpp==0.7.2',
]

docs_requires = [
    'Sphinx==1.3b3',
    'doc8==0.5.0',
]

requires = [
    'schema>=0.3.1',
    'requests>=2.5.0',
]

tests_requires = [
    'httpretty>=0.8.0,!=0.8.1,!=0.8.2,!=0.8.3,!=0.8.7',
    'pytest-cov==1.8.1',
    'pytest-flakes==0.2',
    'pytest-httpretty==0.2.0',
    'pytest-pep8==1.0.6',
    'pytest==2.6.4',
    'six==1.9.0',
    'tox==1.9.0',
]

setup(
    name='durga',
    version='0.2.0.dev0',
    description='Create easy to use Python objects for REST resources including schema validation.',  # noqa
    long_description=readme,
    author='transcode',
    author_email='team@transcode.de',
    url='https://github.com/transcode-de/durga',
    packages=[
        'durga',
    ],
    package_dir={'durga': 'durga'},
    include_package_data=True,
    install_requires=requires,
    extras_require={
        'dev': dev_requires,
        'docs': docs_requires,
        'tests': tests_requires,
    },
    license='BSD',
    zip_safe=False,
    keywords='rest api json client schema validation',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
