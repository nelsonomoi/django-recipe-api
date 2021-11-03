FROM python:3.7-alpine

LABEL  maintenaner='OMOI NELSON NYACHOTI'
LABEL version='0.0.1'

ENV PYTHONUNBEFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt 
RUN pip install --upgrade pip


RUN mkdir /app
WORKDIR /app
COPY ./app /app


