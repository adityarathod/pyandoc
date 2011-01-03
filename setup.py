#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from setuptools import setup


def publish():
	"""Publish to PyPi"""
	os.system("python setup.py sdist upload")

if sys.argv[-1] == "publish":
	publish()
	sys.exit()

required = []

# if sys.version_info < (2, 6):
# 	required.append('simplejson')

setup(
	name='pyandoc',
	version='0.0.1',
	description='Python wrapper for Pandoc - the universal document converter',
	long_description=open('README.rst').read() + '\n\n' +
	                 open('HISTORY.rst').read(),
	author='Kenneth Reitz',
	author_email='me@kennethreitz.com',
	url='http://github.com/kennethreitz/pyandoc',
	packages= [
		'pandoc',
	],
	install_requires=required,
	license='MIT',
	classifiers=(
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
		'Natural Language :: English',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python',
        # 'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7',
		# 'Programming Language :: Python :: 3.0',
		# 'Programming Language :: Python :: 3.1',
	),
    # entry_points={
    #   'console_scripts': [
    #       'tabbed = tablib.cli:start',
    #   ],
    # }
)
