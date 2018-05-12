#!/usr/bin/env python
# Author: Volodymyr Flonts <flyonts@gmail.com>
# Version: 1.0 @ Sat May 12 20:48:28 EEST 2018
import re
import setuptools
import subprocess

setuptools_original_setup = setuptools.setup

def setup_with_git_branch(*args, **kwargs):
    branches = subprocess.check_output(['git', 'branch'])
    current = re.search(r'\* (\S+)', branches).group(1)
    branch = current.replace('_', '.').replace('-', '.')
    commit = subprocess.check_output(['git', 'log', '--pretty=%H'])[:7]
    kwargs['version'] += '.' if '+' in kwargs['version'] else '+'
    kwargs['version'] += '{}.{}'.format(branch, commit)
    return setuptools_original_setup(*args, **kwargs)

setuptools.setup = setup_with_git_branch

__file__ = 'setup.py'
exec open(__file__).read()
