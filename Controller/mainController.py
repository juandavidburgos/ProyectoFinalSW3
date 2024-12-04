#Controlador principal : pagina index
from flask import Blueprint, render_template

# Crear un blueprint para el controlador principal
main_bp = Blueprint('main',__name__)
#Ruta para la pagina principal
@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/coordinator')
def mainCoordinator():
    return render_template('coordinator/mainCoordinator.html', active_view='coordinator')

@main_bp.route('/teacher')
def mainTeacher():
    return render_template('Teacher/mainTeacher.html',active_view='teacher')

@main_bp.route('/evaluator')
def mainEvaluator():
    return render_template('Evaluator/mainEvaluator.html',active_view='evaluator')