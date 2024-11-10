from flask import Flask, render_template
from conexion import get_connection
from flask import request
from datetime import datetime

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
    paciente = obtener_paciente_por_id(id_paciente)
    direcciones = obtener_direcciones(id_paciente)
    # Renderizar la plantilla con la tabla de direcciones
    return render_template('MostrarDireccionesPacientes.html', paciente=paciente, direcciones=direcciones)

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
    if not all([nombre, apellido, dni, genero, fecha_nacimiento]):
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
    edad = calcular_edad_pacientes(fecha_nacimiento)

    # Insertar los datos en la base de datos
    cursor.execute("""
        INSERT INTO 
            t_01paciente 
            (Id_paciente, Nombre, Apellido, DNI, Id_genero, Fecha_nacimiento, Fecha_registro, Observaciones) 
        VALUES 
            (NULL, %s, %s, %s, %s, %s, %s, %s)
    """, 
    (nombre, apellido, dni, id_genero, fecha_nacimiento, fecha_registro, observaciones))
    connection.commit()

    # Actualizar la tabla de pacientes
    pacientes = obtener_pacientes()

    return render_template('PacienteFormulario.html', pacientes=pacientes)

def obtener_paciente_por_id(id_paciente):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT 
            p.Id_paciente, 
            p.Nombre, 
            p.Apellido, 
            p.DNI, 
            g.Nombre AS Genero, 
            p.Fecha_nacimiento, 
            p.Fecha_registro, 
            p.Observaciones, 
            p.Id_padre 
        FROM 
            t_01paciente p 
        INNER JOIN 
            t_02genero g ON p.Id_genero = g.Id_genero 
        WHERE 
            p.Id_paciente = %s
    """, (id_paciente,))
    paciente = cursor.fetchone()
    columns = [column[0] for column in cursor.description]
    paciente = dict(zip(columns, paciente))
    cursor.close()
    connection.close()
    return paciente

@app.route('/agregar-direccion/<id_paciente>', methods=['GET', 'POST'])
def agregar_direccion_paciente(id_paciente):
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
        
        return render_template('MostrarDireccionesPacientes.html', paciente=paciente, mensaje="Dirección agregada con éxito")
    else:
        paciente = obtener_paciente_por_id(id_paciente)
        return render_template('MostrarDireccionesPacientes.html', paciente=paciente)

@app.route('/paciente/direcciones/editar/<int:id_paciente>/<int:id_direccion>', methods=['GET', 'POST'])
def editar_direccion_paciente(id_paciente, id_direccion):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        
        query_mostrar = """
            SELECT d.* 
            FROM t_01paciente p 
            INNER JOIN t_02direccionpaciente d ON p.Id_paciente = d.id_paciente 
            WHERE p.Id_paciente = %s AND d.id_direccion = %s
        """
        params_mostrar = (id_paciente, id_direccion)
        
        cursor.execute(query_mostrar, params_mostrar)
        
        resultado = cursor.fetchone()
        
        direccion = dict(zip([column[0] for column in cursor.description], resultado))
        
        cursor.close()
        connection.close()
        
        return render_template('editar_direccion_paciente.html', direccion=direccion)
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return "Error"

@app.route('/paciente/direcciones/actualizar/<int:id_paciente>/<int:id_direccion>', methods=['POST'])
def actualizar_direccion_paciente(id_paciente, id_direccion):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        
        # Obtener los datos del formulario
        direccion = request.form['direccion']
        ciudad = request.form['ciudad']
        estado = request.form['estado']
        codigo_postal = request.form['codigo_postal']
        
        # Actualizar la dirección en la base de datos
        query_actualizar = """
            UPDATE t_02direccionpaciente
            SET direccion = %s, ciudad = %s, estado = %s, codigo_postal = %s
            WHERE id_paciente = %s AND id_direccion = %s
        """
        params_actualizar = (direccion, ciudad, estado, codigo_postal, id_paciente, id_direccion)
        
        cursor.execute(query_actualizar, params_actualizar)
        connection.commit()
        
        cursor.close()
        connection.close()
        
        # Redireccionar a la página de direcciones del paciente
        return render_template('MostrarDireccionesPacientes.html', id_paciente=id_paciente)
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return "Error"

@app.route('/paciente/direcciones/eliminar/<int:id_paciente>/<int:id_direccion>', methods=['POST'])
def eliminar_direccion_paciente(id_paciente, id_direccion):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        
        query_eliminar = """
            DELETE FROM t_02direccionpaciente
            WHERE id_paciente = %s AND id_direccion = %s
        """
        params_eliminar = (id_paciente, id_direccion)
        
        cursor.execute(query_eliminar, params_eliminar)
        connection.commit()
        
        cursor.close()
        connection.close()
        
        return render_template('MostrarDireccionesPacientes.html', id_paciente=id_paciente)
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return render_template('MostrarDireccionesPacientes.html', id_paciente=id_paciente)   


@app.route('/paciente/historial_educacion/<int:id_paciente>', methods=['GET', 'POST'])
def historial_educacion(id_paciente):
    # Obtener datos del paciente
    paciente = obtener_paciente_por_id(id_paciente)
    print("Paciente:", paciente)
    
    # Obtener registros de historial educativo
    registros = obtener_historial_educativo(id_paciente)
    print("Registros:", registros)
    
    return render_template('HistorialEducativoPaciente.html', paciente=paciente, registros=registros)

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
    resultados = cursor.fetchall()
    
    print(resultados)  # Imprimir los resultados en la consola
    
    # Procesar resultados
    if resultados:
        campos = [column[0] for column in cursor.description]
        respuesta = [dict(zip(campos, row)) for row in resultados]
    else:
        respuesta = []
    
    # Cerrar cursor y conexión
    cursor.close()
    connection.close()
    
    return respuesta

def obtener_registro_por_id(id_historial):
    # Cursor para ejecutar consultas
    connection = get_connection()
    cursor = connection.cursor()
    
    # Consulta SQL
    query = """
    SELECT 
        he.id_historial, 
        he.id_paciente, 
        he.id_institucion, 
        he.adaptacion, 
        he.relacion_docentes, 
        he.relacion_compañeros, 
        he.repitencia_escolar, 
        he.cambios_escuelas, 
        he.cambios_maestros
    FROM 
        t_10historialeducativo he
    WHERE 
        he.id_historial = %s
