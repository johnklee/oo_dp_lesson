.PHONY: test lint dist

all: test lint

init:
	pip3 install -r requirements.txt

test: init
	pytest tests/
