FROM python:3.7

WORKDIR /app/diary

COPY ./ ./
# COPY requirements.txt /app/

# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt

EXPOSE 3031

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8081"]
RUN chmod 777 start.sh
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8081"]
CMD ["./start.sh"]