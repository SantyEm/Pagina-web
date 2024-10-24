from flask import Flask, render_template
from conexion import get_connection

app = Flask(__name__)
@app.route('/Desarrollo')
def mostrar_desarrollo():
   
    return render_template('DesarrolloFormulario.html')

if __name__ == '__main__':
    app.run()