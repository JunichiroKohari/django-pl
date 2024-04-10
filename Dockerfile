FROM python:3.11

WORKDIR /src

COPY requirements.txt ./
COPY requirements-dev.txt ./
RUN pip install -r requirements.txt