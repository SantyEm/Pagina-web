from flask import Flask, render_template
from conexion import get_connection
from flask import request
from datetime import datetime
from flask import session
from flask import current_app

app = Flask(__name__)

def calcular_edad_pacientes(fecha_nacimiento):
    hoy = datetime.today()
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad

@app.route('/pacientes')
def mostrar_pacientes():
    pacientes = obtener_pacientes()
    return render_template('PacienteFormulario.html', pacientes=pacientes)

@app.route('/paciente/direcciones/<int:id_paciente>', methods=['GET'])
def mostrar_direcciones(id_paciente):
    # Obtener las direcciones del paciente con el ID especificado
    direcciones = obtener_direcciones(id_paciente)
    # Renderizar la plantilla con la tabla de direcciones
    return render_template('MostrarDireccionesPacientes.html', direcciones=direcciones)

def obtener_direcciones(id_paciente):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM t_02direccionpaciente WHERE Id_paciente = %s", (id_paciente,))
        direcciones = cursor.fetchall()
        if direcciones is None:
            return []
        return [dict(zip([column[0] for column in cursor.description], row)) for row in direcciones]
    except Exception as e:
        print(f"Error al obtener direcciones: {e}")
        return []
    
    
def obtener_pacientes():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT p.Id_paciente, p.Nombre, p.Apellido, p.DNI, g.Nombre AS Genero, p.Fecha_nacimiento, p.Fecha_registro, p.Observaciones FROM t_01paciente p JOIN t_02genero g ON p.Id_genero = g.Id_genero")
    pacientes = cursor.fetchall()
    pacientes = [dict(zip([column[0] for column in cursor.description], row)) for row in pacientes]
    
    # Agregar una columna adicional para la edad
    for paciente in pacientes:
        paciente['edad'] = calcular_edad_pacientes(paciente['Fecha_nacimiento'])
    
    cursor.close()
    connection.close()
    return pacientes
    
@app.route('/agregar-paciente', methods=['POST'])
def agregar_paciente():
    
    # Obtener la conexión y el cursor
    connection = get_connection()
    cursor = connection.cursor()
    
    # Recibir los datos del formulario
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    dni = request.form['dni']
    genero = request.form['genero']
    fecha_nacimiento = request.form['fecha_nacimiento']
    fecha_registro = request.form['fecha_registro']
    observaciones = request.form['observaciones']

    # Validar los datos
    if not nombre or not apellido or not dni or not genero or not fecha_nacimiento:
        return 'Faltan datos', 400
    
    # Validar fecha de nacimiento
    if fecha_nacimiento > datetime.today().strftime('%Y-%m-%d'):
        return 'Fecha de nacimiento inválida', 400
    
    # Obtener el Id_genero correspondiente al género seleccionado
    cursor.execute("SELECT Id_genero FROM t_02genero WHERE Nombre = %s", (genero,))
    id_genero = cursor.fetchone()[0]
    
    # Convertir la fecha de nacimiento a un objeto datetime
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')

    # Calcular la edad
    def calcular_edad_pacientes(fecha_nacimiento):
        hoy = datetime.today()
        edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        return edad
    
    edad = calcular_edad_pacientes(fecha_nacimiento)

    # Insertar los datos en la base de datos
    cursor.execute("INSERT INTO t_01paciente (Id_paciente, Nombre, Apellido, DNI, Id_genero, Fecha_nacimiento, Edad, Fecha_registro, Observaciones) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s)", (nombre, apellido, dni, id_genero, fecha_nacimiento, edad, fecha_registro, observaciones))
    connection.commit()

    # Actualizar la tabla de pacientes
    pacientes = obtener_pacientes()

    return render_template('PacienteFormulario.html', pacientes=pacientes)

def obtener_paciente_por_id(id_paciente):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM t_01paciente WHERE Id_paciente = %s", (id_paciente,))
    paciente = cursor.fetchone()
    cursor.close()
    connection.close()
    return paciente

@app.route('/agregar-direccion/<id_paciente>', methods=['GET', 'POST'])
def agregar_direccion(id_paciente):
    if request.method == 'POST':
        print(request.form)  # Imprime los datos del formulario
        print(request.headers)  # Imprime los headers de la solicitud
        
        # Obtener la conexión y el cursor
        connection = get_connection()
        cursor = connection.cursor()
        
        # Recibir los datos del formulario
        paciente = obtener_paciente_por_id(id_paciente)
        print(f"Paciente: {paciente}")
        direccion = request.form['direccion']
        ciudad = request.form['ciudad']
        estado = request.form['estado']
        codigo_postal = request.form['codigo_postal']
        
        # Validar los datos
        if not direccion or not ciudad or not estado or not codigo_postal:
            return 'Faltan datos', 400
        
        try:
            # Insertar los datos en la base de datos
            cursor.execute("INSERT INTO t_02direccionpaciente (id_direccion, id_paciente, direccion, ciudad, estado, codigo_postal) VALUES (NULL, %s, %s, %s, %s, %s)", (id_paciente, direccion, ciudad, estado, codigo_postal))
            connection.commit()
            print("Datos insertados correctamente")
        except Exception as e:
            print(f"Error: {e}")
            connection.rollback()  # Revertir los cambios en caso de error
        finally:
            connection.close()  # Cerrar la conexión
        
        return render_template('agregarDireccionPaciente.html', paciente=paciente, mensaje="Dirección agregada con éxito")
    else:
        paciente = obtener_paciente_por_id(id_paciente)
        return render_template('agregarDireccionPaciente.html', paciente=paciente)

