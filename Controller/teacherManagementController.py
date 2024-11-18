from flask import Blueprint, render_template, request, redirect, url_for, flash
from Model.connection import Connection
from Model.teacher import Teacher
from Services.teacherService import TeacherService

#* CONTROLADOR GESTION DE PROFESORES
"""class TeacherManagementController:
    def __init__(self, app):
        # Inicializar la conexión a la base de datos usando la clase Connection
        self.app = app"""

teacher_blueprint = Blueprint('teacher_blueprint', __name__)
teacher_service = TeacherService()

# Ruta para listar los profesores
@teacher_blueprint.route('/docentes', methods=['GET'])
def listar_profesores():
    profesores = teacher_service.obtener_profesores()
    return render_template('profesores/listar.html', profesores=profesores)

# Ruta para mostrar el formulario de agregar profesor
@teacher_blueprint.route('/profesores/nuevo', methods=['GET', 'POST'])
def agregar_profesor():
    if request.method == 'POST':
        datos = request.form
        teacher_service.agregar_profesor(datos)
        flash('Profesor agregado exitosamente')
        return redirect(url_for('teacher_blueprint.listar_profesores'))
    return render_template('profesores/nuevo.html')

# Ruta para mostrar los detalles de un profesor
@teacher_blueprint.route('/profesores/<int:teId>', methods=['GET'])
def ver_profesor(teId):
    profesor = teacher_service.obtener_profesor(teId)
    if profesor:
        return render_template('profesores/detalle.html', profesor=profesor)
    else:
        flash('Profesor no encontrado')
        return redirect(url_for('teacher_blueprint.listar_profesores'))

# Ruta para editar un profesor
@teacher_blueprint.route('/profesores/editar/<int:teId>', methods=['GET', 'POST'])
def editar_profesor(teId):
    profesor = teacher_service.obtener_profesor(teId)
    if request.method == 'POST':
        datos = request.form
        teacher_service.actualizar_profesor(teId, datos)
        flash('Profesor actualizado exitosamente')
        return redirect(url_for('teacher_blueprint.listar_profesores'))
    return render_template('profesores/editar.html', profesor=profesor)

# Ruta para eliminar un profesor
@teacher_blueprint.route('/profesores/eliminar/<int:teId>', methods=['POST'])
def eliminar_profesor(teId):
    teacher_service.eliminar_profesor(teId)
    flash('Profesor eliminado exitosamente')
    return redirect(url_for('teacher_blueprint.listar_profesores'))