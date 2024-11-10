from flask import Flask, render_template
from conexion import get_connection
from flask import request
from datetime import datetime
from flask import flash

app = Flask(__name__)

def calcular_edad(fecha_nacimiento):
    hoy = datetime.today()
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad

@app.route('/padres')
def mostrar_padres():
    padres = obtener_padres()
    return render_template('PadresFormulario.html', padres=padres)

@app.route('/padre/direcciones/<int:id_padre>', methods=['GET'])
def mostrar_direcciones_padre(id_padre):
    # Obtener las direcciones del padre con el ID especificado
    direcciones = obtener_direcciones_padre(id_padre)
    # Renderizar la plantilla con la tabla de direcciones
    print(obtener_direcciones_padre(id_padre))
    return render_template('MostrarDireccionesPadres.html', direcciones=direcciones, id_padre=id_padre)

def obtener_direcciones_padre(id_padre):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        
        cursor.execute("""
            SELECT d.*, ev.estado_vivienda 
            FROM t_04direccionpadre d 
            INNER JOIN t_12estadovivienda ev ON d.id_estado_vivienda = ev.id_estado 
            WHERE d.Id_padre = %s
        """, (id_padre,))
        
        direcciones = cursor.fetchall()
        
        if direcciones is None:
            return []
        
        return [dict(zip([column[0] for column in cursor.description], row)) for row in direcciones]
    
    except Exception as e:
        print(f"Error al obtener direcciones: {e}")
        return []
    
@app.route('/direcciones/editar/<int:id_direccion>', methods=['GET', 'POST'])
def editar_direccion(id_direccion):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        
        # Consulta para mostrar los datos de la dirección
        query_mostrar = """
            SELECT d.*, ev.estado_vivienda 
            FROM t_04direccionpadre d 
            INNER JOIN t_12estadovivienda ev ON d.id_estado_vivienda = ev.id_estado 
            WHERE d.id_direccion = %s
        """
        params_mostrar = (id_direccion,)
        
        cursor.execute(query_mostrar, params_mostrar)
        
        direccion = cursor.fetchone()
        result = dict(zip([column[0] for column in cursor.description], direccion)) if direccion else None
        
        cursor.close()
        connection.close()
        
        return render_template('editar_direccion_padre.html', direccion=result, id_direccion=id_direccion)
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return "Error"
    
@app.route('/direcciones/actualizar/<int:id_direccion>', methods=['POST'])
def actualizar_direccion(id_direccion):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        
        # Consulta para actualizar los datos de la dirección
        query_actualizar = """
            UPDATE t_04direccionpadre 
            SET direccion = %s, ciudad = %s, id_estado_vivienda = %s 
            WHERE id_direccion = %s
        """
        params_actualizar = (
            request.form['direccion'],
            request.form['ciudad'],
            request.form['estado'],
            id_direccion
        )
        
        cursor.execute(query_actualizar, params_actualizar)
        connection.commit()
        
        cursor.close()
        connection.close()
        
        return render_template('MostrarDireccionesPadres.html', id_direccion=id_direccion, mensaje="Dirección actualizada con éxito")
    
    except Exception as e:
        return f"Error: {str(e)}"
    
@app.route('/direcciones/eliminar/<int:id_direccion>', methods=['POST'])
def eliminar_direccion(id_direccion):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        
        query_eliminar = "DELETE FROM t_04direccionpadre WHERE id_direccion = %s"
        params_eliminar = (id_direccion,)
        
        cursor.execute(query_eliminar, params_eliminar)
        connection.commit()
        
        cursor.close()
        connection.close()
        
        # Consulta para obtener las direcciones actualizadas
        connection = get_connection()
        cursor = connection.cursor()
        
        query_direcciones = """
            SELECT d.*, ev.estado_vivienda 
            FROM t_04direccionpadre d 
            INNER JOIN t_12estadovivienda ev ON d.id_estado_vivienda = ev.id_estado
        """
        
        cursor.execute(query_direcciones)
        
        direcciones = cursor.fetchall()
        result = [dict(zip([column[0] for column in cursor.description], row)) for row in direcciones]
        
        cursor.close()
        connection.close()
        
        return render_template('MostrarDireccionesPadres.html', mensaje="Dirección eliminada con éxito")
    
    except Exception as e:
        return f"Error: {str(e)}"
    
    
