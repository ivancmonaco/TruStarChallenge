ifneq (,$(wildcard ./.env))
    include .env
    export
endif

default:
	make start
	
start:
	pipenv run gunicorn -k gevent --bind ${HOST}:${PORT} 'main:start()' --chdir ./src -w 3 --worker-connections 1000

dev:
	(cd src; pipenv run python main.py)

test:
	(cd src; pipenv run python -m unittest discover)

types:
	pipenv run mypy src

lint:
	pipenv run black src