@app.route('/paciente/historial_educacion/<int:id_paciente>', methods=['GET', 'POST'])
def historial_educacion(id_paciente):
    # Código para manejar la ruta
    registros = obtener_historial_educativo(id_paciente)
    return render_template('HistorialEducativoPaciente.html', registros=registros)


def obtener_historial_educativo(id_paciente):
    # Cursor para ejecutar consultas
    connection = get_connection()
    cursor = connection.cursor()
    
    # Consulta SQL
    query = """
    SELECT 
        he.id_historial, 
        p.Nombre AS paciente, 
        ci.institucion AS institucion, 
        he.adaptacion, 
        he.relacion_docentes, 
        he.relacion_compañeros, 
        he.repitencia_escolar, 
        he.cambios_escuelas, 
        he.cambios_maestros
    FROM 
        t_10historialeducativo he
    INNER JOIN 
        t_01paciente p ON he.id_paciente = p.Id_paciente
    INNER JOIN 
        t_11caracteristicainstitu ci ON he.id_institucion = ci.id_institucion
    WHERE 
        he.id_paciente = %s
"""
    
    # Ejecutar consulta
    cursor.execute(query, (id_paciente,))
    
    # Obtener resultados
    resultados = cursor.fetchone()
    
    print(resultados)  # Imprimir los resultados en la consola
    
    # Procesar resultados
    if resultados:
        campos = [column[0] for column in cursor.description]
        respuesta = [dict(zip(campos, resultados))]
    else:
        respuesta = []
    
    # Cerrar cursor y conexión
    cursor.close()
    connection.close()
    
    return respuesta

@app.route('/paciente/informacion_familiar/<int:id_paciente>', methods=['GET', 'POST'])
def informacion_familiar(id_paciente):
    # Código para manejar la ruta
    registros = obtener_informacion_familiar(id_paciente)
    return render_template('InfoFamiliarPaciente.html', registros=registros)


def obtener_informacion_familiar(id_paciente):
    # Cursor para ejecutar consultas
    connection = get_connection()
    cursor = connection.cursor()
    
    # Consulta SQL
    query = """
SELECT 
    info_familiar.id_informacion_familiar,
    p.Nombre AS paciente,
    info_familiar.ambiente_familiar,
    info_familiar.union_estable,
    info_familiar.tiempo_convivencia,
    info_familiar.ingresos_padre,
    info_familiar.ingresos_madre,
    info_familiar.expectativas_padres,
    info_familiar.dia_comun_menor,
    ev.estado_vivienda
FROM 
    t_12infofamiliar info_familiar
INNER JOIN 
    t_01paciente p ON info_familiar.id_paciente = p.Id_paciente
INNER JOIN 
    t_12estadovivienda ev ON info_familiar.id_estado_vivienda = ev.id_estado
WHERE 
    info_familiar.id_paciente = %s
"""
    
    # Ejecutar consulta
    cursor.execute(query, (id_paciente,))
    
    # Obtener resultados
    resultados = cursor.fetchall()
    
    print(resultados)  # Imprimir los resultados en la consola
    
    # Procesar resultados
    if resultados:
        campos = [column[0] for column in cursor.description]
        respuesta = [dict(zip(campos, registro)) for registro in resultados]
    else:
        respuesta = []
    
    # Cerrar cursor y conexión
    cursor.close()
    connection.close()
    
    return respuesta

@app.route('/editar_paciente/<int:id_paciente>', methods=['GET', 'POST'])
def editar_paciente(id_paciente):
    connection = get_connection()
    cursor = connection.cursor()

    if request.method == 'POST':
        nombre = request.form['Nombre']
        apellido = request.form['Apellido']
        cursor.execute("UPDATE pacientes SET nombre = %s, apellido = %s WHERE id_paciente = %s", (nombre, apellido, id_paciente))
        connection.commit()
        return redirect(url_for('index'))
    return render_template('editar_paciente.html')

@app.route('/eliminar_paciente/<int:id_paciente>', methods=['POST'])
def eliminar_paciente(id_paciente):
    connection = get_connection()
    cursor = connection.cursor()
    
    # Eliminar registros relacionados
    cursor.execute("DELETE FROM t_02direccionpaciente WHERE Id_paciente = %s", (id_paciente,))
    cursor.execute("DELETE FROM t_06datosembarazo WHERE Id_paciente = %s", (id_paciente,))
    cursor.execute("DELETE FROM t_10historialeducativo WHERE Id_paciente = %s", (id_paciente,))
    cursor.execute("DELETE FROM t_12infofamiliar WHERE Id_paciente = %s", (id_paciente,))
    cursor.execute("DELETE FROM t_13datosesion WHERE Id_paciente = %s", (id_paciente,))
    
    # Eliminar registro de paciente
    cursor.execute("DELETE FROM t_01paciente WHERE Id_paciente = %s", (id_paciente,))
    
    connection.commit()
    connection.close()
    return render_template('PacienteFormulario.html')

if __name__ == '__main__':
    app.run()