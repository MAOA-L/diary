FROM python:3.7

WORKDIR /app

COPY ./ ./
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8081

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8081"]
RUN chmod 777 start.sh
CMD ["start.sh"]