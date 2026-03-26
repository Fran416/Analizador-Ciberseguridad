FROM python:3.10-slim

# Instalamos Git (indispensable para tu miner)
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copiamos todo: app.py, index.html, repos.csv y processor.py
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Exponemos el puerto familiar
EXPOSE 8080

# Esto activa el "coso" apenas se inicia el contenedor
CMD ["python", "app.py"]