#holaaaaaaaaaa
from flask import Blueprint, render_template, request, redirect, url_for, flash
from Facade.CmpLoutFacade import CmpLoutFacade

competence_bp = Blueprint('competence', __name__)

@competence_bp.route('/add_program_competence', methods=['GET', 'POST'])
def create_program_competence():
    facade = CmpLoutFacade()

    if request.method == 'POST':
        data = request.form.to_dict()
        print(f"Formulario recibido: {data}")
        try:
            competence_data = {
                'comp_description': data['comp_description'],
                'comp_type': data['comp_type'],
                'comp_level': data['comp_level'],
                'comp_subject_id': data.get('comp_subject_id',None)  # Asignatura opcional
            }

            rap_data = {
                'lout_description': data['lout_description']
                #'lout_subject_id': data.get('lout_subject_id',None)  # Asignatura opcional para el RAP
            }

            
            facade.create_competence_with_rap(competence_data, rap_data)
            flash("Competencia de programa y RAP creados exitosamente.", "success")
            return redirect(url_for('competence.create_program_competence'))
        except KeyError as e:
            flash(f"Error: Falta el campo {str(e)} en el formulario.", "danger")
        except Exception as e:
            flash(f"Error al crear competencia y RAP: {e}", "danger")

    competences, error = facade.get_all_competences()
    if competences is None:
        flash(f"Error: {error}", "danger")
        competences = []  # Asegurarse de que 'competences' sea una lista vacía si ocurre un error

    return render_template('Competence/createCompetence.html', competences=competences)

@competence_bp.route('/search_competence', methods=['GET', 'POST'])
def search_competence():
    facade = CmpLoutFacade()
    if request.method == 'POST':
        data=request.form.to_dict()

        try:
            selected_competence = data['comp_id']
            print("Id seleccionado:------------")
            print(selected_competence)

            if not selected_competence:
                flash("Por favor, complete todos los campos del formulario.", "danger")
                return redirect(url_for('competence.search_competence'))

            # Llamar al servicio para obtener la asignatura
            competence, error = facade.get_competence_by_id(selected_competence)

            print(competence)
            if error:
                flash(error, 'error')
                return redirect(url_for('competence.search_competence'))
            if competence:
                return render_template('Competence/updateCompetence.html', competence=competence)
            
        except Exception as e:
            flash(f"Error al recuperar la competencia: {e}", "danger")
    #Metodo para recuperar todas las asignaturas y cargarlas en el combobox
    cbxcompetences,error = facade.get_all_competences()
    if cbxcompetences is None:
        flash(f"Error: {error}", "danger")
        cbxcompetences = []  # Asegurarse de que 'competences' sea una lista vacía si ocurre un error
    #* Si el método NO ES POST, se muestra la vista del formulario.
    return render_template('Competence/searchUpdateCompetence.html', cbxcompetences=cbxcompetences)

@competence_bp.route('/update_competence/<int:comp_id>', methods=['GET', 'POST'])
def update_competence(comp_id):
    facade = CmpLoutFacade()
    competence = None

    if request.method == 'POST':
        data = request.form.to_dict()
        print("LLEGAMOS ACAA")
        try:
            print("LLEGAMOS ACAA")
            # Llamar al servicio para actualizar la asignatura
            updated_competence, error = facade.update_competence(comp_id,data)

            if error:
                flash(error, "danger")
                return redirect(url_for('competence.update_competence', comp_id=comp_id))

            flash("Asignatura actualizada con éxito!", 'success')
            #return redirect(url_for('subject.update_subject'))

        except Exception as e:
            flash(f"Error al actualizar la competencia: {e}", "danger")
            return redirect(url_for('competence.update_competence', comp_id=comp_id))

    try:
        # Recuperar los datos de la asignatura actual para mostrarlos en el formulario
        competence, error = facade.get_competence_by_id(comp_id)

        if error or not competence:
            flash("Error al recuperar los datos de la competencia.", "danger")
            return redirect(url_for('competence.search_competence'))

    except Exception as e:
        flash(f"Error al cargar los datos de la asignatura: {e}", "danger")
        return redirect(url_for('competence.search_competence'))

    return render_template('Competence/updateCompetence.html', competence=competence)

