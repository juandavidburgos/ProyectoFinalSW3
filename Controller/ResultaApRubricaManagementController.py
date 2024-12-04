#Conecta Rubrica con Resultado de aprendizaje 
from flask import Blueprint, render_template, request, redirect, url_for, flash
from Services.ResultaApRubricaService import ResultaApRubricaService

# Crear un blueprint para el controlador de resultados de aprendizaje
resultaApRubric = Blueprint('learning_outcome', __name__)

@resultaApRubric.route('/create_RARubric', methods=['GET', 'POST'])
def create_RA_Rubric():
    print("crear")