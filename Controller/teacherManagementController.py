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
    return render_template('createTeacher.html')



