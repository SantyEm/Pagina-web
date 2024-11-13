FROM python:3.9-slim

# Copia el archivo requirements.txt
COPY requirements.txt .

# Instala las dependencias
RUN pip install -r requirements.txt

# Configura el comando de ejecución
CMD ["python", "HomeProcesos.py"]