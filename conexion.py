from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

def get_connection():
            config = {
            'host': 'junction.proxy.rlwy.net',
            'user': 'root',
            'password': 'qCEFPRFRQtRjGdVhZDGJTyaDnrBeBKAN',
            'database': 'railway',
            'port': 55492
        }
    # Intenta establecer la conexión
    try:
        connection = mysql.connector.connect(**config)
        print("Conexión exitosa a la base de datos")
        return connection
    except mysql.connector.Error as error:
        print("Error al conectar a la base de datos:", error)
        return None
    

