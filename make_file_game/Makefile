.PHONY: venv install run test typecheck lint format check-requirements check clean

PYTHON = .venv/bin/python
PIP = .venv/bin/pip

venv:
	python3 -m venv .venv

install: venv
	$(PIP) install -r requirements-dev.txt

run:
	$(PYTHON) src/krest_nole.py

