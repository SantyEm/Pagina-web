from flask import Flask, render_template, request
from LoginConsultas import process_login

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    return process_login()

if __name__ == '__main__':
    app.run(debug=True)
