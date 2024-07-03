from flask import Flask, render_template
from conexion import get_connection

app = Flask(__name__)

@app.route('/pacientes')
def mostrar_pacientes():
    # Obtener la conexión y el cursor
    connection = get_connection()
    cursor = connection.cursor()

    # Realizar la consulta de los pacientes con la tabla de género
    cursor.execute("SELECT p.Nombre, p.Apellido, p.DNI, g.Nombre AS Genero, p.Fecha_nacimiento, p.Fecha_registro, p.Observaciones FROM t_01paciente p JOIN t_02genero g ON p.Id_genero = g.Id_genero")

    # Obtener los resultados de la consulta
    pacientes = cursor.fetchall()
    
    # Convertir los resultados a diccionarios si es necesario
    pacientes = [dict(zip([column[0] for column in cursor.description], row)) for row in pacientes]
    
    # Cerrar el cursor y la conexión
    cursor.close()
    connection.close()

    # Renderizar la plantilla y pasar la variable pacientes como contexto
    return render_template('PacienteFormulario.html', pacientes=pacientes)


@app.route('/ver_direcciones/<int:id_paciente>', methods=['GET'])
def ver_direcciones(id_paciente):
    # Aquí puedes implementar la lógica para obtener las direcciones del paciente con el ID recibido
    # Ejemplo básico de conexión a la base de datos y consulta
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT ciudad, estado, codigo_postal FROM t_02direccionpaciente WHERE id_paciente = %s", (id_paciente,))
    direcciones = cursor.fetchall()
    cursor.close()
    connection.close()

    # Renderizar la plantilla y pasar las direcciones como contexto
    return render_template('PacienteFormulario.html', direcciones=direcciones)



if __name__ == '__main__':
    app.run()