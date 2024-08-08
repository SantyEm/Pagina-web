from flask import Flask, render_template
from conexion import get_connection
from flask import request
from flask import session
from flask import current_app

app = Flask(__name__)
