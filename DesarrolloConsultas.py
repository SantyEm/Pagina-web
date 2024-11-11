from flask import Flask, render_template, request, redirect, url_for, send_file

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from flask import send_file

from conexion import get_connection

app = Flask(__name__)
@app.route('/Desarrollo')
def mostrar_desarrollo():
    sesiones = obtener_sesiones()
    pacientes = obtener_pacientes()
    print("Pacientes:", pacientes)  # Verifica si hay pacientes
    return render_template('DesarrolloFormulario.html', sesiones=sesiones, pacientes=pacientes)

def obtener_sesiones():
    connection = get_connection()
    cursor = connection.cursor()
    
    query = """
        SELECT 
            s.id_sesiones,
            s.id_paciente, 
            p.nombre,
            p.apellido,
            s.fecha_sesion,
            s.hora_sesion,
            s.duracion,
            ts.nombre_tipo,
            dps.descripcion AS descripcion_psicomotor,
            dl.descripcion AS descripcion_lenguaje,
            s.observacion
        FROM 
            t_13datosesion s
        INNER JOIN 
            t_01paciente p ON s.id_paciente = p.id_paciente
        INNER JOIN 
            t_14tipossesion ts ON s.id_tipo_sesion = ts.id_tipo_sesion
        INNER JOIN 
            t_16desarrollopsicomotor dps ON s.id_desarrollo_psicomotor = dps.id_desarrollo_psicomotor
        INNER JOIN 
            t_15desarrollolenguaje dl ON s.id_desarrollo_lenguaje = dl.id_desarrollo_lenguaje
        WHERE 
            s.id_sesiones = (SELECT MAX(id_sesiones) 
                            FROM t_13datosesion 
                            WHERE id_paciente = s.id_paciente)
    """
    
    cursor.execute(query)
    sesiones = cursor.fetchall()
    sesiones = [dict(zip([column[0] for column in cursor.description], row)) for row in sesiones]
    
    cursor.close()
    connection.close()
    return sesiones

@app.route('/agregar-sesion', methods=['POST'])
def agregar_sesiones():
    print("Llegó a la ruta /agregar-sesion")
    print(request.form)
    
    id_paciente = request.form['id_paciente']
    fecha_sesion = request.form['fecha_sesion']
    hora_sesion = request.form['hora_sesion']
    duracion = request.form['duracion']
    id_tipo_sesion = request.form['id_tipo_sesion']
    id_desarrollo_psicomotor = request.form['id_desarrollo_psicomotor']
    id_desarrollo_lenguaje = request.form['id_desarrollo_lenguaje']
    observacion = request.form['observacion']
    
    connection = get_connection()
    print("Conexión a la base de datos establecida")
    cursor = connection.cursor()
    
    query = """
        INSERT INTO t_13datosesion (
            id_paciente,
            fecha_sesion,
            hora_sesion,
            duracion,
            id_tipo_sesion,
            id_desarrollo_psicomotor,
            id_desarrollo_lenguaje,
            observacion
        ) VALUES (
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s
        )
    """
    cursor.execute(query, (
        id_paciente,
        fecha_sesion,
        hora_sesion,
        duracion,
        id_tipo_sesion,
        id_desarrollo_psicomotor,
        id_desarrollo_lenguaje,
        observacion
    ))
    
    connection.commit()
    cursor.close()
    connection.close()
    
    return redirect(url_for('mostrar_desarrollo'))

@app.route('/historial/<int:id_paciente>', methods=['GET'])
def mostrar_historial(id_paciente):
    sesiones = obtener_sesiones_historial(id_paciente)
    print("Pacientes:", sesiones)  # Verifica si hay pacientes
    return render_template('HistorialDesarrollo.html', sesiones=sesiones, id_paciente=id_paciente)

def obtener_sesiones_historial(id_paciente):
    connection = get_connection()
    cursor = connection.cursor()
    
    query = """
                SELECT 
                s.id_sesiones,
                p.nombre,
                p.apellido,
                s.fecha_sesion,
                s.hora_sesion,
                s.duracion,
                ts.nombre_tipo,
                dps.descripcion AS descripcion_psicomotor,
                dl.descripcion AS descripcion_lenguaje,
                s.observacion
            FROM 
                t_13datosesion s
            INNER JOIN 
                t_01paciente p ON s.id_paciente = p.id_paciente
            INNER JOIN 
                t_14tipossesion ts ON s.id_tipo_sesion = ts.id_tipo_sesion
            INNER JOIN 
                t_16desarrollopsicomotor dps ON s.id_desarrollo_psicomotor = dps.id_desarrollo_psicomotor
            INNER JOIN 
                t_15desarrollolenguaje dl ON s.id_desarrollo_lenguaje = dl.id_desarrollo_lenguaje
            WHERE 
                s.id_paciente = %s
            ORDER BY 
                s.fecha_sesion DESC
    """
    
    cursor.execute(query, (id_paciente,))
    sesiones = cursor.fetchall()
    sesiones = [dict(zip([column[0] for column in cursor.description], row)) for row in sesiones]
    
    cursor.close()
    connection.close()
    return sesiones

def obtener_pacientes():
    connection = get_connection()
    cursor = connection.cursor()
    
    query = "SELECT Id_paciente, Nombre, Apellido FROM t_01paciente"
    
    cursor.execute(query)
    pacientes = cursor.fetchall()
    pacientes = [dict(zip([column[0] for column in cursor.description], row)) for row in pacientes]
    
    cursor.close()
    connection.close()
    return pacientes

