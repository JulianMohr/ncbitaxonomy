.PHONY: develop

PYTHON ?= python3

IN_VENV=. ./venv/bin/activate
venv/bin/activate:
	test -d venv || virtualenv venv --python=$(PYTHON)
	${IN_VENV} && pip install pip --upgrade
	${IN_VENV} && pip install -r requirements.txt

develop: venv/bin/activate
	${IN_VENV} && python setup.py develop

test: venv/bin/activate
#   ${IN_VENV} && pip install flake8 flake8-rst-docstrings flake8-docstrings flake8-import-order
#	${IN_VENV} && flake8 ncbitaxonomy \
#		--import-order-style google --application-import-names ncbitaxonomy \
#		--statistics
	# demo should run without error
	${IN_VENV} && python test.py

IN_BUILD=. ./pypi_build/bin/activate
pypi_build/bin/activate:
	test -d pypi_build || virtualenv pypi_build --python=python3 --prompt "(pypi) "
	${IN_BUILD} && pip install pip --upgrade
	${IN_BUILD} && pip install --upgrade pip setuptools twine wheel readme_renderer[md] keyrings.alt

.PHONY: sdist
sdist: clean pypi_build/bin/activate
	${IN_BUILD} && python setup.py sdist
	${IN_BUILD} && pip install dist/*.tar.gz
	${IN_BUILD} && python -c "import ncbitaxonomy"

.PHONY: clean
clean:
	rm -rf __pycache__ dist build venv ete3.egg-info tmp docs/_build

