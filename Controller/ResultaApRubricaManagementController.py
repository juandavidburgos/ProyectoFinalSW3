#Conecta Rubrica con Resultado de aprendizaje 
from flask import Blueprint, render_template, request, redirect, url_for, flash
from Services.ResultaApRubricaService import ResultaApRubricaService

# Crear un blueprint para el controlador de resultados de aprendizaje
resultaApRubric = Blueprint('learning_outcome', __name__)

@resultaApRubric.route('/create_RARubric', methods=['GET', 'POST'])
def create_RA_Rubric():
    """Ruta para crear un nuevo Resultado de Aprendizaje"""
    if request.method == 'POST':
        data = request.form.to_dict()
        # Llamar al servicio para crear el resultado de aprendizaje
        new_learning_outcome, error = ResultaApRubricaService.create_learning_outcome(data)

        if error:
            flash(error, 'error')
            return redirect(url_for('learning_outcome.create_learning_outcome'))

        flash('¡Resultado de Aprendizaje añadido satisfactoriamente!', 'success')
        return redirect(url_for('learning_outcome.create_learning_outcome'))

    return render_template('LearningOutcome/createLearningOutcome.html')

@resultaApRubric.route('/list_RARubric', methods=['GET', 'POST'])
def list_and_search_RA_Rubric():
    """Ruta para listar y buscar resultados de aprendizaje"""
    try:
        # Obtener todos los resultados de aprendizaje para mostrarlos en la tabla
        learning_outcomes, error = LearningOutcomeService.get_all_learning_outcomes()
        if error:
            flash(error, 'error')
            learning_outcomes = []

        # Si el método es POST, se intenta buscar un resultado de aprendizaje por ID
        if request.method == 'POST':
            lo_id = request.form.get('id')  # Capturar el ID enviado desde el formulario
            if not lo_id:
                flash("Por favor, ingrese el ID del resultado de aprendizaje.", "error")
                return render_template('LearningOutcome/listLearningOutcome.html', learning_outcomes=learning_outcomes)

            # Buscar resultado de aprendizaje por ID
            learning_outcome, error = LearningOutcomeService.get_learning_outcome_by_id(lo_id)
            if error:
                flash(error, 'error')
                return render_template('LearningOutcome/listLearningOutcome.html', learning_outcomes=learning_outcomes)

            # Redirigir a la vista de actualización si el resultado de aprendizaje es encontrado
            if learning_outcome:
                return render_template('LearningOutcome/updateLearningOutcome.html', learning_outcome=learning_outcome)

        # Renderizar la vista con todos los resultados de aprendizaje en caso de método GET o si no se busca ninguno
        return render_template('LearningOutcome/listLearningOutcome.html', learning_outcomes=learning_outcomes)

    except Exception as e:
        flash(f"Error al procesar la solicitud: {str(e)}", "error")
        return render_template('LearningOutcome/listLearningOutcome.html', learning_outcomes=[])



