FROM python:3.7.12-slim-buster
LABEL maintainer="teaflex.dev@hotmail.com"

RUN apt update -y && apt upgrade -y

RUN apt install -y procps curl
RUN pip3 install pipenv

COPY . /delicioso
WORKDIR /delicioso
RUN ["rm", "-rf", "dev.env", "Dockerfile"]
RUN ["pipenv", "install"]

EXPOSE 8000

ENTRYPOINT ["pipenv", "run", "serve"]