django-shop-richproduct
=======================

Provides rich product functionality for the django shop application.

[![Build Status](https://travis-ci.org/nimbis/django-shop-richproduct.svg?branch=master)](https://travis-ci.org/nimbis/django-shop-richproduct)

[![Coverage](https://coveralls.io/repos/nimbis/django-shop-richproduct/badge.png?branch=master)](https://coveralls.io/r/nimbis/django-shop-richproduct?branch=master)


Requirements
------------

* django < 1.8
* django-cms
* django-shop


Installation
------------

* Run `pip install django-shop-richproduct` or download this package and run `python setup.py install`

* Ensure that `django_shop_richproduct` is in your INSTALLED APPS

* Run `syncdb` or `migrate django_shop_richproduct` if you have South installed.

History
-------

v1.1.0:

	* Added purchase_button_label field to the RichProduct model to allow
	  products to customize this button text on an individual basis.

v1.0.0:

    * Django 1.7 is now supported.

v0.2.5:

    * Removing pip requirement from setup.py.

v0.1.0:

    * Initial version.
