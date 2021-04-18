FROM python:3.8

RUN python -m pip install --upgrade pip
RUN pip3 install pipenv

WORKDIR /TruSTAR
COPY Pipfile /TruSTAR
COPY Pipfile.lock /TruSTAR

RUN pipenv install --pre

COPY . /TruSTAR