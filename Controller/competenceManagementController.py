#holaaaaaaaaaa
from flask import Blueprint, request, jsonify
from Services.competenceService import CompetenceService

competence_controller = Blueprint('competence_controller', __name__)

@competence_controller.route('/competences', methods=['POST'])
def create_competence():
    """Crea una nueva competencia."""
    try:
        data = request.json
        response = CompetenceService.create_competence(
            comp_description=data.get("comp_description"),
            comp_type_=data.get("comp_type"),
            comp_level=data.get("comp_level"),
            program_comp_id=data.get("program_comp_id", None)
        )
        return jsonify(response), 201 if "message" in response else 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@competence_controller.route('/competences/<int:comp_id>', methods=['PUT'])
def update_competence(comp_id):
    """Actualiza una competencia existente."""
    try:
        data = request.json
        response = CompetenceService.update_competence(
            comp_id=comp_id,
            comp_description=data.get("description"),
            comp_type=data.get("type"),
            comp_level=data.get("level"),
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
