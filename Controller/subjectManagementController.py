#Controlador gestion de asignaturas
# Aqui va el metodo que va a recibir los argumentos de los formularios de las vistas

from flask import Blueprint, render_template, request, redirect, url_for, flash
from Services.subjectService import SubjectService


# Crear un blueprint para el controlador principal
subject_bp = Blueprint('subject',__name__)

#Ruta para crear una nueva materia, se pone los metodos get y post 
# para mostrar el formulario y añadir una asignatura respectivamente
@subject_bp.route('/add_subject', methods=['GET', 'POST'])
def create_subject():
    if request.method == 'POST':
        data = request.form.to_dict()
        #* Se puede poner: print(f"Formulario recibido: {data}") para verificar que se esten pasando los datos 
        # Llamar al servicio para crear la asignatura
        new_subject, error = SubjectService.create_subject(data)

        if error:
            flash(error, 'error')
            #* Si hay un error, redirije a la misma pagina para volverlo a intentar
            #! Se usa el NOMBRE DEL CONTROLADOR, es decir el que se ledio en el primer parametro
            #! en el blueprint (subject en este caso) para llamar la funcion del contorlador.
            return redirect(url_for('subject.create_subject'))

        flash('Asignatura añadida satisfactoriamente!', 'success')
        #* Si se logro, se lo redirige a la misma pagia para añadir otra materia
        return redirect(url_for('subject.create_subject'))
    #* Si el método NO ES POST, se muestra la vista del formulario.
    return render_template('createSubject.html')  # Vista para crear la asignatura
