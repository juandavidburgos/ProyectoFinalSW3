#holaaaaaaaaaa
from flask import Blueprint, render_template, request, redirect, url_for, flash
from Services.competenceService import CompetenceService

competence_bp = Blueprint('competence', __name__)

# Ruta para crear una nueva competencia, con métodos GET y POST
@competence_bp.route('/add_competence', methods=['GET', 'POST'])
def create_competence():
    if request.method == 'POST':
        # Obtener los datos del formulario y convertirlos a un diccionario
        data = request.form.to_dict()
        # Llamar al servicio para crear la competencia
        new_competence, error = CompetenceService.create_competence(data)

        if error:
            # Si hay un error, mostrar el mensaje y redirigir al mismo formulario
            flash(error, 'error')
            return redirect(url_for('competence.create_competence'))

        # Si se logró crear la competencia, mostrar un mensaje de éxito
        flash('Competencia añadida satisfactoriamente!', 'success')
        # Redirigir al formulario para agregar otra competencia
        return redirect(url_for('competence.create_competence'))

    # Si el método no es POST, se muestra el formulario de creación de la competencia
    return render_template('Competence/createCompetence.html')  # Vista para crear la competencia

@competence_bp.route('/list_competence', methods=['GET'])
def list_competences():
    """Ruta para listar todas las competencias"""
    # Llamar al servicio para obtener todos los resultados de aprendizaje
    competences, error = CompetenceService.get_all_competences()

    if error:
        flash(error, 'error')
        competences = []  # Si hay un error, enviar una lista vacía

    # Renderizar la plantilla con los resultados
    return render_template('Competence/createCompetence.html', competences=competences)

@competence_bp.route('/update_competence', methods=['GET', 'POST'])
def update_competence():
    competence = None
    if request.method == 'POST':
        data = request.form.to_dict()
        comp_id = data.get('comp_id')  # Obtener del formulario

        # Llamamos al servicio para actualizar la competencia
        competence, error = CompetenceService.update_competence(comp_id, data)
        if error:
            flash(error, "error")
            return redirect(url_for('competence.update_competence', comp_id=comp_id))  # Pasamos el nombre para seguir con el flujo
        if competence:
            flash("Competencia actualizada con éxito!", 'success')
            return redirect(url_for('competence.get_all_competences', comp_id=competence.comp_id))  # Redirigimos usando el nombre actualizado

    # Si el método NO ES POST, se muestra la vista del formulario.
    return render_template('Competence/updateCompetence.html', competence=competence)

'''
@competence_controller.route('/competences/<int:comp_id>', methods=['PUT'])
def update_competence(comp_id):
    """Actualiza una competencia existente."""
    try:
        data = request.json
        response = CompetenceService.update_competence(
            comp_id=comp_id,
            comp_description=data.get("comp_description"),
            comp_type=data.get("comp_type"),
            comp_level=data.get("comp_level"),
            program_comp_id=data.get("program_comp_id", None)
        )
        return jsonify(response), 200 if "message" in response else 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@competence_controller.route('/competences/comp_type/<string:comp_type>', methods=['GET'])
def get_competences_by_type(comp_type):
    """Obtiene todas las competencias por tipo."""
    response = CompetenceService.get_competences_by_type(comp_type)
    return jsonify(response), 200 if isinstance(response, list) else 400

@competence_controller.route('/competences/linked/<int:program_comp_id>', methods=['GET'])
def get_linked_competences(program_comp_id):
    """Obtiene competencias vinculadas a una competencia padre."""
    response = CompetenceService.get_linked_competences(program_comp_id)
    return jsonify(response), 200 if isinstance(response, list) else 400
'''