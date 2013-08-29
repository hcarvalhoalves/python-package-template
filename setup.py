#!/usr/bin/env python
from setuptools import setup, find_packages

import requirements
import versioneer

versioneer.versionfile_source = 'src/mypackage/version.py'
versioneer.versionfile_build = 'mypackage/version.py'
versioneer.tag_prefix = '' # use if tags are like "1.2.0"
#versioneer.tag_prefix = 'mypackage-' # use if tags are like "mypackage-1.2.0"
versioneer.parentdir_prefix = 'mypackage-' # dirname like 'myproject-1.2.0'

setup(
    name="mypackage",
    author="Henrique Carvalho Alves",
    author_email="hcarvalhoalves@gmail.com",
    package_dir={'': 'src'},
    packages=find_packages('src'),
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    install_requires=requirements.get_requires(),
    dependency_links=requirements.get_dependencies(),
    include_package_data=True,
    zip_safe=False,
    test_suite = "mypackage.tests")
