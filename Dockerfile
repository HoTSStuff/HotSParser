FROM python:2.7.9
RUN mkdir -p /app
ADD . /app
RUN pip install -r /app/requirements.txt

WORKDIR /app
CMD ["python", "manage.py", "runserver"]