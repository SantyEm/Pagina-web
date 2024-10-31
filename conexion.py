from flask import Flask, render_template, request, redirect
import schedule
import datetime
import os
import subprocess
import time
import threading
import mysql.connector

app = Flask(__name__)

def get_connection():
    config = {
        'host': 'localhost',
        'user': 'root',
        'password': '12345',
        'database': 'bdpsico'
    }
    # Intenta establecer la conexión
    try:
        connection = mysql.connector.connect(**config)
        print("Conexión exitosa a la base de datos")
        return connection
    except mysql.connector.Error as error:
        print("Error al conectar a la base de datos:", error)
        return None
    

# Función para realizar la copia de seguridad de la base de datos
def backup_database():
    """
    Realiza una copia de seguridad de la base de datos 'bdpsico' en un archivo .sql
    """
    
    # Establece conexión con la base de datos
    connection = get_connection()
    
    if connection:
        # Genera el nombre del archivo de backup con la fecha actual
        filename = f"backup_{datetime.date.today().strftime('%Y-%m-%d')}.sql"
        
        # Establece la ruta donde se guardará el archivo de backup
        filepath = os.path.join("C:\\Backups\\MySQL", filename)
        
        # Comando para realizar la copia de seguridad utilizando mysqldump
        command = f"mysqldump -h localhost -u root -p12345 bdpsico > {filepath}"
        
        # Ejecuta el comando en la terminal
        subprocess.run(command, shell=True)
        
        # Cierra la conexión con la base de datos
        connection.close()


# Programa la copia de seguridad para ejecutarse diariamente a las 2:00 AM
schedule.every().day.at("02:00").do(backup_database)


# Configura el schedule para ejecutarse antes de la primera solicitud
@app.before_first_request
def setup_schedule():
    """
    Configura el schedule para ejecutarse en segundo plano
    """
    
    # Función para ejecutar el schedule en segundo plano
    def run_schedule():
        while True:
            # Ejecuta las tareas programadas
            schedule.run_pending()
            
            # Espera 1 segundo antes de verificar nuevamente
            time.sleep(1)
    
    # Crea un hilo para ejecutar el schedule en segundo plano
    thread = threading.Thread(target=run_schedule)
    
    # Inicia el hilo
    thread.start()