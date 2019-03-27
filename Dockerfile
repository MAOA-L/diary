FROM python:3.7

WORKDIR /app

COPY diary diary
COPY manage.py requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8081

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8081"]