def obtener_padres():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
        SELECT 
            p.Id_padre, 
            p.Nombres, 
            p.Apellido, 
            p.Telefono, 
            p.Ocupacion, 
            e.nivel, 
            p.Fecha_nacimiento, 
            p.tipo_relacion 
        FROM 
            t_03padres_madres p 
        LEFT JOIN 
            t_05niveleseducacion e 
        ON 
            p.id_nivel_educacion = e.id_nivel
    ''')
    padres = cursor.fetchall()
    padres = [dict(zip([column[0] for column in cursor.description], row)) for row in padres]

    # Agregar una columna adicional para la edad
    for padre in padres:
        padre['edad'] = calcular_edad(padre['Fecha_nacimiento'])

    cursor.close()
    connection.close()
    return padres


@app.route('/agregar-padre', methods=['POST'])
def agregar_padre_registro():
        # Obtener la conexión y el cursor
        connection = get_connection()
        cursor = connection.cursor()

        # Obtener los datos del formulario
        nombres = request.form['nombres']
        apellido = request.form['apellido']
        telefono = request.form['telefono']
        ocupacion = request.form['ocupacion']
        nivel_educacion = request.form['nivel_educacion']
        fecha_nacimiento = request.form['fecha_nacimiento']
        tipo_relacion = request.form['tipo_relacion']

        # Validar los datos
        if not nombres or not apellido or not ocupacion or not nivel_educacion:
            return 'Faltan datos', 400

        # Obtener el Id_nivel correspondiente al nivel de educación seleccionado
        cursor.execute("SELECT id_nivel FROM t_05niveleseducacion WHERE id_nivel = %s", (nivel_educacion,))
        resultado = cursor.fetchone()
        if resultado is not None:
            id_nivel = resultado[0]
        else:
        # Manejar el caso en que no se encontró ningún resultado
             id_nivel = None

        # Convertir la fecha de nacimiento a un objeto datetime
        fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')

        # Calcular la edad
        edad = datetime.now().year - fecha_nacimiento.year - ((datetime.now().month, datetime.now().day) < (fecha_nacimiento.month, fecha_nacimiento.day))

        # Agregar el padre a la base de datos
        cursor.execute("INSERT INTO t_03padres_madres(Nombres, Apellido, Telefono, Ocupacion, id_nivel_educacion, Fecha_nacimiento) VALUES (%s, %s, %s, %s, %s, %s)", (nombres, apellido, telefono, ocupacion, id_nivel, fecha_nacimiento))
        connection.commit()

        # Obtener el ID del padre recién agregado
        padre_id = cursor.lastrowid
        
       # Obtener el id_tipo_relacion correspondiente al tipo de relación seleccionado
        cursor.execute("SELECT id_tipo_relacion FROM t_04tipo_relacion WHERE descripcion = %s", (tipo_relacion,))
        resultado = cursor.fetchone()
        if resultado is not None:
            id_tipo_relacion = resultado[0]
        else:
            # Manejar el caso en que no se encontró ningún resultado
            id_tipo_relacion = None
        print(tipo_relacion)

        padres = obtener_padres()
        # print(padres)  # Agregar este print
        return render_template('PadresFormulario.html', padres=padres)


@app.route('/direcciones/agregar/<id_padre>', methods=['POST'])
def agregar_direccion(id_padre):
    id_padre = request.form['id_padre']
    direccion = request.form['direccion']
    ciudad = request.form['ciudad']
    estado = request.form['estado']
    id_padre = request.form.get('id_padre', None)
    print("ID del padre:", id_padre)
    if id_padre is None or id_padre == '':
        return "Error: ID Padre no puede ser vacío"

    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO t_04direccionpadre (id_padre, direccion, ciudad, id_estado_vivienda)
            VALUES (%s, %s, %s, %s)
        """, (id_padre, direccion, ciudad, estado))

        connection.commit()
        return render_template("MostrarDireccionesPadres.html", mensaje='Direccion agregada correctamente. Puede cerrar esta pestaña.')

    except Exception as e:
        print(f"Error al agregar dirección: {e}")
        return "Error al agregar dirección"

    
    
@app.route('/eliminar_padre/<int:Id_padre>', methods=['POST'])
def eliminar_padre(Id_padre):
    print("Eliminando padre con ID:", Id_padre)
    
    # Conecta a la base de datos
    connection = get_connection()
    cursor = connection.cursor()
    
    # Elimina el registro en t_03padres_madres
    cursor.execute("DELETE FROM t_03padres_madres WHERE Id_padre = %s", (Id_padre,))
    
    # Elimina los registros relacionados en t_04direccionpadre
    cursor.execute("DELETE FROM t_04direccionpadre WHERE id_padre = %s", (Id_padre,))
    
    # Elimina los registros relacionados en t_06datosembarazo
    cursor.execute("DELETE FROM t_06datosembarazo WHERE id_paciente = (SELECT id_paciente FROM t_03padres_madres WHERE Id_padre = %s)", (Id_padre,))
    
    # Elimina los registros relacionados en t_09enfermedadesembarazo
    cursor.execute("DELETE FROM t_09enfermedadesembarazo WHERE id_embarazo IN (SELECT id_embarazo FROM t_06datosembarazo WHERE id_paciente = (SELECT id_paciente FROM t_03padres_madres WHERE Id_padre = %s))", (Id_padre,))
    
    # Confirma los cambios
    connection.commit()
    
    # Cierra la conexión
    cursor.close()
    connection.close()
    
    # Actualiza la lista de registros
    padres = obtener_padres()
    
    mensaje = 'Registro eliminado con éxito. Puede cerrar esta pestaña.'
    
    # Redirige a la página principal o muestra un mensaje de éxito
    return render_template('PadresFormulario.html', padres=padres)  # o return "Registro eliminado con éxito"

@app.route('/padre/editar/<int:padre_id>', methods=['GET', 'POST'])
def editar_padre(padre_id):
    print("ID recibido:", padre_id)
    padre = obtener_padre_especifico(padre_id)
    print(padre)  # Verifica que se esté obteniendo el padre correctamente
    if padre is None:
        return "Padre no encontrado", 404
    return render_template('EditarPadres.html', padre=padre)

def obtener_padre_especifico(id_padre):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
        SELECT 
            p.Id_padre, 
            p.Nombres, 
            p.Apellido, 
            p.Telefono, 
            p.Ocupacion, 
            e.nivel, 
            p.Fecha_nacimiento, 
            p.tipo_relacion 
        FROM 
            t_03padres_madres p 
        LEFT JOIN 
            t_05niveleseducacion e 
        ON 
            p.id_nivel_educacion = e.id_nivel 
        WHERE 
            p.Id_padre = %s
    ''', (id_padre,))
    padre = cursor.fetchone()
    if padre is None:
        return None
    return dict(zip([column[0] for column in cursor.description], padre))

