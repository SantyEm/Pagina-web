from flask import Flask, render_template, request, redirect, url_for
from conexion import get_connection

app = Flask(__name__)

mensajes = {
    "error_password_mismatch": "Las contraseñas no coinciden. Inténtalo de nuevo.",
    "error_security_answer": "La respuesta de seguridad es incorrecta. Inténtalo nuevamente.",
    "error_user_not_found": "El usuario o correo electrónico no existe.",
    "success_password_changed": "Contraseña cambiada exitosamente."
}

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/inicio')
def inicio():
    # Lógica para el formulario de inicio
    return render_template('home.html')

@app.route('/processLogin', methods=['POST'])
def process_login():
    username = request.form['username']
    password = request.form['password']

    print(f"Username: {username}, Password: {password}")

    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM usuario WHERE NombreUsuario = %s AND Contraseña = %s", (username, password))
    user = cursor.fetchone()
    cursor.close()
    connection.close()

    if user:
        print("Inicio de sesión exitoso.")
        success_message = "Inicio de sesión exitoso."
        return render_template('home.html', success_message=success_message)
    else:
        print("Usuario o contraseña incorrectos.")
        error = "Usuario o contraseña incorrectos. Por favor, inténtalo nuevamente."
        return render_template('login.html', error=error)

# Ruta para el formulario de registro
@app.route('/registrarse', methods=['GET'])
def IngresoRegistro():
    return render_template('loginRegistro.html')  # Renderiza el formulario para ingresar la nueva contraseña

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
            rol_id = request.form['rol']
            codigo_especial = request.form.get('codigo')

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

            # Verificar si el código especial del administrador es correcto
            consulta_codigo = "SELECT codigo FROM codigos_administrador WHERE id = 1"  # Cambiar "id" según tu necesidad
            cursor.execute(consulta_codigo)
            resultado = cursor.fetchone()

            if resultado is None or codigo_especial != resultado[0]:
                cursor.close()
                connection.close()
                return render_template('loginRegistro.html', error="Código especial incorrecto. Por favor, ingresa el código correcto.")

            # Insertar los nuevos datos en la tabla de usuarios
            insert_query = "INSERT INTO usuario (NombreUsuario, Apellido, Contraseña, RolID, Email, PreguntaSeguridad, RespuestaSeguridad) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (nombre_usuario, apellido_usuario, contraseña, rol_id, email, pregunta_seguridad, respuesta_seguridad)
            cursor.execute(insert_query, values)
            connection.commit()

            # Cerrar el cursor y la conexión
            cursor.close()
            connection.close()

            # Redirige a la página de inicio de sesión
            return redirect('/')

        except Exception as e:
            print(f"Error al procesar el registro: {str(e)}")
            return "Error al procesar el registro. Inténtalo de nuevo más tarde."

    # Si el método no es POST, renderiza nuevamente el formulario de registro
    return render_template('loginRegistro.html')

def contar_usuarios_registrados():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM usuario")
        cantidad = cursor.fetchone()[0]
        cursor.close()
        connection.close()

        return cantidad
    except Exception as e:
        print(f"Error al contar usuarios: {str(e)}")
        return -1  # En caso de error, retorna -1

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


if __name__ == '__main__':
    app.run()