"""
    
    # Ejecutar consulta
    cursor.execute(query, (id_historial,))
    
    # Obtener resultados
    resultado = cursor.fetchone()
    
    # Cerrar cursor y conexión
    cursor.close()
    connection.close()
    
    return resultado

@app.route('/agregar-historial-educativo/<int:id_paciente>', methods=['POST'])
def agregar_historial_educativo(id_paciente):
    # Obtener datos del formulario
    id_institucion = request.form['id_institucion']
    adaptacion = request.form['adaptacion']
    relacion_docentes = request.form['relacion_docentes']
    relacion_compañeros = request.form['relacion_compañeros']
    repitencia_escolar = request.form['repitencia_escolar']
    cambios_escuelas = request.form['cambios_escuelas']
    cambios_maestros = request.form['cambios_maestros']

    # Conectar a la base de datos
    connection = get_connection()
    cursor = connection.cursor()

    # Consulta SQL para insertar datos
    query = """
        INSERT INTO t_10historialeducativo (
            id_paciente,
            id_institucion,
            adaptacion,
            relacion_docentes,
            relacion_compañeros,
            repitencia_escolar,
            cambios_escuelas,
            cambios_maestros
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    # Ejecutar consulta
    cursor.execute(query, (
        id_paciente,
        id_institucion,
        adaptacion,
        relacion_docentes,
        relacion_compañeros,
        repitencia_escolar,
        cambios_escuelas,
        cambios_maestros
    ))

    # Commit cambios
    connection.commit()

    # Cerrar cursor y conexión
    cursor.close()
    connection.close()

    # Obtener datos del paciente
    paciente = obtener_paciente_por_id(id_paciente)

    # Obtener registros de historial educativo
    registros = obtener_historial_educativo(id_paciente)

    # Redireccionar a la página de historial educativo
    return render_template('HistorialEducativoPaciente.html', paciente=paciente, registros=registros)

# NO FUNCIONA EDITAR HISTORIAL EDUCATIVO HAY QUE VER QUE PASA 
@app.route('/historial-educativo/editar/<int:id_historial>', methods=['GET'])
def editar_historial_educativo(id_historial):
    print("ID Historial:", id_historial)
    registro = obtener_registro_por_id(id_historial)
    print("Registro:", registro)
    return render_template('editar_historial_educativo_paciente.html', registro=registro)

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
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        dni = request.form['dni']
        id_genero = request.form['id_genero']
        fecha_nacimiento = request.form['fecha_nacimiento']
        fecha_registro = request.form['fecha_registro']
        observaciones = request.form['observaciones']
        id_padre = request.form['id_padre']

        cursor.execute("UPDATE t_01paciente SET nombre=%s, apellido=%s, DNI=%s, id_genero=%s, fecha_nacimiento=%s, fecha_registro=%s, observaciones=%s, id_padre=%s WHERE id_paciente=%s", 
                (nombre, apellido, dni, id_genero, fecha_nacimiento, fecha_registro, observaciones, id_padre, id_paciente))
        connection.commit()
        connection.close()
        return render_template('editar_paciente.html')

    
    paciente = obtener_paciente_por_id(id_paciente)
    if paciente is None:
        return 'Paciente no encontrado', 404
    print(paciente)
    return render_template('editar_paciente.html', paciente=paciente)

@app.route('/paciente/<int:id_paciente>/datos_gestacion', methods=['GET'])
def mostrar_datos_gestacion(id_paciente):
    datos_gestacion = obtener_datos_gestacion(id_paciente)
    return render_template('DatosGestacion.html', datos_gestacion=datos_gestacion)


def obtener_datos_gestacion(id_paciente):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT 
                e.id_embarazo, 
                e.id_paciente, 
                tp.tipo AS tipo_parto, 
                e.inicio_del_embarazo, 
                e.fecha_fin_del_embarazo, 
                e.semana_gestacion, 
                e.peso_al_nacer,
                en.enfermedad
            FROM 
                t_06datosembarazo e
            LEFT JOIN 
                t_08tipoparto tp ON e.id_tipo_parto = tp.id_tipo_parto
            LEFT JOIN 
                t_09enfermedadesembarazo en ON e.id_embarazo = en.id_embarazo
            WHERE 
                e.id_paciente = %s
        """, (id_paciente,))
        datos_gestacion = cursor.fetchall()
        return [dict(zip([column[0] for column in cursor.description], row)) for row in datos_gestacion]
    except Exception as e:
        print(f"Error al obtener datos de gestación: {e}")
        return []

@app.route('/registrar-embarazo', methods=['POST'])
def agregar_embarazo():
    try:
        datos_embarazo = {
            'inicio_del_embarazo': request.form['inicio_del_embarazo'],
            'fecha_fin_del_embarazo': request.form['fecha_fin_del_embarazo'],
            'semana_gestacion': request.form['semana_gestacion'],
            'peso_al_nacer': request.form['peso_al_nacer'],
            'id_tipo_parto': request.form['id_tipo_parto'],
            'enfermedad': request.form['enfermedad']
        }
        
        if not validar_datos(datos_embarazo):
            print("Datos inválidos:", datos_embarazo)
            return "Datos inválidos: " + str(datos_embarazo), 400
        
        connection = get_connection()
        cursor = connection.cursor()
        
        cursor.execute("""
            INSERT INTO t_06datosembarazo 
            (inicio_del_embarazo, fecha_fin_del_embarazo, semana_gestacion, peso_al_nacer, id_tipo_parto)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            datos_embarazo['inicio_del_embarazo'],
            datos_embarazo['fecha_fin_del_embarazo'],
            datos_embarazo['semana_gestacion'],
            datos_embarazo['peso_al_nacer'],
            datos_embarazo['id_tipo_parto']
        ))
        
        id_embarazo = cursor.lastrowid
        
        enfermedad = datos_embarazo['enfermedad'] if datos_embarazo['enfermedad'].strip() != "" else "Ninguna"
        cursor.execute("""
            INSERT INTO t_09enfermedadesembarazo 
            (id_embarazo, enfermedad)
            VALUES (%s, %s)
        """, (id_embarazo, enfermedad))
        
        connection.commit()
        connection.close()
        
        return "Embarazo registrado correctamente"
    except Exception as e:
        print(f"Error al registrar embarazo: {e}")
        return "Error al registrar embarazo", 500


