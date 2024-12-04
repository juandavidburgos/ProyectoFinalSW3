#holaaaaaaaaaa
from flask import Blueprint, render_template, request, redirect, url_for, flash
from Facade.integrationFacade import IntegrationFacade
from Facade.cmpLoutFacade import CmpLoutFacade

integration_bp = Blueprint('integration', __name__)

@integration_bp.route('/to_subject', methods=['GET', 'POST'])
def assign_to_subject():
    facadeInt = IntegrationFacade()
    
    # * Cargar combo box --------------------------------------------------
    # Validar competences
    cbxcompetences, error = facadeInt.get_competences()

    # Validar subjects
    cbxsubjects, error = facadeInt.get_subjects()

    # Validar teachers
    cbxteachers, error = facadeInt.get_teachers()

    # * FIN Cargar combo box --------------------------------------------------

    if request.method == 'POST':
        data = request.form.to_dict()
        print(f"Formulario recibido: {data}")
        try:
            selected_comp_id = data['competence_id']
            selected_subject_id = data['subject_id']
            selected_teacher_id = data ['teacher_id']
            time = data['time']

            if not selected_comp_id or not selected_subject_id or not selected_teacher_id:
                flash("Por favor, complete todos los campos del formulario.", "danger")
                return redirect(url_for('integration.assign_to_subject'))

            sub_competence_data={
                'comp_description': data['cmp_subject_description'],
                'comp_type': data['comp_type'],
                'comp_level':data.get('comp_level')
            } 
            print("DATOS COMPETENCIA DE ASIGNATURA")
            print(sub_competence_data)
            raa_data={'lout_description':data['lout_sub_description']}

            print("DATOS RAA DE ASIGNATURA")
            print(raa_data)

            facadeInt.assign_to_subject(selected_comp_id,selected_teacher_id,selected_subject_id, time)
            facadeInt.create_subject_competence(sub_competence_data,raa_data)
            flash("Asignación exitosa y competencia de asignatura creada!", "success")
            return redirect(url_for('integration.assign_to_subject'))
        except KeyError as e:
            flash(f"Error: Falta el campo {str(e)} en el formulario.", "danger")
        except Exception as e:
            flash(f"Error al asignar y crear competencia: {e}", "danger")

    competences, error = facadeInt.get_all_competences()
    assignments, error = facadeInt.get_assignments()

    if (competences is None) or (cbxcompetences is None) or (cbxsubjects is None) or (cbxteachers is None) or (assignments is None):
        competences = []  # Asegurarse de que 'competences' sea una lista vacía si ocurre un error
        cbxsubjects = []  # Asegurarse de que 'subjects' sea una lista vacía si ocurre un error
        cbxteachers = []  # Asegurarse de que 'teachers' sea una lista vacía si ocurre un error
        cbxcompetences = [] # Asegurarse de que 'competences' sea una lista vacía si ocurre un error
        assignments = []  # Asegurarse de que 'assignments' sea una lista vacía si ocurre un error
    return render_template('Competence/assigns.html', 
    cbxcompetences=cbxcompetences,
    cbxsubjects=cbxsubjects,
    cbxteachers=cbxteachers,
    competences=competences,
    assignments=assignments)

