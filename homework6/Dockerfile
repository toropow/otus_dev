#Build image:
#docker build -t hw5 .
#Run service:
#docker run --rm -it -p 5000:5000 hw5

FROM python:3.7-buster
MAINTAINER toropow@gmail.com

WORKDIR /app

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH="${PATH}:/root/.poetry/bin"
RUN poetry config virtualenvs.create false

COPY olympiad/poetry.lock olympiad/pyproject.toml ./

RUN poetry install --no-interaction --no-ansi

COPY olympiad /app

EXPOSE 5000

CMD gunicorn --bind  0.0.0.0:5000 --workers 2 main:app
