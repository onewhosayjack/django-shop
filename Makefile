.ONESHELL:

venv: venv/touchfile

venv/touchfile: requirements.txt
	test -d venv || virtualenv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/touchfile

test: venv
	. venv/bin/activate

clean:
	rm -rf venv
	find -iname "*.pyc" -delete

all: venv

.PLONY:run