@integration_bp.route('/search_subject_comp', methods=['GET', 'POST'])
def search_subcomp():
    facade = IntegrationFacade()
    mostrar_nuevo_campo = False  # Flag para controlar si mostrar el nuevo campo
    competences = []
    if request.method == 'POST':
        data = request.form.to_dict()
        try:
            
            teacher_id = data['teacher_id']
            if not teacher_id:
                flash("Por favor, complete todos los campos del formulario.", "danger")
                return redirect(url_for('integration.search_subcomp'))

            print("LLEGAMOS ANTES DE LLAMAR ASSIGNMNET BY TICHER")
            assignment, error = facade.get_assignment_by_teacher(teacher_id)

            print("---------------")
            print(assignment)

            if error:
                flash(error, 'error')
                return redirect(url_for('integration.search_subcomp'))
            if assignment:
                competenceIds = [ass["comp_id"] for ass in assignment]
                competences , error = facade.get_competences_names_by_ids(competenceIds)
                if error:
                    print(error)
                mostrar_nuevo_campo = True
                flash(f"Consulta realizada con exito", "success")
                #return render_template('Teacher/searchLearningOutcome.html', assignment=assignment, idCompetencias=idCompetencias)
                return render_template('Teacher/searchLearningOutcome.html', assignment=assignment,competences=competences,mostrar_nuevo_campo=mostrar_nuevo_campo)
            
        except Exception as e:
            flash(f"Error al recuperar la asignacion: {e}", "danger")
    
    return render_template('Teacher/searchLearningOutcome.html')

@integration_bp.route('/get_subject_lout', methods=['GET', 'POST'])
def get_lout_by_competence():
    facade = IntegrationFacade()
    mostrar_cbx=False
    if request.method == 'POST':
        data = request.form.to_dict()
        try:
            print("ENTRAMOS A GET_LOUT_BY_COMPTENCE")
            selected_comp_id = data['competence_id']
            print(selected_comp_id)
            # Llamar al servicio para actualizar la asignatura
            raas, error = facade.get_lout_by_competence(selected_comp_id)
            print("pASAMOS A RASS,ERROR")
            print(raas)
            if error:
                flash(error, "danger")
                return redirect(url_for('integration.get_lout_by_competence'))
        
            if raas:
                raaIds = [lou["lout_id"] for lou in raas]
                raas,error = facade.get_lout_names_by_ids(raaIds)
                print("Entramos al if de raas")
                if error:
                    print(error)
                mostrar_cbx = True
                return render_template('Teacher/searchLearningOutcome.html',raas=raas,mostrar_cbx=mostrar_cbx)

        except Exception as e:
            flash(f"Error al recuperar el raa: {e}", "danger")

    return render_template('Teacher/searchLearningOutcome.html')


@integration_bp.route('/search_subject_lout', methods=['GET', 'POST'])
def search_subject_lout():
    facade = IntegrationFacade()
    if request.method == 'POST':
        data=request.form.to_dict()

        try:
            selected_raa = data['subject_lout_id']

            if not selected_raa:
                flash("Por favor, complete todos los campos del formulario.", "danger")
                return redirect(url_for('integration.search_subject_lout'))

            # Llamar al servicio para obtener la asignatura
            raa, error = facade.get_lout_by_id(selected_raa)

            print(raa)
            if error:
                flash(error, 'error')
                return redirect(url_for('integration.search_subject_lout'))
            if raa:

                return render_template('LearningOutcome/updateLearningOutcome.html',learning_outcome=raa)
            
        except Exception as e:
            flash(f"Error al recuperar el RAA: {e}", "danger")

    return render_template('Teacher/searchLearningOutcome.html')
""""
@integration_bp.route('/update_learning_outcome', methods=['GET', 'POST'])
def update_learning_outcome():
    facade = IntegrationFacade()
    learning_outcome = None
    if request.method == 'POST':
        data = request.form.to_dict()
        lout_id = data.get('lout_id')  # Obtener el nombre del formulario

        # Llamamos al servicio para actualizar el RA
        learning_outcome, error = facade.update_subject_lout(lout_id, data)
        if error:
            flash(error, "error")
            return redirect(url_for('learning_outcome.list_and_search_learning_outcomes', lout_id=lout_id))
        if learning_outcome:
            flash("RA actualizado con éxito!", 'success')
            return redirect(url_for('learning_outcome.list_and_search_learning_outcomes', lout_id=lout_id))  # Redirigimos usando el nombre actualizado

    # Si el método NO ES POST, se muestra la vista del formulario.
    return render_template('LearningOutcome/updateLearningOutcome.html', learning_outcome=learning_outcome)
"""