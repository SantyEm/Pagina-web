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
app.add_url_rule('/padre/direcciones/<int:id_padre>', 'mostrar_direcciones_padre', PadresConsulta.mostrar_direcciones_padre)
app.add_url_rule('/direcciones/editar/<int:id_direccion>', 'editar_direccion', PadresConsulta.editar_direccion)
app.add_url_rule('/direcciones/agregar', 'agregar_direccion', PadresConsulta.agregar_direccion)
app.add_url_rule('/agregar-padre', 'agregar_padre', PadresConsulta.agregar_padre)
app.add_url_rule('/padres', 'obtener_padres', PadresConsulta.obtener_padres)
app.add_url_rule('/eliminar_padre/<int:Id_padre>', 'eliminar_padre', PadresConsulta.eliminar_padre, methods=['POST'])
app.add_url_rule('/padre/<int:id_padre>/datos-embarazo/', 'mostrar_datos_embarazo', PadresConsulta.mostrar_datos_embarazo, methods=['GET'])
app.add_url_rule('/padre/editar/<int:padre_id>', 'editar_padre', PadresConsulta.editar_padre, methods=['GET', 'POST'])
app.add_url_rule('/editar-padre', 'editar_padre_form', PadresConsulta.editar_padre_form, methods=['POST'])
app.add_url_rule('/registrar-embarazo', 'agregar_embarazo', PadresConsulta.Agregar_embarazo, methods=['POST'])
app.add_url_rule('/embarazo/editar/<int:embarazo_id>', 'editar_embarazo', PadresConsulta.editar_embarazo, methods=['GET', 'POST'])
app.add_url_rule('/buscar', 'buscar', PadresConsulta.buscar, methods=['POST'])

# procesos del pacientes
app.add_url_rule('/pacientes', "mostrar_pacientes", pacientesConsultas.mostrar_pacientes)
app.add_url_rule('/paciente/direcciones/<int:id_paciente>', 'mostrar_direcciones', pacientesConsultas.mostrar_direcciones, methods=['GET'])
app.add_url_rule('/agregar-paciente', 'agregar_paciente', pacientesConsultas.agregar_paciente, methods=['POST'])
app.add_url_rule('/agregar-direccion/<id_paciente>', 'agregar_direccion_paciente', pacientesConsultas.agregar_direccion_paciente, methods=['GET', 'POST'])
app.add_url_rule('/paciente/historial_educacion/<int:id_paciente>', 'historial_educacion', pacientesConsultas.historial_educacion, methods=['GET', 'POST'])
app.add_url_rule('/paciente/historial_educacion/<int:id_paciente>', 'historial_educacion', pacientesConsultas.historial_educacion, methods=['GET', 'POST'])
app.add_url_rule('/paciente/informacion_familiar/<int:id_paciente>', 'informacion_familiar', pacientesConsultas.informacion_familiar, methods=['GET', 'POST'])
app.add_url_rule('/editar_paciente/<int:id_paciente>', 'editar_paciente', pacientesConsultas.editar_paciente, methods=['GET', 'POST'])
app.add_url_rule('/eliminar_paciente/<int:id_paciente>', 'eliminar_paciente', pacientesConsultas.eliminar_paciente, methods=['POST'])
app.add_url_rule('/busqueda_sesiones', 'buscar_sesiones', pacientesConsultas.buscar_sesiones, methods=['POST'])


# procesos del desarrollo
app.add_url_rule('/Desarrollo', "mostrar_desarrollo", DesarrolloConsultas.mostrar_desarrollo)



if __name__ == '__main__':
    app.run(debug=True)
