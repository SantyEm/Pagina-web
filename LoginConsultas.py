from flask import Flask, render_template, request, redirect, url_for, session
from conexion import get_connection
import re

app = Flask(__name__)
app.secret_key = 'XD'

mensajes = {
    "error_password_mismatch": "Las contraseñas no coinciden. Inténtalo de nuevo.",
    "error_security_answer": "La respuesta de seguridad es incorrecta. Inténtalo nuevamente.",
    "error_user_not_found": "El usuario o correo electrónico no existe.",
    "success_password_changed": "Contraseña cambiada exitosamente."
}

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    if 'username' in session:
        username = session['username']
        print("Nombre de usuario en sesión:", username)  # Agregar esta línea para imprimir en la consola
        return render_template('home.html', username=username)
    else:
        return redirect(url_for('login'))

@app.route('/processLogin', methods=['POST'])
def process_login():
    
    username = request.form['username']
    password = request.form['password']

    print(f"Username: {username}, Password: {password}")

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuario WHERE NombreUsuario = %s AND Contraseña = %s", (username, password))
    user = cursor.fetchone()
    cursor.close()
    connection.close()

    if user:
        print("Inicio de sesión exitoso.")
        session['username'] = username
        session['usuario_id'] = user['UsuarioID']
        success_message = "Inicio de sesión exitoso."
        return redirect(url_for('home', success_message=success_message))
    else:
        print("Usuario o contraseña incorrectos.")
        error = "Usuario o contraseña incorrectos. Por favor, inténtalo nuevamente."
        return render_template('login.html', error=error)


# Ruta para el formulario de registro
@app.route('/registrarse', methods=['GET'])
def IngresoRegistro():
    return render_template('loginRegistro.html')  # Renderiza el formulario para ingresar la nueva contraseña

def es_contraseña_segura(contraseña):
    if len(contraseña) < 8:
        return False, "La contraseña debe tener al menos 8 caracteres."
    if not re.search(r'[A-Z]', contraseña):
        return False, "La contraseña debe contener al menos una letra mayúscula."
    if not re.search(r'[a-z]', contraseña):
        return False, "La contraseña debe contener al menos una letra minúscula."
    if not re.search(r'[0-9]', contraseña):
        return False, "La contraseña debe contener al menos un número."
    if not re.search(r'[!@#$%^&*]', contraseña):
        return False, "La contraseña debe contener al menos un carácter especial (!@#$%^&*)."
    return True, ""

@app.route('/registrar_usuario', methods=['POST'])
def procesar_registro():
    if request.method == 'POST':
        try:
            # Obtener los datos del formulario
            nombre_usuario = request.form['nombre_usuario']
            apellido_usuario = request.form['apellido_usuario']
            contraseña = request.form['contraseña']
            email = request.form['email']
            pregunta_seguridad = request.form['pregunta_seguridad']
            respuesta_seguridad = request.form['respuesta_seguridad']

            # Validar la contraseña
            es_segura, mensaje = es_contraseña_segura(contraseña)
            if not es_segura:
                return render_template('loginRegistro.html', error=mensaje)

            # Obtener la conexión y el cursor
            connection = get_connection()
            cursor = connection.cursor()

            # Verificar si el usuario o el email ya existen en la base de datos
            cursor.execute("SELECT * FROM usuario WHERE NombreUsuario = %s OR Email = %s", (nombre_usuario, email))
            existing_user = cursor.fetchone()

            if existing_user:
                cursor.close()
                connection.close()
                return render_template('loginRegistro.html', error="El usuario o el email ya existen. Intente con otro.")

            # Insertar los nuevos datos en la tabla de usuarios
            insert_query = "INSERT INTO usuario (NombreUsuario, Apellido, Contraseña, Email, PreguntaSeguridad, RespuestaSeguridad) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (nombre_usuario, apellido_usuario, contraseña, email, pregunta_seguridad, respuesta_seguridad)
            cursor.execute(insert_query, values)
            connection.commit()

            # Cerrar el cursor y la conexión
            cursor.close()
            connection.close()

            # Redirige a la página de inicio de sesión
            return render_template('login.html', mensaje="Registro exitoso. Por favor, inicia sesión.")
        except Exception as e:
            print(f"Error al procesar el registro: {str(e)}")
            return "Error al procesar el registro. Inténtalo de nuevo más tarde."

    # Si el método no es POST, renderiza nuevamente el formulario de registro
    return render_template('loginRegistro.html')
# hasta aca proceso de login en duda si colocarlo o no

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'GET':
        return render_template('loginCambioContraseña1.html')  # Renderiza el primer formulario para ingresar el usuario o email
    
    if request.method == 'POST':
        try:
            username_or_email = request.form['username_or_email']
            
            # Conexión a la base de datos
            connection = get_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM usuario WHERE NombreUsuario = %s OR Email = %s", (username_or_email, username_or_email))
            existing_user = cursor.fetchone()
            
            if existing_user:
                # Obtener la pregunta de seguridad asociada al usuario o email
                security_question = existing_user['PreguntaSeguridad']
                return render_template('loginCambioContraseña2.html', security_question=security_question, username_or_email=username_or_email)
            else:
                return render_template('loginCambioContraseña1.html', error="El usuario o correo electrónico no existe.")

        except Exception as e:
            print(f"Error al procesar la solicitud de cambio de contraseña: {str(e)}")
            return render_template('loginCambioContraseña1.html', error="Error al procesar la solicitud. Inténtalo nuevamente.")

    return render_template('loginCambioContraseña1.html')


