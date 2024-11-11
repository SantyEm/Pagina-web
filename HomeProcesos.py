from flask import Flask, render_template, request, url_for, redirect, session, make_response
from conexion import get_connection

import subprocess
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'XD'

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/opciones_usuario', methods=['GET', 'POST'])
def opciones_usuario():
    if 'username' in session:
        username = session['username']
        print(f"Username in session: {username}")  # Agregar este print

        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        query = "SELECT UsuarioID, NombreUsuario, Apellido, Email FROM usuario WHERE NombreUsuario = %s"
        cursor.execute(query, (username,))
        datos_usuario = cursor.fetchone()
        cursor.close()
        connection.close()

        print("Datos del usuario obtenidos:", datos_usuario)  # Verifica que los datos del usuario se obtienen correctamente

        return render_template('opcionesUsuario.html', datos_usuario=datos_usuario)
    else:
        return redirect(url_for('login'))

    
@app.route('/acerca-de')
def AcercaDe():
    # Aquí podrías realizar consultas adicionales del acerca de
    return render_template('acercaDe.html')

@app.route('/volver_inicio')
def inicio():
    # Aquí podrías realizar consultas adicionales del paciente formulario xd
    return render_template('home.html')

@app.route('/backup', methods=['GET', 'POST'])
def backup():
    # Código para manejar el formulario de backup
    return render_template('backup.html')

@app.route("/cerrar-sesion", methods=['GET', 'POST'])
def logout():
    confirm_logout = request.args.get("confirm_logout")
    if confirm_logout == "true":
        # Elimina la información de la sesión y redirige al usuario a la página de inicio de sesión
        session.clear()
        return redirect(url_for('login'))
    else:
        # En caso de que el usuario no confirme el cierre de sesión, redirige a la página de inicio
        # Agregar encabezados para evitar el almacenamiento en caché
        response = make_response(redirect(url_for('home')))
        response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
        return response

@app.route('/backup_seguridad', methods=['POST'])
def crear_backup():
    connection = get_connection()
    realizar_backup(connection)
    return redirect(url_for('backup', mensaje='backup guardado correctamente.'))

def realizar_backup(connection):
    # Ruta completa al archivo de salida
    ruta_archivo = r'C:\Users\Usuar\Downloads\bdpsico.sql'
    
    # Comando para exportar el esquema de la base de datos
    command = f'mysqldump -h localhost -u root -p12345 bdpsico > {ruta_archivo}'
    
    # Ejecutar el comando en la terminal
    subprocess.run(command, shell=True)
    
    # Mensaje de confirmación
    print(f"Exportación del esquema de la base de datos completada. Archivo guardado en {ruta_archivo}")
    connection.close()

    
if __name__ == '__main__':
    app.run(debug=True)
