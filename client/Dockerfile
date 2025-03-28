FROM python:3.9-slim-buster

WORKDIR /app

COPY client/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY client/client.py .
COPY client/templates /app/templates

CMD ["python", "client.py"]