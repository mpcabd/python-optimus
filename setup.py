#!/usr/bin/env python
# coding=utf-8

import os

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="python-optimus",
    version="1.0.1",
    author="Abdullah Diab",
    author_email="mpcabd@gmail.com",
    maintainer="Abdullah Diab",
    maintainer_email="mpcabd@gmail.com",
    description="Transform internal id's to "
                "obfuscated integers using Knuth's integer hash",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mpcabd/python-optimus",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    platforms="ALL",
    license="MIT",
    keywords="hashing hashids optimus knuth",
)
