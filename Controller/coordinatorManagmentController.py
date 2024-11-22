from flask import Blueprint, jsonify, request
from app.services.coordinator_service import CoordinatorService

# Blueprint para las rutas del coordinador
coordinator_blueprint = Blueprint('coordinator', __name__)
service = CoordinatorService()

# Listar todos los coordinadores
@coordinator_blueprint.route('/coordinators', methods=['GET'])
def get_all_coordinators():
    coordinators = service.get_all()
    return jsonify([coordinator.to_dict() for coordinator in coordinators]), 200

# Obtener un coordinador por ID
@coordinator_blueprint.route('/coordinators/<int:coordinator_id>', methods=['GET'])
def get_coordinator_by_id(coordinator_id):
    coordinator = service.get_by_id(coordinator_id)
    if not coordinator:
        return jsonify({"error": "Coordinator not found"}), 404
    return jsonify(coordinator.to_dict()), 200

# Crear un nuevo coordinador
@coordinator_blueprint.route('/coordinators', methods=['POST'])
def create_coordinator():
    data = request.get_json()
    try:
        new_coordinator = service.create(data)
        return jsonify(new_coordinator.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# Actualizar un coordinador existente
@coordinator_blueprint.route('/coordinators/<int:coordinator_id>', methods=['PUT'])
def update_coordinator(coordinator_id):
    data = request.get_json()
    try:
        updated_coordinator = service.update(coordinator_id, data)
        return jsonify(updated_coordinator.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# Eliminar un coordinador
@coordinator_blueprint.route('/coordinators/<int:coordinator_id>', methods=['DELETE'])
def delete_coordinator(coordinator_id):
    try:
        service.delete(coordinator_id)
        return jsonify({"message": "Coordinator deleted successfully"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

"""
# Crear un docente (gestión de docentes por el coordinador)
@coordinator_blueprint.route('/coordinators/<int:coordinator_id>/teachers', methods=['POST'])
def create_teacher_by_coordinator(coordinator_id):
    data = request.get_json()
    try:
        new_teacher = service.create_teacher(coordinator_id, data)
        return jsonify(new_teacher.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# Gestionar asignaturas (crear, vincular competencias y RA)
@coordinator_blueprint.route('/coordinators/<int:coordinator_id>/subjects', methods=['POST'])
def manage_subjects(coordinator_id):
    data = request.get_json()
    try:
        new_subject = service.create_subject(coordinator_id, data)
        return jsonify(new_subject.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# Vincular competencias y RA a un programa
@coordinator_blueprint.route('/coordinators/<int:coordinator_id>/competencies', methods=['POST'])
def manage_competencies(coordinator_id):
    data = request.get_json()
    try:
        new_competency = service.create_competency(coordinator_id, data)
        return jsonify(new_competency.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
"""