from flask import Flask, session
import LoginConsultas
import HomeProcesos
import PadresConsulta
import pacientesConsultas
import DesarrolloConsultas

app = Flask(__name__)
app.secret_key = 'XD'

 # procesos del login 
app.add_url_rule('/', 'login', LoginConsultas.login)
app.add_url_rule('/home', 'home', LoginConsultas.home)
app.add_url_rule('/processLogin', 'process_login', LoginConsultas.process_login, methods=['POST'])
app.add_url_rule('/registrarse', 'IngresoRegistro', LoginConsultas.IngresoRegistro, methods=['GET'])
app.add_url_rule('/registrar_usuario', 'procesar_registro', LoginConsultas.procesar_registro, methods=['POST'])
app.add_url_rule('/forgot_password', 'forgot_password', LoginConsultas.forgot_password, methods=['GET', 'POST'])
app.add_url_rule('/cambiar_contraseña', 'cambiar_contraseña', LoginConsultas.cambiar_contraseña, methods=['POST'])
app.add_url_rule('/actualizar_informacion', 'actualizar_informacion', LoginConsultas.actualizar_informacion, methods=['POST'])
app.add_url_rule('/informacion_personal', 'informacion_personal', LoginConsultas.informacion_personal)

 # procesos del home
app.add_url_rule('/opciones_usuario', 'opciones_usuario', HomeProcesos.opciones_usuario, methods=['GET', 'POST'])
app.add_url_rule('/cerrar-sesion', 'logout', HomeProcesos.logout, methods=['GET', 'POST'])
app.add_url_rule('/acerca-de', 'AcercaDe', HomeProcesos.AcercaDe)
app.add_url_rule('/backup', 'backup', HomeProcesos.backup)
app.add_url_rule('/volver_inicio', 'home', LoginConsultas.home)


 # procesos del padres
app.add_url_rule('/padres', 'mostrar_padres', PadresConsulta.mostrar_padres)


# procesos del pacientes
app.add_url_rule('/pacientes', "mostrar_pacientes", pacientesConsultas.mostrar_pacientes)

# procesos del desarrollo
app.add_url_rule('/Desarrollo', "mostrar_desarrollo", DesarrolloConsultas.mostrar_desarrollo)



if __name__ == '__main__':
    app.run(debug=True)
