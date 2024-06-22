from flask import Flask, render_template, request, redirect, url_for
from conexion import get_connection

app = Flask(__name__)

@app.route("/")
def home():
    # Lógica de procesamiento para el home
    
    connection = get_connection()
    cursor = connection.cursor()
    user = cursor.fetchone()
    cursor.close()
    connection.close()
    return render_template("home.html")


if __name__ == "__main__":
    app.run()