def validar_datos(datos):
    if not validar_fecha(datos['inicio_del_embarazo']) or not validar_fecha(datos['fecha_fin_del_embarazo']):
        return False
    
    if not datos['semana_gestacion'].isdigit() or not datos['peso_al_nacer'].replace('.', '', 1).isdigit():
        return False
    
    if not datos['id_tipo_parto'].isdigit():
        return False
    
    # Permitir que el campo "enfermedad" esté vacío
    if len(datos['enfermedad']) < 3 and datos['enfermedad'].strip() != "":
        return False
    
    return True


def validar_fecha(fecha):
    try:
        datetime.strptime(fecha, '%Y-%m-%d')
        return True
    except ValueError:
        return False

    
 # Este codigo de editar del embarazo no funciona no tiene formulario

@app.route('/embarazo/editar/<int:embarazo_id>', methods=['GET', 'POST'])
def editar_embarazo(embarazo_id):
    datos_embarazo = obtener_datos_gestacion(embarazo_id)
    
    if request.method == 'POST':
        print(request.form)  # Agregar print aquí
        # Procesar los datos del formulario
        inicio_del_embarazo = request.form['inicio_del_embarazo']
        fecha_fin_del_embarazo = request.form['fecha_fin_del_embarazo']
        tipo_parto = request.form['tipo_parto']
        semana_gestacion = request.form['semana_gestacion']
        peso_al_nacer = request.form['peso_al_nacer']
        enfermedad = request.form['enfermedad']
        
        connection = get_connection()
        cursor = connection.cursor()

        query = "UPDATE t_embarazos SET inicio_del_embarazo = %s, fecha_fin_del_embarazo = %s, tipo_parto = %s, semana_gestacion = %s, peso_al_nacer = %s, enfermedad = %s WHERE id_embarazo = %s"
        cursor.execute(query, (inicio_del_embarazo, fecha_fin_del_embarazo, tipo_parto, semana_gestacion, peso_al_nacer, enfermedad, embarazo_id))
        connection.commit()
        
        # Obtener los datos actualizados
        datos_embarazo = obtener_datos_gestacion(embarazo_id)
        
        return render_template('EditarEmbarazo.html', embarazo=datos_embarazo[0])
    
    else:
        # Renderizar el formulario para edición
        return render_template('EditarEmbarazo.html', embarazo=datos_embarazo[0])

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

@app.route('/buscarPaciente', methods=['POST'])
def buscar_paciente():
    parametro = request.form['parametro']
    buscar = request.form['buscar']

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT 
            p.Id_paciente, 
            p.Nombre, 
            p.Apellido, 
            p.DNI, 
            g.Nombre AS Genero, 
            p.Fecha_nacimiento, 
            p.Fecha_registro, 
            p.Observaciones
        FROM 
            t_01paciente p 
        JOIN 
            t_02genero g ON p.Id_genero = g.Id_genero
        WHERE 
            p.{} LIKE '%{}%'
    """.format(parametro, buscar)

    cursor.execute(query)
    resultados = cursor.fetchall()

    # Convertir resultados a diccionario
    resultados = [dict(zip([column[0] for column in cursor.description], row)) for row in resultados]

    # Agregar una columna adicional para la edad
    for paciente in resultados:
        paciente['edad'] = calcular_edad_pacientes(paciente['Fecha_nacimiento'])

    return render_template('busqueda_paciente.html', pacientes=resultados)

if __name__ == '__main__':
    app.run()