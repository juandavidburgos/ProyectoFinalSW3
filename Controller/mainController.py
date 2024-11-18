#Controlador principal : pagina index
from flask import Blueprint, render_template

# Crear un blueprint para el controlador principal
main_bp = Blueprint('main',__name__)
#Ruta para la pagina principal
@main_bp.route('/')
def index():
    return render_template('index.html')
