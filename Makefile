.PHONY: install test clean

VENV := .venv
PY := $(VENV)/bin/python
PIP := $(PY) -m pip

install:
	@echo "🔧 Performing initial setup for development..."
	@echo "🔧 Creating virtual environment if needed..."
	@test -d $(VENV) || python3 -m venv $(VENV)
	@echo "✅ Virtual environment is ready."
	$(PIP) install -U pip
	$(PIP) install -r requirements.txt
	$(PY) -m playwright install --with-deps

test:
# 	$(PY) -m pytest -q
	$(PY) -m pytest -v

clean:
	rm -rf $(VENV) .pytest_cache **/__pycache__
