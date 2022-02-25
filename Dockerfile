FROM python:3.7.12-slim-buster
LABEL maintainer="teaflex.dev@hotmail.com"

RUN apt update -y && apt upgrade -y

RUN apt install -y procps curl apache2
RUN service apache2 start
RUN pip3 install pipenv

COPY . /delicioso
WORKDIR /delicioso
RUN ["rm", "-rf", "dev.env", "Dockerfile"]
RUN ["pipenv", "install"]
RUN pipenv run set_admin
RUN pipenv run set_static

EXPOSE 8000

ENTRYPOINT service apache2 start && pipenv run serve