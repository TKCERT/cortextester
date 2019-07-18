all: Pipfile.lock dev-requirements.txt

Pipfile.lock: Pipfile
	pipenv lock --pre --dev

dev-requirements.txt: Pipfile Pipfile.lock
	pipenv lock --pre --dev --requirements > dev-requirements.txt

build: setup.py
	pipenv run python3 setup.py sdist bdist_wheel
