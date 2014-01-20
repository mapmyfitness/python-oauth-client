#!/usr/bin/env python

from setuptools import setup
import sys

if 'sdist' in sys.argv:
    import mmf_release_tools
    version = mmf_release_tools.generate_release_version('0.1', __file__)
    mmf_release_tools.write_release_version(version)
else:
    with open("RELEASE-VERSION", "r") as f:
        version = f.readlines()[0].strip()

setup(
    name = 'oauth-client',
    version = version,
    packages = ['oauth_client', 'oauth_client.adapter'],

    author = 'Lann Martin',
    author_email = 'oauth-client@lannbox.com',
    description = 'client library for OAuth 1.0',
    license = 'MIT',
    url = 'http://github.com/lann/python-oauth-client',

    test_suite = 'tests',
    tests_require = 'mock',
    )
