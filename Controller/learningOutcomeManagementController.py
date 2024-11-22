from flask import Blueprint, render_template, request, redirect, url_for, flash
from Services.learningOutcomeService import LearningOutcomeService

# Crear un blueprint para el controlador de resultados de aprendizaje
learning_outcome_bp = Blueprint('learning_outcome', __name__)

@learning_outcome_bp.route('/create_learning_outcome', methods=['GET', 'POST'])
def create_learning_outcome():
    """Ruta para crear un nuevo Resultado de Aprendizaje"""
    if request.method == 'POST':
        data = request.form.to_dict()
        # Llamar al servicio para crear el resultado de aprendizaje
        new_learning_outcome, error = LearningOutcomeService.create_learning_outcome(data)

        if error:
            flash(error, 'error')
            return redirect(url_for('learning_outcome.create_learning_outcome'))

        flash('¡Resultado de Aprendizaje añadido satisfactoriamente!', 'success')
        return redirect(url_for('learning_outcome.create_learning_outcome'))

    return render_template('LearningOutcome/createLearningOutcome.html')

@learning_outcome_bp.route('/list_learning_outcome', methods=['GET'])
def list_learning_outcomes():
    """Ruta para listar todos los Resultados de Aprendizaje"""
    # Llamar al servicio para obtener todos los resultados de aprendizaje
    learning_outcomes, error = LearningOutcomeService.get_all_learning_outcomes()

    if error:
        flash(error, 'error')
        learning_outcomes = []  # Si hay un error, enviar una lista vacía

    # Renderizar la plantilla con los resultados
    return render_template('LearningOutcome/createLearningOutcome.html', learning_outcomes=learning_outcomes)

#No funciona -> <int:lo_id> estara bien o cual sera la manera correcta
@learning_outcome_bp.route('/update_learning_outcome', methods=['GET', 'POST'])
def update_learning_outcome():
    learning_outcome = None
    if request.method == 'POST':
        data = request.form.to_dict()
        lo_id = data.get('lo_id')  # Obtener el nombre del formulario

        # Llamamos al servicio para actualizar el RA
        learning_outcome, error = LearningOutcomeService.update_learning_outcome(lo_id, data)
        if error:
            flash(error, "error")
            return redirect(url_for('learning_outcome.update_learning_outcome', lo_id=lo_id))
        if learning_outcome:
            flash("RA actualizado con éxito!", 'success')
            return redirect(url_for('learning_outcome.update_learning_outcome', lo_id=lo_id))  # Redirigimos usando el nombre actualizado

    # Si el método NO ES POST, se muestra la vista del formulario.
    return render_template('LearningOutcome/updateLearningOutcome.html', learning_outcome=learning_outcome)


def update_learning_outcome_bad(lo_id):
    """Ruta para actualizar un Resultado de Aprendizaje existente"""
    if request.method == 'POST':
        data = request.form.to_dict()
        # Llamar al servicio para actualizar el resultado de aprendizaje
        updated_learning_outcome, error = LearningOutcomeService.update_learning_outcome(
            lo_id=lo_id,
            lo_description=data.get('lo_description')
        )

        if error:
            flash(error, 'error')
            return redirect(url_for('learning_outcome.update_learning_outcome', lo_id=lo_id))

        flash('¡Resultado de Aprendizaje actualizado satisfactoriamente!', 'success')
        return redirect(url_for('learning_outcome.update_learning_outcome', lo_id=lo_id))

    # Si el método es GET, obtener el resultado de aprendizaje existente para prellenar el formulario
    learning_outcome = LearningOutcomeService.get_learning_outcomes_by_competencia(lo_id)
    if not learning_outcome:
        flash('El Resultado de Aprendizaje no existe.', 'error')
        return redirect(url_for('learning_outcome.create_learning_outcome'))

    return render_template('LearningOutcome/updateLearningOutcome.html', learning_outcome=learning_outcome, lo_id=lo_id)


