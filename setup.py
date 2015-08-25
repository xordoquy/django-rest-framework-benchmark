#!/usr/bin/env python
"""
drf_bench
=====

"""

import drf_bench
from setuptools import setup, find_packages
import sys

install_requires = [
    "Django==1.8.4",
    "djangorestframework==3.2.3",
]

dev_requires = [
    'django-debug-toolbar',
]

test_requires = [
    "pytest",
    "pytest-cov",
    "pytest-django",
]


setup(
    name="drf_bench",
    version=drf_bench.__version__,
    author="Xavier Ordoquy",
    author_email="xordoquy@linovia.com",
    url="",
    description="A benchmark for Django REST framework.",

    # Packages and data to take into account
    packages=find_packages(exclude=("tests", "tests.*")),
    include_package_data=True,

    zip_safe=False,  # Avoid eggs

    # Allow pip install .[tests,dev] to install the dev and test dependencies
    extras_require={
        "tests": test_requires,
        "dev": dev_requires,
    },
    install_requires=install_requires,
    tests_require=test_requires,
)