# editar
@app.route('/sesion/editar/<int:id_sesion>', methods=['GET'])
def obtener_sesion(id_sesion):
    connection = get_connection()
    cursor = connection.cursor()
    query = """
        SELECT 
            s.id_sesiones,
            s.id_paciente, 
            p.nombre,
            p.apellido,
            s.fecha_sesion,
            s.hora_sesion,
            s.duracion,
            ts.nombre_tipo,
            dps.descripcion AS descripcion_psicomotor,
            dl.descripcion AS descripcion_lenguaje,
            s.observacion
        FROM 
            t_13datosesion s
        INNER JOIN 
            t_01paciente p ON s.id_paciente = p.id_paciente
        INNER JOIN 
            t_14tipossesion ts ON s.id_tipo_sesion = ts.id_tipo_sesion
        INNER JOIN 
            t_16desarrollopsicomotor dps ON s.id_desarrollo_psicomotor = dps.id_desarrollo_psicomotor
        INNER JOIN 
            t_15desarrollolenguaje dl ON s.id_desarrollo_lenguaje = dl.id_desarrollo_lenguaje
        WHERE 
            s.id_sesiones = %s
    """
    cursor.execute(query, (id_sesion,))
    sesion = cursor.fetchone()
    sesion = dict(zip([column[0] for column in cursor.description], sesion))
    cursor.close()
    connection.close()
    return render_template('editar_sesion.html', sesion=sesion)

@app.route('/sesion/actualizar/<int:id_sesion>', methods=['POST'])
def actualizar_sesion(id_sesion):
    print(request.form)
    # Obtener los datos del formulario
    fecha_sesion = request.form['fecha_sesion']
    hora_sesion = request.form['hora_sesion']
    duracion = request.form['duracion']
    id_tipo_sesion = request.form['id_tipo_sesion']
    id_desarrollo_psicomotor = request.form['id_desarrollo_psicomotor']
    id_desarrollo_lenguaje = request.form['id_desarrollo_lenguaje']
    observacion = request.form['observacion']

    # Actualizar los datos en la base de datos
    connection = get_connection()
    cursor = connection.cursor()
    query = """
        UPDATE t_13datosesion 
        SET 
            fecha_sesion = %s, 
            hora_sesion = %s, 
            duracion = %s,
            id_tipo_sesion = %s,
            id_desarrollo_psicomotor = %s,
            id_desarrollo_lenguaje = %s,
            observacion = %s
        WHERE 
            id_sesiones = %s
    """
    cursor.execute(query, (
        fecha_sesion, 
        hora_sesion, 
        duracion, 
        id_tipo_sesion, 
        id_desarrollo_psicomotor, 
        id_desarrollo_lenguaje, 
        observacion, 
        id_sesion
    ))
    connection.commit()
    cursor.close()
    connection.close()

    # Redireccionar a la página de historial
    return render_template('HistorialDesarrollo.html')

@app.route('/sesion/eliminar/<int:id_sesion>', methods=['POST'])
def eliminar_sesion(id_sesion):
    # Conexión a la base de datos
    connection = get_connection()
    cursor = connection.cursor()
    
    # Query para eliminar la sesión
    query = "DELETE FROM t_13datosesion WHERE id_sesiones = %s"
    cursor.execute(query, (id_sesion,))
    
    # Commit y cierre de la conexión
    connection.commit()
    cursor.close()
    connection.close()
    
    # Redirección a la página de historial
    return render_template('HistorialDesarrollo.html')

# falta pulir cosas en editar

@app.route('/busqueda_sesiones', methods=['POST'])
def buscar_sesiones():
    parametro = request.form['parametro']
    buscar = request.form['buscar']
    
    connection = get_connection()
    cursor = connection.cursor()
    
    query = """
        SELECT 
            s.id_sesiones,
            p.nombre,
            p.apellido,
            s.fecha_sesion,
            s.hora_sesion,
            s.duracion,
            ts.nombre_tipo,
            dps.descripcion AS descripcion_psicomotor,
            dl.descripcion AS descripcion_lenguaje,
            s.observacion
        FROM 
            t_13datosesion s
        INNER JOIN 
            t_01paciente p ON s.id_paciente = p.id_paciente
        INNER JOIN 
            t_14tipossesion ts ON s.id_tipo_sesion = ts.id_tipo_sesion
        INNER JOIN 
            t_16desarrollopsicomotor dps ON s.id_desarrollo_psicomotor = dps.id_desarrollo_psicomotor
        INNER JOIN 
            t_15desarrollolenguaje dl ON s.id_desarrollo_lenguaje = dl.id_desarrollo_lenguaje
        WHERE 
            p.{} LIKE '%{}%'
    """.format(parametro, buscar)
    
    cursor.execute(query)
    resultados = cursor.fetchall()
    
    # Convertir resultados a diccionario
    resultados = [dict(zip([column[0] for column in cursor.description], row)) for row in resultados]
    
    return render_template('busqueda_sesiones.html', sesiones=resultados)

# exportar datos de la tabla a pdf
@app.route('/exportar_todo/<int:id_paciente>')
def exportar_todo(id_paciente):
    sesiones = obtener_sesiones_historial(id_paciente)

    datos = []
    for sesion in sesiones:
        datos.append([
            sesion['fecha_sesion'],
            sesion['hora_sesion'],
            sesion['duracion'],
            sesion['nombre_tipo'],
            sesion['descripcion_psicomotor'],
            sesion['descripcion_lenguaje'],
            sesion['observacion'],
            ""  # Acciones
        ])

    # Código para crear el PDF
    pdf = SimpleDocTemplate("HistorialPaciente.pdf", pagesize=letter)

    # Estilos de la tabla
    estilos = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('TOPPADDING', (0, 1), (-1, -1), 12),
    ])

    # Creamos la tabla
    tabla = Table(datos, style=estilos)

    # Agregamos la tabla al PDF
    pdf.build([tabla])

    return send_file("HistorialPaciente.pdf", as_attachment=True)

if __name__ == '__main__':
    app.run()