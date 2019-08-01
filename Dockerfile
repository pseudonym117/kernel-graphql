FROM python:alpine3.7

ENV FLASK_APP=/app/src/kernel-graphql
EXPOSE 5000

RUN pip install pipenv

WORKDIR /app
COPY ./Pipfile* /app/

RUN pipenv install --ignore-pipfile

COPY ./src /app/src

CMD pipenv run flask run --host=0.0.0.0
