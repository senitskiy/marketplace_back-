FROM python:3.9

# environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV app_port 8000

COPY . /code/
WORKDIR /code
RUN pip install -r req.txt
RUN sed -i 's/force_text/force_str/' /usr/local/lib/python3.9/site-packages/graphene_django/utils/utils.py

EXPOSE ${app_port}

CMD ["python3", "manage.py", "runserver"]