@competence_bp.route('/view_competences', methods=['GET'])
def view_competences():
    facade = CmpLoutFacade()
    try:
        # Obtener todas las competencias
        competences, error = facade.get_all_competences()

        if error:
            flash("Error al obtener las competencias: " + error, "danger")
    except Exception as e:
        flash(f"Error al buscar competencias: {e}", "danger")
        competences = []

    # Renderizar la plantilla con todas las competencias
    return render_template('Competence/listCompetence.html', competences=competences)







"""""
# Ruta para crear una nueva competencia, con métodos GET y POST
@competence_bp.route('/add_competence', methods=['GET', 'POST'])
def create_competence():
    if request.method == 'POST':
        # Obtener los datos del formulario y convertirlos a un diccionario
        data = request.form.to_dict()
        # Llamar al servicio para crear la competencia
        new_competence, error = CompetenceService.create_competence(data)

        if error:
            # Si hay un error, mostrar el mensaje y redirigir al mismo formulario
            flash(error, 'error')
            return redirect(url_for('competence.create_competence'))

        # Si se logró crear la competencia, mostrar un mensaje de éxito
        flash('Competencia añadida satisfactoriamente!', 'success')
        # Redirigir al formulario para agregar otra competencia
        return redirect(url_for('competence.create_competence'))

    # Si el método no es POST, se muestra el formulario de creación de la competencia
    return render_template('Competence/createCompetence.html')  # Vista para crear la competencia

@competence_bp.route('/list_competence', methods=['GET', 'POST'])
def list_and_search_competences():
    #Ruta para listar y buscar competencias
    try:
        # Obtener todas las competencias para mostrarlas en la tabla
        competences, error = CompetenceService.get_all_competences()
        if error:
            flash(error, 'error')
            competences = []

        # Si el método es POST, se intenta buscar una competencia por ID
        if request.method == 'POST':
            comp_id = request.form.get('id')  # Capturar el ID enviado desde el formulario
            if not comp_id:
                flash("Por favor, ingrese el ID de la competencia.", "error")
                return render_template('Competence/listCompetence.html', competences=competences)

            # Buscar competencia por ID
            competence, error = CompetenceService.get_competence_by_id(comp_id)
            if error:
                flash(error, 'error')
                return render_template('Competence/listCompetence.html', competences=competences)

            # Redirigir a la vista de actualización si la competencia es encontrada
            if competence:
                return render_template('Competence/updateCompetence.html', competence=competence)

        # Renderizar la vista con todas las competencias en caso de método GET o si no se busca ninguna competencia
        return render_template('Competence/listCompetence.html', competences=competences)

    except Exception as e:
        flash(f"Error al procesar la solicitud: {str(e)}", "error")
        return render_template('Competence/listCompetence.html', competences=[])

@competence_bp.route('/update_competence', methods=['GET', 'POST'])
def update_competence():
    competence = None
    if request.method == 'POST':
        data = request.form.to_dict()
        comp_id = data.get('comp_id')  # Obtener del formulario

        # Llamamos al servicio para actualizar la competencia
        competence, error = CompetenceService.update_competence(comp_id, data)
        if error:
            flash(error, "error")
            return redirect(url_for('competence.list_and_search_competences', comp_id=comp_id))  # Pasamos el nombre para seguir con el flujo
        if competence:
            flash("Competencia actualizada con éxito!", 'success')
            return redirect(url_for('competence.list_and_search_competences', comp_id=competence.comp_id))  # Redirigimos usando el nombre actualizado

    # Si el método NO ES POST, se muestra la vista del formulario.
    return render_template('Competence/updateCompetence.html', competence=competence)

'''
@competence_controller.route('/competences/comp_type/<string:comp_type>', methods=['GET'])
def get_competences_by_type(comp_type):
    #Obtiene todas las competencias por tipo.
    response = CompetenceService.get_competences_by_type(comp_type)
    return jsonify(response), 200 if isinstance(response, list) else 400

@competence_controller.route('/competences/linked/<int:program_comp_id>', methods=['GET'])
def get_linked_competences(program_comp_id):
    #Obtiene competencias vinculadas a una competencia padre.
    response = CompetenceService.get_linked_competences(program_comp_id)
    return jsonify(response), 200 if isinstance(response, list) else 400
"""
