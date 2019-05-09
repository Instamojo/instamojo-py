#!/usr/bin/env python

import ast
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def generate_long_description():
    with open('README.md') as f:
        long_description = f.read()
        try:
            import pypandoc
            long_description = pypandoc.convert_text(
                long_description, 'rst', format='md')
        except ImportError:
            pass
        return long_description

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('instamojo_wrapper/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name="instamojo_wrapper",
    version=version,
    description="Instamojo API 1.1 Wrapper",
    long_description=generate_long_description(),
    author="Instamojo Developers",
    author_email="support@instamojo.com",
    license="MIT",
    url="http://github.com/Instamojo/instamojo-py",
    keywords=["instamojo", "api", "wrapper", "1.1"],
    include_package_data=True,
    packages=["instamojo_wrapper"],
    install_requires=[
        "requests",
    ],
    classifiers=(
        "Development Status :: 4 - Beta",
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ),
)
