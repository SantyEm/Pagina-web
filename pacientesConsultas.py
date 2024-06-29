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

    # Cerrar el cursor y la conexión
    cursor.close()
    connection.close()

    # Renderizar la plantilla y pasar la variable pacientes como contexto
    return render_template('PacienteFormulario.html', pacientes=pacientes)

if __name__ == '__main__':
    app.run()