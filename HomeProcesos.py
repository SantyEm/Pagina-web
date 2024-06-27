from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/opciones_usuario')
def opciones_usuario():
    # Aquí podrías realizar consultas adicionales o lógica relacionada con las opciones del usuario
    print("¡Llegaste a la función opciones_usuario()!")  # Mensaje de prueba en consola
    return render_template('opcionesUsuario.html')

@app.route('/acerca-de')
def AcercaDe():
    # Aquí podrías realizar consultas adicionales del acerca de
    return render_template('acercaDe.html')

@app.route('/datos_pacientes')
def pacientes():
    # Aquí podrías realizar consultas adicionales del paciente formulario xd
    return render_template('PacienteFormulario.html')

@app.route('/volver_inicio')
def inicio():
    # Aquí podrías realizar consultas adicionales del paciente formulario xd
    return render_template('home.html')

@app.route("/cerrar-sesion", methods=['GET', 'POST'])
def logout():
    confirm_logout = request.args.get("confirm_logout")
    if confirm_logout == "true":
        # Redirige al usuario a la página de inicio
        return render_template('login.html')
    else:
        # En caso de que el usuario no confirme el cierre de sesión, redirige a la página de inicio de sesión
        return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
