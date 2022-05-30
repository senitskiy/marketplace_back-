FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV app_port 8000

COPY . /code/
WORKDIR /code
RUN pip install -r req.txt
RUN sed -i 's/force_text/force_str/' /usr/local/lib/python3.10/site-packages/graphene_django/utils/utils.py
RUN python manage.py makemigrations && python manage.py migrate 
EXPOSE ${app_port}