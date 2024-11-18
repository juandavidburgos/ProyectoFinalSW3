#Controlador gestion de asignaturas
# Aqui va el metodo que va a recibir los argumentos de los formularios de las vistas

from flask import Blueprint, render_template

# Crear un blueprint para el controlador principal
subject_bp = Blueprint('subject',__name__)
#Ruta para la pagina principal
@subject_bp.route('/add_subject')
def add():
    return render_template('index.html')