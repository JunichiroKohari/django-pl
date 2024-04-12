FROM library/python:3.11

COPY ./requirements.txt /tmp/
WORKDIR /tmp
RUN pip install -r requirements.txt

COPY . /src
WORKDIR /src/booklist

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
