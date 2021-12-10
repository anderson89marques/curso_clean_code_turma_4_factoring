export PYTHONDONTWRITEBYTECODE=1

.PHONY=help

help:  ## This help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

clean:  ## Remove cache files
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf


###
# Dependencies section
###
_base-pip:
	@pip install -U pip poetry wheel

dev-dependencies: _base-pip  ## Install development dependencies
	@poetry install

dependencies: _base-pip  ## Install dependencies
	@poetry install --no-dev

outdated:  ## Show outdated packages
	@poetry show --outdated

test: clean
	@poetry run pytest

test-coverage: clean  ## Run tests with coverage output
	@poetry run pytest tests/ --cov refactor/ --cov-report term-missing --cov-report html