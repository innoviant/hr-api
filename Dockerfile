FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

EXPOSE 8000

# Команда для запуска uvicorn
CMD python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload \
    --proxy-headers --forwarded-allow-ips '*'