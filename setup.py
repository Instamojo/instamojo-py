#!/usr/bin/env python

import os
import sys

import instamojo

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'instamojo',
]

requires = ['requests']

setup(
    name='instamojo',
    version=instamojo.__version__,
    description='Instamojo API Wrapper.',
    long_description=open('README.md').read(),
    author='Instamojo Developers',
    author_email='dev@instamojo.com',
    url='https://www.instamojo.com/developers/',
    packages=packages,
    package_data={'': ['LICENSE']},
    package_dir={'instamojo': 'instamojo'},
    include_package_data=True,
    install_requires=requires,
    license=open('LICENSE').read(),
    zip_safe=False,
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ),
)
