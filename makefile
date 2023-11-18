default:
	@cat makefile


env:
	python3 -m venv env
	source env/bin/activate && pip install -r requirements.txt


run:
	@bin/clockdemo_param.py >/dev/null 2>&1

.PHONY: test

test:
	pytest -vv tests
