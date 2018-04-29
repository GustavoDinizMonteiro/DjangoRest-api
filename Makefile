init:
	pip install pipenv --upgrade
	pipenv install --dev --skip-lock

pep8:
	pipenv run flake8 --exclude comprAgendada/settings.py,migrations
