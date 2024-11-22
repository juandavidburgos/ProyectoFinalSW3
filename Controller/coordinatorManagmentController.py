from flask import Blueprint, render_template, request, redirect, url_for, flash
from Services.coordinatorService import CoordinatorService

# CONTROLADOR GESTION DE COORDINADORES

# Blueprint para las rutas del coordinador
coordinator_blueprint = Blueprint('coordinator', __name__)

# Método para listar todos los coordinadores
@coordinator_blueprint.route('/coordinators', methods=['GET'])
def get_all_coordinators():
    coordinators = CoordinatorService.get_all_coordinators()
    return render_template('coordinator/searchCoordinator.html', coordinators=coordinators)

# Método para obtener un coordinador por ID
@coordinator_blueprint.route('/coordinators/<int:coordinator_id>', methods=['GET'])
def get_coordinator_by_id(coordinator_id):
    coordinator = CoordinatorService.get_coordinator_by_id(coordinator_id)
    if not coordinator:
        flash("Coordinador no encontrado", 'error')
        return redirect(url_for('coordinator.get_all_coordinators'))
    return render_template('coordinator/detailCoordinator.html', coordinator=coordinator)

# Método para crear un nuevo coordinador
@coordinator_blueprint.route('/create_coordinator', methods=['GET', 'POST'])
def create_coordinator():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(f"Datos recibidos: {data}")  # Verificar datos en consola
        new_coordinator, error = CoordinatorService.create_coordinator(data)

        if error:
            flash(error, 'error')
            return redirect(url_for('coordinator.create_coordinator'))
        
        flash("Coordinador creado exitosamente", 'success')
        return redirect(url_for('coordinator.get_all_coordinators'))

    return render_template('coordinator/createCoordinator.html')

# Método para actualizar un coordinador existente
@coordinator_blueprint.route('/edit_coordinator/<int:coordinator_id>', methods=['GET', 'POST'])
def update_coordinator(coordinator_id):
    coordinator = CoordinatorService.get_coordinator_by_id(coordinator_id)
    if not coordinator:
        flash("Coordinador no encontrado", 'error')
        return redirect(url_for('coordinator.get_all_coordinators'))

    if request.method == 'POST':
        data = request.form.to_dict()
        updated_coordinator, error = CoordinatorService.update_coordinator(coordinator_id, data)

        if error:
            flash(error, 'error')
            return redirect(url_for('coordinator.update_coordinator', coordinator_id=coordinator_id))

        flash("Coordinador actualizado exitosamente", 'success')
        return redirect(url_for('coordinator.get_all_coordinators'))

    return render_template('coordinator/editCoordinator.html', coordinator=coordinator)

# Método para eliminar un coordinador
@coordinator_blueprint.route('/delete_coordinator/<int:coordinator_id>', methods=['POST'])
def delete_coordinator(coordinator_id):
    try:
        CoordinatorService.delete_coordinator(coordinator_id)
        flash("Coordinador eliminado exitosamente", 'success')
    except ValueError as e:
        flash(f"Error al eliminar el coordinador: {str(e)}", 'error')

    return redirect(url_for('coordinator.get_all_coordinators'))

"""
# Método para crear un docente por parte de un coordinador
@coordinator_blueprint.route('/create_teacher_by_coordinator', methods=['GET', 'POST'])
def create_teacher_by_coordinator():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(f"Datos recibidos: {data}")  # Verificar datos en consola
        new_teacher, error = CoordinatorService.create_teacher(data)

        if error:
            flash(error, 'error')
            return redirect(url_for('coordinator.create_teacher_by_coordinator'))

        flash("Docente creado exitosamente", 'success')
        return redirect(url_for('coordinator.get_all_coordinators'))

    return render_template('coordinator/createTeacherByCoordinator.html')

# Método para gestionar asignaturas (crear y vincular competencias y RA)
@coordinator_blueprint.route('/create_subject', methods=['GET', 'POST'])
def manage_subjects():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(f"Datos recibidos: {data}")  # Verificar datos en consola
        new_subject, error = CoordinatorService.create_subject(data)

        if error:
            flash(error, 'error')
            return redirect(url_for('coordinator.manage_subjects'))

        flash("Asignatura creada exitosamente", 'success')
        return redirect(url_for('coordinator.get_all_coordinators'))

    return render_template('coordinator/manageSubjects.html')

# Método para gestionar competencias y RA
@coordinator_blueprint.route('/create_competency', methods=['GET', 'POST'])
def manage_competencies():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(f"Datos recibidos: {data}")  # Verificar datos en consola
        new_competency, error = CoordinatorService.create_competency(data)

        if error:
            flash(error, 'error')
            return redirect(url_for('coordinator.manage_competencies'))

        flash("Competencia creada exitosamente", 'success')
        return redirect(url_for('coordinator.get_all_coordinators'))

    return render_template('coordinator/manageCompetencies.html')
"""