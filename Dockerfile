FROM python3.7

WORKDIR /app

COPY diary diary
COPY manage.py requirements.txt /app/

RUN pip install -r requirements.txt && \
        python manage.py collectstatic --noinput

EXPOSE 8081

CMD ["python", "manage.py", "runserver", "0.0.0.0:8081"]