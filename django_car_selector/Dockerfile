FROM python:3.10

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools wheel


# install dependencies
COPY req.txt ./
RUN pip install -r req.txt

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy project
COPY . /usr/src/app


RUN python manage.py migrate