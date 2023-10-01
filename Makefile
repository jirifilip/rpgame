.poetry_installed:
	poetry install
	touch .poetry_installed


test: .poetry_installed
	poetry run pytest -vvv -s


pre-commit: .poetry_installed
	poetry run pre-commit --all-files
