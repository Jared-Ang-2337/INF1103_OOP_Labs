FROM python:3.14-slim

WORKDIR /app

COPY *.py ./
COPY inventory.json ./

CMD ["python", "main.py"]
