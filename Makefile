.PHONY: venv install test style all_tests

venv:
	virtualenv -p python3.6 .venv
	. .venv/bin/activate
	pip install -r requirements.txt

install:
	pip install -r requirements.txt

test:
	pytest -v tests/

style:
	flake8 --max-line-length=100 src

all_tests: style test




