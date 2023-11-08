# FIXME: https://github.com/pypa/pip/issues/11440
deps:
	pip install .[dev]
	pip uninstall -y teamcity-messages-extra
