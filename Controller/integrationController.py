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
