from flask import Blueprint, request, jsonify
from Services.learningOutcomeService import LearningOutcomeService

learning_outcome_controller = Blueprint('learning_outcome_controller', __name__)

@learning_outcome_controller.route('/learning-outcomes', methods=['POST'])
def create_learning_outcome():
    """Crea un nuevo resultado de aprendizaje (RA)."""
    try:
        data = request.json
        response = LearningOutcomeService.create_learning_outcome(
            comp_id=data.get("comp_id"),
            description=data.get("lo_description")
        )
        return jsonify(response), 201 if "message" in response else 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@learning_outcome_controller.route('/learning-outcomes/<int:lo_id>', methods=['PUT'])
def update_learning_outcome(lo_id):
    """Actualiza un resultado de aprendizaje (RA) existente."""
    try:
        data = request.json
        response = LearningOutcomeService.update_learning_outcome(
            lo_id=lo_id,
            comp_id=data.get("comp_id"),
            lo_description=data.get("lo_description")
        )
        return jsonify(response), 200 if "message" in response else 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@learning_outcome_controller.route('/learning-outcomes/competence/<int:comp_id>', methods=['GET'])
def get_learning_outcomes_by_competencia(comp_id):
    """Obtiene todos los RA asociados a una competencia específica."""
    response = LearningOutcomeService.get_learning_outcomes_by_competencia(comp_id)
    return jsonify(response), 200 if isinstance(response, list) else 400

