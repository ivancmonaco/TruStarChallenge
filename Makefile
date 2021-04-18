default:
	make start
	
start:
	pipenv run gunicorn -k gevent --bind 0.0.0.0:4000 'main:start()' --chdir ./src -w 3 --worker-connections 1000

dev:
	(cd src; pipenv run python main.py)

test:
	(cd src; pipenv run python -m unittest discover)

types:
	pipenv run mypy src

lint:
	pipenv run black src