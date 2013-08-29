#!/usr/bin/env python

import sys
import os

base_location = os.path.abspath(os.path.dirname(__file__))

requirements = 'REQUIREMENTS'
requirements_links = 'REQUIREMENTS_LINKS'

def filter_comments(fd):
    return filter(lambda l: l.strip().startswith("#") is False, fd.readlines())

def readfile(filename, func):
    try:
        with open(os.path.join(base_location, filename)) as f:
            data = func(f)
    except (IOError, IndexError):
        sys.stderr.write(u"""
Can't find '%s' file. This doesn't seem to be a valid release.
""" % filename)
        sys.exit(1)
    return data

def get_requires():
    return readfile(requirements, filter_comments)

def get_dependencies():
    return readfile(requirements_links, filter_comments)
