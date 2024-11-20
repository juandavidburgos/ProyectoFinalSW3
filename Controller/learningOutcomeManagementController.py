from flask import Blueprint, render_template, request, redirect, url_for, flash
from Services.learningOutcomeService import LearningOutcomeService

# Crear un blueprint para el controlador de resultados de aprendizaje
learning_outcome_bp = Blueprint('learning_outcome', __name__)

@learning_outcome_bp.route('/add_learning_outcome', methods=['GET', 'POST'])
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

    return render_template('createLearningOutcome.html')

#No funciona -> <int:lo_id> estara bien o cual sera la manera correcta
@learning_outcome_bp.route('/update_learning_outcome/<int:lo_id>', methods=['GET', 'POST'])
def update_learning_outcome(lo_id):
    """Ruta para actualizar un Resultado de Aprendizaje existente"""
    if request.method == 'POST':
        data = request.form.to_dict()
        # Llamar al servicio para actualizar el resultado de aprendizaje
        updated_learning_outcome, error = LearningOutcomeService.update_learning_outcome(
            lo_id=lo_id,
            comp_id=data.get('comp_id'),
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

    return render_template('updateLearningOutcome.html', learning_outcome=learning_outcome, lo_id=lo_id)


