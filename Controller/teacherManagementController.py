from flask import Blueprint, render_template, request, redirect, url_for, flash
from Services.teacherService import TeacherService

#CONTROLADOR GESTION DE Docentes

#Blueprint para el controlador de docentes
teacher_blueprint = Blueprint('teacher', __name__)

#GET:Sirve para mostrar el formulario para crear un docente 
#POST:Sirve para crear un docente en la base de datos 

# Metodo crear docente
@teacher_blueprint.route('/create_teacher', methods=['GET', 'POST'])
def create_teacher():
    if request.method == 'POST':
        #Se obtienen los datos del formulario y se convierten a un diccionario
        data = request.form.to_dict()
        print(f"Datos recibidos: {data}")#verificar que se esten pasando los datos
        #Se llama al servicio para crear el docente
        new_teacher, error = TeacherService.create_teacher(data)

        #En caso de que ocurra un error  
        if error:
            #se muestra un mensaje
            flash(error, 'error')
            #se redirige a la misma pagina para poder intentar de nuevo
            return redirect(url_for('teacher.create_teacher'))
        
        #En caso contrario se muestra un mensaje y se redirige a la misma pagina
        flash('Docente agregado exitosamente')
        return redirect(url_for('teacher.create_teacher'))
    
    #Si el metodo no es POST se muestra la vista del formulario
    return render_template('Teacher/gestionTeacher.html')

#Metodo para mostrar todos los docentes
@teacher_blueprint.route('/search_allTeacher')
def search_allTeacher():
    #Se llama al servicio para obtener todos los docentes
    teachers = TeacherService.get_all_teacher()
    #Se muestra la vista de todos los docentes
    return render_template('Teacher/searchTeacher.html', teachers=teachers)

#Metodo para buscar un docente por su identificación
@teacher_blueprint.route('/search_by_identificationTeacher', methods=['GET', 'POST'])
def search_by_identificationTeacher():
    if request.method == 'POST':
        #Se obtiene la identificación del formulario
        teIdentification = request.form.get('teIdentification')
        #Se llama al servicio
        byIdentificationTeacher,error = TeacherService.search_by_identificationTeacher(teIdentification)
        #En caso de que ocurra un error
        if error:
            #Se muestra un mensaje
            flash(error, 'error')
            #Se redirige a la misma pagina para intentar de nuevo
            return redirect(url_for('teacher.searchTeacher'))
        #En caso contrario se muestra la vista con el docente encontrado
        return render_template('Teacher/searchTeacher.html', teacher=byIdentificationTeacher)
    return render_template('Teacher/searchTeacher.html')

#Metodo para buscar un docente por su apellido
@teacher_blueprint.route('/search_by_lastNameTeacher', methods=['GET', 'POST'])
def search_by_lastNameTeacher():
    if request.method == 'POST':
        #Se obtiene el apellido del formulario
        teLastName = request.form.get('teLastName')
        #print(f"Datos recibidos: {teLastName}")#verificar que se esten pasando los datos

        byLastNameTeacher,error = TeacherService.search_by_identificationTeacher(teLastName)
        if error:
            flash(error, 'error')
            return redirect(url_for('teacher.searchTeacher'))
        #En caso contrario se muestra la vista con el docente encontrado
        return render_template('Teacher/searchTeacher.html', teacher=byLastNameTeacher)
    return render_template('Teacher/searchTeacher.html')
        
    
#Metodo para buscar un docente por el tipo docente
@teacher_blueprint.route('/search_by_typeTeacher', methods=['GET', 'POST'])
def search_by_typeTeacher():
    if request.method == 'POST':
        #Se obtiene la identificación del formulario
        teTypeTeacher = request.form.get('teTypeTeacher')
        print(f"Datos recibidos: {teTypeTeacher}")#verificar que se esten pasando los datos
        #Se llama al servicio
        byTypeTeacher,error = TeacherService.search_by_typeTeacher(teTypeTeacher)
        #En caso de que ocurra un error
        if error:
            #Se muestra un mensaje
            flash(error, 'error')
            #Se redirige a la misma pagina para intentar de nuevo
            return redirect(url_for('teacher.searchTeacher'))
        #En caso contrario se muestra la vista con el docente encontrado
        return render_template('Teacher/searchTeacher.html', teachers=byTypeTeacher)
    return render_template('Teacher/searchTeacher.html')

#Metodo para editar un docente
@teacher_blueprint.route('/edit_teacher/<teIdentification>', methods=['GET', 'POST'])
def edit_teacher(teIdentification):
    if request.method == 'POST':
        # Obtener datos del formulario
        data = request.form.to_dict()
        print(f"Datos recibidos para editar: {data}")  # Para depuración

        # Llamar al servicio para actualizar el docente
        updated_teacher, error = TeacherService.edit_teacher(teIdentification, data)
        #update_teacher(teIdentification, data)

        # En caso de error, mostrar mensaje y redirigir
        if error:
            flash(error, 'error')
            return redirect(url_for('teacher.edit_teacher'))
        return redirect(url_for('teacher.edit_teacher', teIdentification=edit_teacher.teIdentification))