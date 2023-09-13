PWD = $(shell pwd)

check:
	flake8
	ruff check .
	pytest
	black --check .

lint:
	black pyshadowserver
	black tests

clean:
	rm -rf $(PWD)/build $(PWD)/dist $(PWD)/pyshadowserver.egg-info

dist:
	python3 setup.py sdist bdist_wheel

upload:
	python3 -m twine upload dist/*

test:
	pytest
