FROM python:3.10

RUN pip install --upgrade pip

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy project
COPY . /usr/src/app

# install dependencies
COPY req.txt ./
RUN pip install -r req.txt

RUN python manage.py migrate