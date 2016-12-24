#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup

def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname), "r") as f:
        return f.read()

setup(
    name = "fontawesome",
    version = "0.1",
    author = "Davide Depau",
    author_email = "davide@depau.eu",
    description = ("A simple module to insert FontAwesome unicode characters to strings."),
    license = "MIT",
    keywords = "fontawesome unicode",
    url = "http://github.com/Davideddu/python-fontawesome",
    packages=['fontawesome'],
    long_description=read('README.md'),
    requires=["future"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
)
