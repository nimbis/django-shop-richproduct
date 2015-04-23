#!/usr/bin/env python

from setuptools import setup, find_packages

# setup the project
setup(
    name="django-shop-richproduct",
    version="1.0.0",
    author="Nimbis Services, Inc.",
    author_email="info@nimbisservices.com",
    description="Rich product functionality for django shop.",
    license="BSD",
    packages=find_packages(exclude=["tests", ]),
    install_requires=[
        'Django',
        'django-shop >= 0.2.0',
        'image',
        'django-cms',
        'django-treebeard',
    ],
    zip_safe=False,
    include_package_data=True,
)
