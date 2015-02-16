#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
        name = 'pullword',
        version = '0.0.1',
        keywords = ('pullword'),
        description = 'the sdk for pullword.com -- a free online Chinese text segmentation platform',
        license = 'MIT License',
        install_requires = ['requests>=1.0.0'],
        author = 'binhe22',
        packages = find_packages(),
        platforms = 'any',
    )
