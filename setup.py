#!/usr/bin/env python
from setuptools import setup, find_packages

import sys
import os

BASE_LOCATION = os.path.abspath(os.path.dirname(__file__))

VERSION_FILE = 'VERSION'
REQUIRES_FILE = 'REQUIREMENTS'
DEPENDENCIES_FILE = 'REQUIREMENTS_LINKS'

def filter_comments(fd):
    return filter(lambda l: l.strip().startswith("#") is False, fd.readlines())

def readfile(filename, func):
    try:
        with open(os.path.join(BASE_LOCATION, filename)) as f:
            data = func(f)
    except (IOError, IndexError):
        sys.stderr.write(u"""
Can't find '%s' file. This doesn't seem to be a valid release.

If you are working from a git clone, run:
    make describe
    setup.py develop

To build a valid release, run:
    make all

""" % filename)
        sys.exit(1)
    return data

def get_version():
    return readfile(VERSION_FILE, lambda f: f.read().strip())

def get_requires():
    return readfile(REQUIRES_FILE, filter_comments)

def get_dependencies():
    return readfile(DEPENDENCIES_FILE, filter_comments)

setup(
    name="mypackage",
    author="Henrique Carvalho Alves",
    author_email="hcarvalhoalves@gmail.com",
    package_dir={'': 'src'},
    packages=find_packages('src'),
    version=get_version(),
    install_requires=get_requires(),
    dependency_links=get_dependencies(),
    include_package_data=True,
    zip_safe=False,
    test_suite = "mypackage.tests")
