
.PHONY: db test pep8 clean doc check-venv check-venv

# clean out potentially stale pyc files
clean:
	@find . -name "*.pyc" -exec rm {} \;

# check that virtualenv is enabled
check-venv:
ifndef VIRTUAL_ENV
	$(error VIRTUAL_ENV is undefined, try "workon" command)
endif

# Install pip requirements.txt file
reqs: check-venv
	pip install -r requirements.txt

# Show all occurence of same error
# Exclude the static directory, since it's auto-generated
PEP8_OPTS=--repeat --exclude=static,migrations,south_migrations,js,doc --show-source

pep8: check-venv
	python setup.py pep8 $(PEP8_OPTS)

#
# flake8
#

FLAKE8_OPTS = --max-complexity 10 --exclude='doc,migrations,south_migrations'
flake8: check-venv
	flake8 $(FLAKE8_OPTS) .

test: check-venv clean
	python manage.py test

#
# doc
#

doc:
	cd doc; make html
	@echo "See ./doc/_build/index.html for html documentation."

#
# code coverage
#

COVERAGE_INCLUDE='shop_richproduct/*'

coverage:
	coverage erase
	-coverage run --include=$(COVERAGE_INCLUDE) ./manage.py test
	coverage report
	coverage html
	@echo "See ./htmlcov/index.html for coverage report"