@app.route('/cambiar_contraseña', methods=['POST'])
def cambiar_contraseña():
    try:
        # Imprimir los datos recibidos para depuración
        print(request.form)

        username_or_email = request.form['username_or_email']
        security_answer = request.form['security_answer']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']
        security_question = request.form['security_question']

        # Verificar que las contraseñas coinciden
        if new_password != confirm_password:
            return render_template('loginCambioContraseña2.html', error="Las contraseñas no coinciden. Intenta de nuevo.", security_question=security_question, username_or_email=username_or_email)

        # Conexión a la base de datos
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuario WHERE NombreUsuario = %s OR Email = %s", (username_or_email, username_or_email))
        user = cursor.fetchone()

        # Verificar usuario y respuesta de seguridad
        if user and user['RespuestaSeguridad'].strip().lower() == security_answer.strip().lower():
            # Actualizar la contraseña
            cursor.execute("UPDATE usuario SET Contraseña = %s WHERE NombreUsuario = %s OR Email = %s", (new_password, username_or_email, username_or_email))
            connection.commit()

            # Verificar si la actualización fue exitosa
            if cursor.rowcount > 0:
                success_message = mensajes["success_password_changed"]
                success_password_changed = "Contraseña cambiada exitosamente."
                cursor.close()
                connection.close()
                return render_template('login.html')  # Redirigir al formulario de inicio de sesión
            else:
                error_message = mensajes["error_security_answer"]
                success_password_changed = "No se pudo actualizar la contraseña."
        else:
            cursor.close()
            connection.close()
            return render_template('loginCambioContraseña2.html', error="La respuesta de seguridad es incorrecta. Inténtalo nuevamente.", security_question=security_question, username_or_email=username_or_email)
    
    except Exception as e:
        print(f"Error al cambiar la contraseña: {str(e)}")
        return render_template('loginCambioContraseña2.html', error="Error al procesar el cambio de contraseña. Inténtalo nuevamente.", security_question=security_question, username_or_email=username_or_email)


@app.route('/actualizar_informacion', methods=['POST'])
def actualizar_informacion():
    if 'username' in session:
        username = session['username']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']

        connection = get_connection()
        cursor = connection.cursor()

        # Actualizar los datos del usuario en la base de datos
        query = "UPDATE usuario SET NombreUsuario = %s, Apellido = %s, Email = %s WHERE NombreUsuario = %s"
        cursor.execute(query, (nombre, apellido, email, username))
        connection.commit()

        # Volver a consultar los datos actualizados del usuario
        query_select = "SELECT UsuarioID, NombreUsuario, Apellido, Email FROM usuario WHERE NombreUsuario = %s"
        cursor.execute(query_select, (username,))
        datos_usuario = cursor.fetchone()

        cursor.close()
        connection.close()

        if datos_usuario:
            success_message = "Información actualizada correctamente."
            return render_template('opcionesUsuario.html', datos_usuario=datos_usuario, success_message=success_message)
        else:
            return render_template('opcionesUsuario.html', message="Error al actualizar la información del usuario")

    else:
        return redirect(url_for('login'))

@app.route('/cambiar-contraseña', methods=['POST'])
def cambiar_contrasena():
    if 'username' in session:
        username = session['username']
        
        # Obtener el id_usuario desde la base de datos
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT UsuarioID FROM usuario WHERE NombreUsuario = %s", (username,))
        id_usuario = cursor.fetchone()[0]
        
        contrasena_actual = request.form['current-password']
        nueva_contrasena = request.form['new-password']
        confirmar_nueva_contrasena = request.form['confirm-new-password']
        
        # Verificar que la contraseña actual coincida con la almacenada en la base de datos
        cursor.execute("SELECT contraseña FROM usuario WHERE UsuarioID = %s", (id_usuario,))
        resultado = cursor.fetchone()
        if resultado[0] != contrasena_actual:
            return 'Contraseña actual incorrecta', 401
        
        # Verificar que la nueva contraseña y su confirmación coincidan
        if nueva_contrasena != confirmar_nueva_contrasena:
            return 'Nueva contraseña y confirmación no coinciden', 400
        
        # Actualizar la contraseña en la base de datos
        cursor.execute("UPDATE usuario SET contraseña = %s WHERE UsuarioID = %s", (nueva_contrasena, id_usuario))
        connection.commit()
        
        return redirect(url_for('home'))
    
    else:
        return redirect(url_for('home'))
    

if __name__ == '__main__':
    app.run()