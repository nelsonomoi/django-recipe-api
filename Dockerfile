FROM python:3.7-alpine

LABEL  maintenaner='OMOI NELSON NYACHOTI'
LABEL version='0.0.1'

ENV PYTHONUNBEFFERED 1

COPY ./requirements.txt /requirements.text

RUN pip install -r /requirements.txt 


RUN mkdir /app
WORKDIR /app
COPY ./app /app


RUN adduser user 
USER user