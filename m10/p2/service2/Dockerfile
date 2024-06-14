FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

# Comando para executar a aplicação usando Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8002", "src.main:app"]