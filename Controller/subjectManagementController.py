#Controlador gestion de asignaturas
# Aqui va el metodo que va a recibir los argumentos de los formularios de las vistas

from flask import Blueprint, render_template, request, redirect, url_for, flash
from Services.subjectService import SubjectService
from Facade.subjectManagementFacade import SubjectManagementFacade


# Crear un blueprint para el controlador principal
subject_bp = Blueprint('subject',__name__)

#Ruta para crear una nueva materia, se pone los metodos get y post 
# para mostrar el formulario y añadir una asignatura respectivamente
@subject_bp.route('/add_subject', methods=['GET', 'POST'])
def create_subject():
    facade = SubjectManagementFacade()
    if request.method == 'POST':
        data = request.form.to_dict()
        #* Se puede poner: print(f"Formulario recibido: {data}") para verificar que se esten pasando los datos 
        # Llamar al servicio para crear la asignatura
        new_subject, error = facade.create_subject(data)

        if error:
            flash(error, 'error')
            #* Si hay un error, redirije a la misma pagina para volverlo a intentar
            #! Se usa el NOMBRE DEL CONTROLADOR, es decir el que se ledio en el primer parametro
            #! en el blueprint (subject en este caso) para llamar la funcion del contorlador.
            return redirect(url_for('subject.create_subject'))

        flash('Asignatura añadida satisfactoriamente!', 'success')
        #* Si se logro, se lo redirige a la misma pagia para añadir otra materia
        return redirect(url_for('subject.create_subject'))
    subjects,error = facade.get_all_subjects()
    if subjects is None:
        flash(f"Error: {error}", "danger")
        subjects = []  # Asegurarse de que 'competences' sea una lista vacía si ocurre un error
    #* Si el método NO ES POST, se muestra la vista del formulario.
    return render_template('Subject/createSubject.html', subjects=subjects)  # Vista para crear la asignatura


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

    return render_template('Subject/viewSubject.html', subject=subject)

@subject_bp.route('/search_subject', methods=['GET', 'POST'])
def search_subject():
    facade = SubjectManagementFacade()
    if request.method == 'POST':
        data=request.form.to_dict()

        try:
            selected_subject = data['subject_id']
            print("Id seleccionado:------------")
            print(selected_subject)

            if not selected_subject:
                flash("Por favor, complete todos los campos del formulario.", "danger")
                return redirect(url_for('subject.search_subject'))

            # Llamar al servicio para obtener la asignatura
            subject, error = facade.get_subject_by_id(selected_subject)

            print(subject)
            if error:
                flash(error, 'error')
                return redirect(url_for('subject.search_subject'))
            if subject:
                return render_template('Subject/updateSubject.html', subject=subject)
            
        except Exception as e:
            flash(f"Error al recuperar la asignatura: {e}", "danger")
    #Metodo para recuperar todas las asignaturas y cargarlas en el combobox
    cbxsubjects,error = facade.get_all_subjects()
    if cbxsubjects is None:
        flash(f"Error: {error}", "danger")
        cbxsubjects = []  # Asegurarse de que 'competences' sea una lista vacía si ocurre un error
    #* Si el método NO ES POST, se muestra la vista del formulario.
    return render_template('Subject/searchUpdateSubject.html', cbxsubjects=cbxsubjects)

@subject_bp.route('/update_subject/<int:id>', methods=['GET', 'POST'])
def update_subject(id):
    facade = SubjectManagementFacade()
    subject = None

    if request.method == 'POST':
        data = request.form.to_dict()

        try:
            # Llamar al servicio para actualizar la asignatura
            updated_subject, error = facade.update_subject(id, data)

            if error:
                flash(error, "danger")
                return redirect(url_for('subject.update_subject', id=id))

            flash("Asignatura actualizada con éxito!", 'success')
            #return redirect(url_for('subject.update_subject'))

        except Exception as e:
            flash(f"Error al actualizar la asignatura: {e}", "danger")
            return redirect(url_for('subject.update_subject', id=id))

    try:
        # Recuperar los datos de la asignatura actual para mostrarlos en el formulario
        subject, error = facade.get_subject_by_id(id)

        if error or not subject:
            flash("Error al recuperar los datos de la asignatura.", "danger")
            return redirect(url_for('subject.search_subject'))

    except Exception as e:
        flash(f"Error al cargar los datos de la asignatura: {e}", "danger")
        return redirect(url_for('subject.search_subject'))

    return render_template('Subject/updateSubject.html', subject=subject)











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