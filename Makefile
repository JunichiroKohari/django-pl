up:
	docker compose up

upd:
	docker compose up -d

down:
	docker compose down

shell:
	docker compose exec app bash

build:
	docker compose build

service=null
startproject:
	docker compose exec app python3 manage.py startproject ${service}

startapp:
	docker compose exec app python3 manage.py startapp ${service}

runserver:
	docker compose exec app python3 manage.py runserver 0.0.0.0:8000

makemigrations:
	docker compose exec app python3 booklist/manage.py makemigrations

migrate:
	docker compose exec app python3 manage.py migrate

createsuperuser:
	docker compose exec app python3 manage.py createsuperuser

test:
	docker compose exec app pytest

test-cov:
	docker compose exec app pytest --cov .