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


@subject_bp.route('/get_subject', methods=['GET', 'POST'])
def get_subject():
    subject = None  # Inicializa subject como None
    if request.method == 'POST':
        name = request.form.get('name')  # Obtener el nombre del formulario
        if not name:
            flash("Por favor, ingrese el nombre de la asignatura.", "error")
            return redirect(url_for('subject.get_subject'))

        subject, error = SubjectService.get_subject_by_name(name)
        if error:
            flash(error, "error")
            return redirect(url_for('subject.get_subject'))

    return render_template('viewSubject.html', subject=subject)

@subject_bp.route('/search_subject', methods=['GET', 'POST'])
def search_subject():
    subject = None
    name = request.args.get('name', '')

    # Si el método es GET, se renderiza la vista de búsqueda de asignatura
    if request.method == 'GET':
        return render_template('searchUpdateSubject.html', subject=subject)

    # Si el método es POST, se intenta buscar la asignatura por nombre
    if request.method == 'POST':
        name = request.form.get('name')  # Capturar el nombre enviado
        if not name:
            flash("Por favor, ingrese el nombre de la asignatura.", "error")
            return redirect(url_for('subject.search_subject', name=''))

        subject, error = SubjectService.get_subject_by_name(name)
        if error:
            flash(error, "error")
            return redirect(url_for('subject.search_subject', name=''))

        if subject:
            return render_template('updateSubject.html', subject=subject)
        else:
            # Si no se encuentra la asignatura, se muestra un mensaje y se regresa a la búsqueda
            flash("La asignatura no existe", "error")
            return render_template('searchUpdateSubject.html', subject=subject)

@subject_bp.route('/update_subject', methods=['GET', 'POST'])
def update_subject():
    subject = None
    if request.method == 'POST':
        data = request.form.to_dict()
        name = data.get('name')  # Obtener el nombre del formulario

        #!¡IMPORTANTE!
        #* A la hora de quereer actualizar la asignatura, no se le puede actualizar el nombre porque sino va a generar
        #* un ciclo donde vuelve a llamarse otro metodo y demas. Entonces:
        # ? Como solucionar ese ciclo?
        # ? Mejor hacer la busqueda por id?

        # Llamamos al servicio para actualizar la asignatura
        subject, error = SubjectService.update_subject(name, data)
        if error:
            flash(error, "error")
            return redirect(url_for('subject.update_subject', name=name))  # Pasamos el nombre para seguir con el flujo
        if subject:
            flash("Asignatura actualizada con éxito!", 'success')
            return redirect(url_for('subject.search_subject', name=subject.name))  # Redirigimos usando el nombre actualizado

    # Si el método NO ES POST, se muestra la vista del formulario.
    return render_template('updateSubject.html', subject=subject)










#@subject_bp.route('/get/<name>', methods=['GET','POST'])
#def get_subject(name):
 #   subject = None
  #  subject,error = SubjectService.get_subject_by_name(name)
   # if request.method=='POST':
    #    name = request.form.to_dict()
     #   if not name:
      #      flash("Por favor ingrese un nombre para la asignatura", "Error")
       #     return redirect(url_for('subject.get_subject'))
        
       # subject,error = SubjectService.get_subject_by_name(name)

       # if error:
       #     flash(error, "Error inesperado")
      #      return redirect(url_for('subject.get_subject'))
        
   # return render_template('viewSubject.html', subject=subject)

#@subject_bp.route('/update/<name>', methods=['GET','POST'])
#def update_subject(name):
#    subject=None
#    subject,error=SubjectService.get_subject_by_name(name)
#    if error:
#        flash(error, "Error inesperado")
#        return redirect(url_for('subject.update_subject'))

#    if request.method == 'POST':
#        data = request.form
#        updated_subject, update_error = SubjectService.update_subject_by_name(name, data)
#        if update_error:
#            flash(update_error, "error")
#            return redirect(url_for('subject.update_subject', name=name))

#        flash("Asignatura actualizada satisfactoriamente!", "success")
#        return redirect(url_for('subject.update_subject'))

#    return render_template('updateSubject.html', subject = subject)