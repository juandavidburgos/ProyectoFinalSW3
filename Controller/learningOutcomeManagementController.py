from flask import Blueprint, render_template, request, redirect, url_for, flash
from Services.learningOutcomeService import LearningOutcomeService
from Facade.learningOutcomeManagementFacade import LoutFacade
# Crear un blueprint para el controlador de resultados de aprendizaje
learning_outcome_bp = Blueprint('learning_outcome', __name__)

@learning_outcome_bp.route('/create_learning_outcome', methods=['GET', 'POST'])
def create_learning_outcome():
    """Ruta para crear un nuevo Resultado de Aprendizaje"""
    facade= LoutFacade()
    if request.method == 'POST':
        data = request.form.to_dict()
        # Llamar al servicio para crear el resultado de aprendizaje
        new_learning_outcome, error = facade.create_lo(data)

        if error:
            flash(error, 'error')
            return redirect(url_for('learning_outcome.create_learning_outcome'))

        flash('¡Resultado de Aprendizaje añadido satisfactoriamente!', 'success')
        return redirect(url_for('learning_outcome.create_learning_outcome'))

    return render_template('LearningOutcome/createLearningOutcome.html')

@learning_outcome_bp.route('/list_learning_outcome', methods=['GET', 'POST'])
def list_and_search_learning_outcomes():
    """Ruta para listar y buscar resultados de aprendizaje"""
    facade= LoutFacade()
    try:
        # Obtener todos los resultados de aprendizaje para mostrarlos en la tabla
        learning_outcomes, error = facade.get_all_louts()
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
            learning_outcome, error = facade.get_learning_outcome_by_id(lo_id)
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

#No funciona -> <int:lo_id> estara bien o cual sera la manera correcta
@learning_outcome_bp.route('/update_learning_outcome', methods=['GET', 'POST'])
def update_learning_outcome():
    learning_outcome = None
    facade = LoutFacade()
    if request.method == 'POST':
        data = request.form.to_dict()
        lout_id = data.get('lout_id')  # Obtener el nombre del formulario

        # Llamamos al servicio para actualizar el RA
        learning_outcome, error = facade.update_learning_outcome(lout_id, data)
        if error:
            flash(f"Error al actualizar: {str(error)}")
            return redirect(url_for('learning_outcome.update_learning_outcome', learning_outcome=data))
        if learning_outcome:
            flash("RA actualizado con éxito!", 'success')
            #return redirect(url_for('learning_outcome.list_and_search_learning_outcomes', lout_id=lout_id))  # Redirigimos usando el nombre actualizado
    # Si el método NO ES POST, se muestra la vista del formulario.
    return render_template('LearningOutcome/updateLearningOutcome.html', learning_outcome=learning_outcome)


