from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_jwt_extended import jwt_required, get_jwt_identity,decode_token  # Importar JWT, decorador
from flask import current_app
from Services.teacherService import TeacherService
from Facade.teacherManagementFacade import TeacherManagementFacade

#CONTROLADOR GESTION DE Docentes

#Blueprint para el controlador de docentes
teacher_blueprint = Blueprint('teacher', __name__)

#GET:Sirve para mostrar el formulario para crear un docente 
#POST:Sirve para crear un docente en la base de datos 

# Metodo crear docente
# Ruta protegida para crear docente
@teacher_blueprint.route('/create_teacher', methods=['GET', 'POST'])
#@jwt_required()  # Proteger la ruta con JWT
def create_teacher():
    # Obtener la identidad del usuario desde el token JWT
    #current_user = get_jwt_identity()
    #print(f"Usuario autenticado: {current_user}")
    facade = TeacherManagementFacade()
    if request.method == 'POST':
        # Se obtienen los datos del formulario y se convierten a un diccionario
        data = request.form.to_dict()
        print(f"Datos recibidos: {data}")  # Verificar que se estén pasando los datos
        # Se llama al servicio para crear el docente
        new_teacher, error = TeacherManagementFacade.create_teacher(data)

        # En caso de que ocurra un error  
        if error:
            # Se muestra un mensaje
            flash(error, 'error')
            # Se redirige a la misma página para poder intentar de nuevo
            return redirect(url_for('teacher.create_teacher'))

        # En caso contrario se muestra un mensaje y se redirige a la misma página
        flash('Docente agregado exitosamente')
        return redirect(url_for('Teacher/teacher.create_teacher'))
    teachers,error = facade.get_all_teachers()
    if teachers is None:
        flash(f"Error: {error}", "danger")
        teachers = []  # Asegurarse de que 'competences' sea una lista vacía si ocurre un error
    #* Si el método NO ES POST, se muestra la vista del formulario.
    #Si el metodo no es POST se muestra la vista del formulario
    return render_template('Teacher/createTeacher.html',teachers=teachers)

#Metodo para mostrar todos los docentes
@teacher_blueprint.route('/search_allTeacher')
def search_allTeacher():
    #Se llama al servicio para obtener todos los docentes
    teachers = TeacherService.search_allTeacher()
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
@teacher_blueprint.route('/edit_teacher/<string:teIdentification>', methods=['GET', 'POST'])
def edit_teacher(teIdentification):
    if request.method == 'POST':
        teIdentification = request.form.get('teIdentification')
        edit_teacher, error = TeacherService.edit_teacher(teIdentification)
        if error:
            flash(error, 'error')
            return redirect(url_for('teacher.edit_teacher'))
        return redirect(url_for('teacher.edit_teacher', teIdentification=edit_teacher.teIdentification))
    
@teacher_blueprint.route('/manage_rubrics', methods=['GET','POST'])
def manage_rubrics():
    return render_template('Teacher/rubrics.html')

@teacher_blueprint.route('/edit_teacher_1>', methods=['GET', 'POST'])
def edit_teacher_1():
    return render_template('Teacher/searchTeacher.html')