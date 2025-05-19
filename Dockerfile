FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Команда для запуску додатка
CMD ["python", "run.py"]