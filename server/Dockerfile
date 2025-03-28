FROM python:3.9-slim-buster

WORKDIR /app

COPY server/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY server/server.py .

CMD ["python", "server.py"]