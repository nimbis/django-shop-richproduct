from setuptools import setup
from pip.req import parse_requirements

# parse requirements
reqs = parse_requirements("requirements/common.txt")

# setup the project
setup(
    name="django-shop-richproduct",
    version="0.0.1",
    author="Nimbis Services, Inc.",
    author_email="info@nimbisservices.com",
    description="Rich product functionality for django shop.",
    license="BSD",
    packages=['shop_richproduct'],
    install_requires=[str(x).split(' ')[0] for x in reqs],
    zip_safe=False,
    include_package_data=True,
    test_suite="tests.main",
)
