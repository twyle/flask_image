install-dev:
	@pip install -r requirements-dev.txt

install-reqs:
	@pip install -r requirements.txt

build: clean
	@python setup.py sdist bdist_wheel

install:
	@pip uninstall flask-image -y
	@pip install dist/flask_image-0.1.0-py3-none-any.whl

clean:
	@rm -rf build dist flask_image.*

check-build:
	@twine check dist/*

test-upload:
	@twine upload --repository testpypi dist/*

upload:
	@twine upload dist/*

pre-commit:
	@pre-commit install

initial-tag:
	@git tag -a -m "Initial tag." v0.0.1

init-cz:
	@cz init

bump-tag:
	@cz bump --check-consistency --changelog

# build|ci|docs|feat|fix|perf|refactor|style|test|chore|revert|bump

lint:
	@black ./flask_image
	@isort ./flask_image
	@flake8 ./flask_image
	@mypy ./flask_image
	@pydocstyle  ./flask_image
	# @pylint --rcfile=.pylintrc ./flask_image

test:
	@python -m pytest