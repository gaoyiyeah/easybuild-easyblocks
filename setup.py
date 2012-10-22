import os
import sys
from distutils import log

from easybuild.easyblocks import VERSION

API_VERSION = str(VERSION).split('.')[0]

# log levels: 0 = WARN (default), 1 = INFO, 2 = DEBUG
log.set_verbosity(1)

try:
    from setuptools import setup
    log.info("Installing with setuptools.setup...")
except ImportError, err:
    log.info("Failed to import setuptools.setup, so falling back to distutils.setup")
    from distutils import setup

# Utility function to read README file
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

log.info("Installing version %s (required versions: API >= %s)" % (VERSION, API_VERSION))

setup(
    name = "easybuild-easyblocks",
    version = str(VERSION),
    author = "EasyBuild community",
    author_email = "easybuild@lists.ugent.be",
    description = """EasyBuild is a software installation framework in Python that allows you to install software \
in a structured and robust way. 
This package contains a collection of easyblocks, i.e. Python modules which implement support for installing \
particular (groups of) software packages with EasyBuild.""",
    license = "GPLv2",
    keywords = "software build building installation installing compilation HPC scientific",
    url = "http://hpcugent.github.com/easybuild",
    packages = ["easybuild", "easybuild.easyblocks", "easybuild.easyblocks.generic"],
    package_dir = {"easybuild.easyblocks": "easybuild/easyblocks"},
    package_data = {'easybuild.easyblocks': ["[a-z0-9]/*.py"]},
    long_description = read("README.rst"),
    classifiers = [
                   "Development Status :: 5 - Production/Stable",
                   "Environment :: Console",
                   "Intended Audience :: System Administrators",
                   "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
                   "Operating System :: POSIX :: Linux",
                   "Programming Language :: Python :: 2.4",
                   "Topic :: Software Development :: Build Tools",
                  ],
    platforms = "Linux",
    provides = ["easybuild", "easybuild.easyblocks", "easybuild.easyblocks.generic"],
    install_requires = ["easybuild-framework >= %s.0" % API_VERSION]
)
