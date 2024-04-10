FROM python:3.11

WORKDIR /src

COPY requirements.txt requirements-dev.txt ./
RUN pip install -r requirements.txt