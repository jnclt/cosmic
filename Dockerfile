FROM python:3.10-slim-bullseye

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN mkdir -p /src
COPY . /src/
RUN pip install --editable /src


