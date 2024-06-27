from flask import Flask
import LoginConsultas
import HomeProcesos

app = Flask(__name__)

 # procesos del login 
app.add_url_rule('/', 'login', LoginConsultas.login)
app.add_url_rule('/inicio', 'inicio', LoginConsultas.inicio)
app.add_url_rule('/processLogin', 'process_login', LoginConsultas.process_login, methods=['POST'])
app.add_url_rule('/registrarse', 'IngresoRegistro', LoginConsultas.IngresoRegistro, methods=['GET'])
app.add_url_rule('/registrar_usuario', 'procesar_registro', LoginConsultas.procesar_registro, methods=['POST'])
app.add_url_rule('/forgot_password', 'forgot_password', LoginConsultas.forgot_password, methods=['GET', 'POST'])
app.add_url_rule('/cambiar_contraseña', 'cambiar_contraseña', LoginConsultas.cambiar_contraseña, methods=['POST'])

 # procesos del home
app.add_url_rule('/opciones_usuario', 'opciones_usuario', HomeProcesos.opciones_usuario)
app.add_url_rule('/cerrar-sesion', 'logout', HomeProcesos.logout, methods=['GET', 'POST'])
app.add_url_rule('/acerca-de', 'AcercaDe', HomeProcesos.AcercaDe)
app.add_url_rule('/datos_pacientes', 'pacientes', HomeProcesos.pacientes)
app.add_url_rule('/volver_inicio', 'inicio', LoginConsultas.inicio)

if __name__ == '__main__':
    app.run(debug=True)
