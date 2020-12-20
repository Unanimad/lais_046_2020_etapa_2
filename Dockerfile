FROM python:3.6.7

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app
CMD ["python", "manage.py", "migrate"]
EXPOSE 8010
CMD ["python", "manage.py", "runserver", "0.0.0.0:8010"]