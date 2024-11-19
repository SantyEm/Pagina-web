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
app.add_url_rule("/backup_seguridad", "crear_backup", HomeProcesos.crear_backup, methods=["POST"])
app.add_url_rule('/volver_inicio', 'home', LoginConsultas.home)


 # procesos del tutor
app.add_url_rule('/padres', 'mostrar_padres', PadresConsulta.mostrar_padres)

app.add_url_rule("/padre/editar/<int:padre_id>", "editar_padre", PadresConsulta.editar_padre, methods=['GET', 'POST'])
app.add_url_rule('/padre/direcciones/<int:id_padre>', 'mostrar_direcciones_padre', PadresConsulta.mostrar_direcciones_padre, methods=['GET'])
app.add_url_rule('/direcciones/editar/<int:id_direccion>', 'editar_direccion', PadresConsulta.editar_direccion, methods=['GET', 'POST'])
app.add_url_rule('/direcciones/agregar/<id_padre>r', 'agregar_direccion', PadresConsulta.agregar_direccion, methods=['POST'])
app.add_url_rule('/direcciones/actualizar/<int:id_direccion>', "actualizar_direccion", PadresConsulta.actualizar_direccion, methods=['POST'])
app.add_url_rule("/direcciones/eliminar/<int:id_direccion>", "eliminar_direccion", PadresConsulta.eliminar_direccion, methods=['POST'])

app.add_url_rule('/agregar-padre', 'agregar_padre_registro', PadresConsulta.agregar_padre_registro, methods=['POST'])
app.add_url_rule('/padres', 'obtener_padres', PadresConsulta.obtener_padres)
app.add_url_rule('/eliminar_padre/<int:Id_padre>', 'eliminar_padre', PadresConsulta.eliminar_padre, methods=['POST'])

app.add_url_rule('/padre/editar/<int:padre_id>', 'editar_padre', PadresConsulta.editar_padre, methods=['GET', 'POST'])
app.add_url_rule('/editar-padre', 'editar_padre_form', PadresConsulta.editar_padre_form, methods=['POST'])
app.add_url_rule('/buscar', 'buscar', PadresConsulta.buscar, methods=['POST'])

# procesos del pacientes
app.add_url_rule('/pacientes', "mostrar_pacientes", pacientesConsultas.mostrar_pacientes)
app.add_url_rule('/paciente/direcciones/<int:id_paciente>', 'mostrar_direcciones', pacientesConsultas.mostrar_direcciones, methods=['GET'])
app.add_url_rule('/agregar-paciente', 'agregar_paciente', pacientesConsultas.agregar_paciente, methods=['POST'])
app.add_url_rule("/editar_paciente/<int:id_paciente>", "mostrar_edicion_paciente", pacientesConsultas.mostrar_edicion_paciente, methods=['GET'])
app.add_url_rule("/actualizar_paciente", "actualizar_paciente", pacientesConsultas.actualizar_paciente, methods=['POST'])
app.add_url_rule('/eliminar_paciente/<int:id_paciente>', 'eliminar_paciente', pacientesConsultas.eliminar_paciente, methods=['POST'])
app.add_url_rule('/buscarPaciente', 'buscar_paciente', pacientesConsultas.buscar_paciente, methods=['POST'])


app.add_url_rule('/agregar-direccion/<id_paciente>', 'agregar_direccion_paciente', pacientesConsultas.agregar_direccion_paciente, methods=['GET', 'POST'])
app.add_url_rule("/paciente/direcciones/editar/<int:id_paciente>/<int:id_direccion>", "editar_direccion_paciente", pacientesConsultas.editar_direccion_paciente, methods=['GET', 'POST'])
app.add_url_rule("/paciente/direcciones/actualizar/<int:id_paciente>/<int:id_direccion>", "actualizar_direccion_paciente", pacientesConsultas.actualizar_direccion_paciente, methods=['POST'])
app.add_url_rule("/paciente/direcciones/eliminar/<int:id_paciente>/<int:id_direccion>", "eliminar_direccion_paciente", pacientesConsultas.eliminar_direccion_paciente, methods=['POST'])


app.add_url_rule('/paciente/historial_educacion/<int:id_paciente>', 'historial_educacion', pacientesConsultas.historial_educacion, methods=['GET', 'POST'])
app.add_url_rule('/agregar-historial-educativo/<int:id_paciente>', 'agregar_historial_educativo', pacientesConsultas.agregar_historial_educativo, methods=['POST'])
app.add_url_rule("/historial-educativo/editar/<int:id_historial>", "editar_historial_educativo", pacientesConsultas.editar_historial_educativo, methods=['GET'])


app.add_url_rule('/paciente/informacion_familiar/<int:id_paciente>', 'informacion_familiar', pacientesConsultas.informacion_familiar, methods=['GET', 'POST'])

app.add_url_rule("/paciente/<int:id_paciente>/datos_gestacion", "mostrar_datos_gestacion", pacientesConsultas.mostrar_datos_gestacion, methods=['GET'])
app.add_url_rule("/registrar-embarazo", "agregar_embarazo", pacientesConsultas.agregar_embarazo, methods=['POST'])
app.add_url_rule("/embarazo/editar/<int:embarazo_id>", "editar_embarazo", pacientesConsultas.editar_embarazo, methods=['GET', 'POST'])

# procesos del desarrollo
app.add_url_rule('/Desarrollo', "mostrar_desarrollo", DesarrolloConsultas.mostrar_desarrollo)
app.add_url_rule("/agregar-sesion", "agregar_sesiones", DesarrolloConsultas.agregar_sesiones, methods=['POST'])
app.add_url_rule("/historial/<int:id_paciente>", "mostrar_historial", DesarrolloConsultas.mostrar_historial, methods=['GET'])
app.add_url_rule("/sesion/editar/<int:id_sesion>", "obtener_sesion", DesarrolloConsultas.obtener_sesion, methods=['GET'])
app.add_url_rule("/sesion/actualizar/<int:id_sesion>", "actualizar_sesion", DesarrolloConsultas.actualizar_sesion, methods=['POST'])
app.add_url_rule("/sesion/eliminar/<int:id_sesion>", "eliminar_sesion", DesarrolloConsultas.eliminar_sesion, methods=['POST'])
app.add_url_rule("/busqueda_sesiones", "buscar_sesiones", DesarrolloConsultas.buscar_sesiones, methods=['POST'])
app.add_url_rule("/exportar_todo/<int:id_paciente>", "exportar_todo", DesarrolloConsultas.exportar_todo)


if __name__ == '__main__':
    app.run(debug=True)
