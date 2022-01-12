FROM python:3.9
# set some useful envs
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# declare workdir
WORKDIR /code

# install poetry
RUN pip install -U pip
RUN pip install poetry

# copy the projectfile
COPY ./pyproject.toml 
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi

# snag yonder app
COPY . /code/api

# run that API

