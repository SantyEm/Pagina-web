from flask import Flask, render_template
from conexion import get_connection
from flask import request
from datetime import datetime

from flask import session
from flask import current_app

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
    return render_template('MostrarDireccionesPadres.html', direcciones=direcciones)

def obtener_direcciones_padre(id_padre):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM t_04direccionpadre WHERE Id_padre = %s", (id_padre,))
        direcciones = cursor.fetchall()
        if direcciones is None:
            return []
        return [dict(zip([column[0] for column in cursor.description], row)) for row in direcciones]
    except Exception as e:
        print(f"Error al obtener direcciones: {e}")
        return []
    
def obtener_padres():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT p.Id_padre, p.Nombres, p.Apellido, p.Telefono, p.Ocupacion, e.nivel, p.Fecha_nacimiento FROM t_03padres p LEFT JOIN t_05niveleseducacion e ON p.id_nivel_educacion = e.id_nivel")
    padres = cursor.fetchall()
    padres = [dict(zip([column[0] for column in cursor.description], row)) for row in padres]

    # Agregar una columna adicional para la edad
    for padre in padres:
        padre['edad'] = calcular_edad(padre['Fecha_nacimiento'])
    cursor.close()
    connection.close()
    return padres

    
@app.route('/agregar-padre', methods=['POST'])
def agregar_padre():
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

        # Validar los datos
        if not nombres or not apellido or not ocupacion or not nivel_educacion:
            return 'Faltan datos', 400

        # Obtener el Id_nivel correspondiente al nivel de educación seleccionado
        cursor.execute("SELECT id_nivel FROM t_05niveleseducacion WHERE nivel = %s", (nivel_educacion,))
        resultado = cursor.fetchone()
        if resultado is not None:
            id_nivel = resultado[0]
        else:
        # Manejar el caso en que no se encontró ningún resultado
             id_nivel = None
        # o lanzar una excepción, dependiendo de la lógica de tu aplicación

        # Convertir la fecha de nacimiento a un objeto datetime
        fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')

        # Calcular la edad
        edad = datetime.now().year - fecha_nacimiento.year - ((datetime.now().month, datetime.now().day) < (fecha_nacimiento.month, fecha_nacimiento.day))

        # Agregar el padre a la base de datos
        cursor.execute("INSERT INTO t_03padres (Nombres, Apellido, Telefono, Ocupacion, id_nivel_educacion, Fecha_nacimiento) VALUES (%s, %s, %s, %s, %s, %s)", (nombres, apellido, telefono, ocupacion, id_nivel, fecha_nacimiento))
        connection.commit()

        # Obtener el ID del padre recién agregado
        padre_id = cursor.lastrowid

        # Agregar las direcciones del padre
        direcciones = request.form.getlist('direccion')
        for direccion in direcciones:
            cursor.execute("INSERT INTO t_04direccionpadre (Id_Padre, Direccion, Ciudad, Estado_Vivienda) VALUES (%s, %s, %s, %s)", (padre_id, direccion['direccion'], direccion['ciudad'], direccion['estado_vivienda']))
            connection.commit()

        padres = obtener_padres()
        print(padres)  # Agregar este print
        return render_template('PadresFormulario.html', padres=padres)
    
    
@app.route('/eliminar_padre/<int:Id_padre>', methods=['POST'])
def eliminar_padre(Id_padre):
    # Conecta a la base de datos
    connection = get_connection()
    cursor = connection.cursor()
    
    # Ejecuta la consulta para eliminar el registro
    cursor.execute("DELETE FROM t_03padres WHERE Id_padre = %s", (Id_padre,))
    
    # Confirma los cambios
    connection.commit()
    
    # Cierra la conexión
    cursor.close()
    connection.close()
    
    # Actualiza la lista de registros
    padres = obtener_padres()
    
    # Redirige a la página principal o muestra un mensaje de éxito
    return render_template('PadresFormulario.html', padres=padres)  # o return "Registro eliminado con éxito"


if __name__ == '__main__':
    app.run()

