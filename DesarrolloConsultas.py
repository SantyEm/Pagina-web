from flask import Flask, render_template
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
    """
    
    cursor.execute(query)
    sesiones = cursor.fetchall()
    sesiones = [dict(zip([column[0] for column in cursor.description], row)) for row in sesiones]
    
    cursor.close()
    connection.close()
    return sesiones

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
            p.id_paciente = %s
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

if __name__ == '__main__':
    app.run()