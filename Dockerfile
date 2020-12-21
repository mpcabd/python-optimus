FROM python:3.9-alpine

RUN apk add --no-cache gcc musl-dev libffi-dev python3-dev openssl openssl-dev

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade setuptools wheel pip twine tox

COPY . .

CMD tox -e py39
