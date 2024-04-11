# booklist

## purpose
just a test of django

## versions
:Python: 3.11
:Django: 4.2

## how to install and start up
Get codes from the repository, and prepare for docker-compose environment.

```bash
$ git clone https://github.com/JunichiroKohari/django-pl
$ cd booklist
$ docker compose run --rm booklist python manage.py migrate
$ docker compose up -d
$ open http://localhost:8000/
```

## development

### install to develop

1. check out
2. install modules with the following steps

```bash
$ cd booklist
$ python3.11 -m venv venv
$ source venv/bin/activate
(venv) $ pip install -e .
```