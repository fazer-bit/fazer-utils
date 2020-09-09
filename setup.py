#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

__version__ = "0.1.0"
URL = "https://github.com/fazer-bit/fazer-utils.git"

setup(
    name="fazer-utils",
    version=__version__,
    description="Python library for Timers",
    long_description=open("README.md").read(),
    author="fazer-bit",
    author_email="git-dotcom@mail.ru",
    url=URL,
    keywords=["timers", "library"],
    packages=["timers"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "Topic :: Office/Business :: Financial",
    ],
    # install_requires=open("requirements.txt").readlines(),
    # setup_requires=["pytest-runner"],
    include_package_data=True,
)

