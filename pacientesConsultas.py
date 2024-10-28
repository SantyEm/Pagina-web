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
    cursor.execute("DELETE FROM pacientes WHERE id_paciente = %s", (id_paciente,))
    connection.commit()
    return render_template('PacienteFormulario.html')

if __name__ == '__main__':
    app.run()