FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /home/django/app
ENV PATH $PATH:/home/django/.local/bin

COPY requirements.txt /home/django/app
RUN pip install -r requirements.txt

COPY . /home/django/app

ENV PORT 8080

CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 ccpb.wsgi:application