@app.route('/editar-padre', methods=['POST'])
def editar_padre_form():
    id_padre = request.form['id_padre']  
    padre = obtener_padre_especifico(id_padre)
    if padre is None:
        return 'Padre no encontrado', 404

    nombres = request.form['nombres']
    apellido = request.form['apellido']
    telefono = request.form['telefono']
    ocupacion = request.form['ocupacion']
    fecha_nacimiento = request.form['fecha_nacimiento']
    nivel_educacion = request.form['nivel_educacion']
    tipo_relacion = request.form['tipo_relacion']

    connection = get_connection()
    cursor = connection.cursor()

    # Actualizar los datos del padre en la base de datos
    query = """
        UPDATE 
            t_03padres_madres 
        SET 
            Nombres = %s, 
            Apellido = %s, 
            Telefono = %s, 
            Ocupacion = %s, 
            Fecha_nacimiento = %s, 
            id_nivel_educacion = (SELECT id_nivel FROM t_05niveleseducacion WHERE nivel = %s), 
            tipo_relacion = %s 
        WHERE 
            Id_padre = %s
    """
    cursor.execute(query, (nombres, apellido, telefono, ocupacion, fecha_nacimiento, nivel_educacion, tipo_relacion, id_padre))
    connection.commit()

    cursor.close()
    connection.close()

    return render_template('PadresFormulario.html', mensaje='Edición exitosa. Puede cerrar esta pestaña.')

    # Código para manejar la búsqueda
@app.route('/buscar', methods=['POST'])
def buscar():
    buscar = request.form['buscar']
    parametro = request.form['parametro']

    connection = get_connection()
    cursor = connection.cursor()

    # Consulta SQL con filtro
    query = """
        SELECT p.Id_padre, p.Nombres, p.Apellido, p.Telefono, p.Ocupacion, e.nivel, p.Fecha_nacimiento, p.id_tipo_relacion 
        FROM t_03padres_madres p 
        LEFT JOIN t_05niveleseducacion e ON p.id_nivel_educacion = e.id_nivel 
        WHERE {} LIKE '%{}%'
    """.format(parametro, buscar)

    cursor.execute(query)
    resultados = cursor.fetchall()

    # Convertir resultados a diccionario
    resultados = [dict(zip([column[0] for column in cursor.description], row)) for row in resultados]

    # Agregar columna edad
    for resultado in resultados:
        resultado['edad'] = calcular_edad(resultado['Fecha_nacimiento'])

    cursor.close()
    connection.close()
    print(resultados)

    return render_template('BusquedaPadreFormulario.html', resultados=resultados)

if __name__ == '__main__':
    app.run()

