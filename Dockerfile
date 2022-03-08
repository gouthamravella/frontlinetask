FROM python:3.8.5-slim

WORKDIR /code

# set environment variables
ENV ENVIRONMENT='DEV'

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y sudo netcat apt-utils
RUN apt-get install -y libmariadb-dev 
RUN apt-get install -y python3-dev build-essential python3-pip

COPY ./requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt

EXPOSE 8000
COPY . /code/

CMD [ "gunicorn", "sample_task.wsgi:application", "-b", "0.0.0.0:8000","--timeout","7200","--workers","3"]