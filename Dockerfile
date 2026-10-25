FROM python:3.14-slim

WORKDIR /app

COPY main.py inventory.py product.py fileHandler.py ./
COPY inventory.txt ./

CMD ["python", "main.py"]
