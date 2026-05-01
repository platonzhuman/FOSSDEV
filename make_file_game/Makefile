.PHONY: venv install run test typecheck lint format check-requirements check clean

PYTHON = .venv/bin/python
PIP = .venv/bin/pip

venv:
	python3 -m venv .venv

install: venv
	$(PIP) install -r requirements-dev.txt

run:
	$(PYTHON) src/krest_nole.py

test:
	$(PYTHON) -m pytest tests/tests_krest_nole.py

typecheck:
	$(PYTHON) -m mypy src/ --ignore-missing-imports

lint:
	$(PYTHON) -m ruff check src/ tests/

format:
	$(PYTHON) -m ruff format src/ tests/

check-requirements:
	$(PYTHON) src/script.py

check: typecheck lint check-requirements

clean:
	rm -rf __pycache__ .mypy_cache .ruff_cache dist build *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +