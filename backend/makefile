PYTHON=python3
PIP=pip
VENV_DIR=venv

venv:
	$(PYTHON) -m venv $(VENV_DIR)
	$(VENV_DIR)/bin/pip install -r requirements.txt


activate:
	source $(VENV_DIR)/bin/activate


install:
	$(PIP) install -r requirements.txt


migrate:
	$(PYTHON) manage.py migrate

runserver:
	$(PYTHON) manage.py runserver

build:
	$(PYTHON) -m venv $(VENV_DIR)
	. $(VENV_DIR)/bin/activate
	$(PIP) install -r requirements.txt
	$(PYTHON) manage.py migrate
	$(PYTHON) manage.py runserver

clean:
	rm -rf $(VENV_DIR)
	rm -rf *.pyc
	rm -rf __pycache__
