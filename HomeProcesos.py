from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/opciones_usuario')
def opciones_usuario():
    # Aquí podrías realizar consultas adicionales o lógica relacionada con las opciones del usuario
    print("¡Llegaste a la función opciones_usuario()!")  # Mensaje de prueba en consola
    return render_template('opcionesUsuario.html')

if __name__ == '__main__':
    app.run()
