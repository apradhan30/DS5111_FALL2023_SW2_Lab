default:
	@cat makefile


env:
	python3 -m venv env
	. env/bin/activate && pip install -r requirements.txt


run:
	@python bin/clockdeco_param.py

.PHONY: test

test:
	pytest -vv test

lint:
	pip list
	pylint bin/perceptron.py
