.PHONY: test style-check style deps

test:
	uv run python -m pytest --cov

style-check:
	uv run black teamcity_extra tests --check
	uv run isort teamcity_extra tests --check

style:
	uv run black teamcity_extra tests
	uv run isort teamcity_extra tests

deps:
	uv sync --dev
