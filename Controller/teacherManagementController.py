from flask import Blueprint, render_template, request, redirect, url_for, flash
from Model.connection import Connection
from Model.teacher import Teacher
from Services.teacherService import TeacherService

#* CONTROLADOR GESTION DE PROFESORES
teacher_blueprint = Blueprint('teacher_blueprint', __name__)
teacher_service = TeacherService()

# Metodo crear teacher
@teacher_blueprint.route('/newTeacher', methods=['GET', 'POST'])
def create_teacher():
    if request.method == 'POST':
        datos = request.form
        teacher_service.create_teacher(datos)
        flash('Docente agregado exitosamente')
        return redirect(url_for('teacher_blueprint.listar_profesores'))
    return render_template('profesores/nuevo.html')

# Metoodo Editar teacher
@teacher_blueprint.route('/teacherUpdate/<int:teIdentificacion>', methods=['GET', 'POST'])
def update_teacher(teIdentificacion):
    profesor = teacher_service.obtener_profesor(teIdentificacion)
    if request.method == 'POST':
        datos = request.form
        teacher_service.actualizar_profesor(teIdentificacion, datos)
        flash('Docente actualizado exitosamente')
        return redirect(url_for('teacher_blueprint.listar_profesores'))
    return render_template('profesores/editar.html', profesor=profesor)

# Metodo Eliminar teacher
@teacher_blueprint.route('/profesores/eliminar/<int:teId>', methods=['POST'])
def delete_teacher(teIdentificacion):
    teacher_service.eliminar_profesor(teIdentificacion)
    flash('Docente eliminado exitosamente')
    return redirect(url_for('teacher_blueprint.listar_profesores'))

# Ruta para listar los profesores
@teacher_blueprint.route('/docentes', methods=['GET'])
def listar_profesores():
    profesores = teacher_service.obtener_profesores()
    return render_template('teachers/index.html', profesores=profesores)

# Ruta para mostrar los detalles de un profesor
@teacher_blueprint.route('/profesores/<int:teId>', methods=['GET'])
def ver_profesor(teId):
    profesor = teacher_service.obtener_profesor(teId)
    if profesor:
        return render_template('profesores/detalle.html', profesor=profesor)
    else:
        flash('Docente no encontrado')
        return redirect(url_for('teacher_blueprint.listar_profesores'))



