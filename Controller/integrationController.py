#holaaaaaaaaaa
from flask import Blueprint, render_template, request, redirect, url_for, flash
from Facade.integrationFacade import IntegrationFacade

integration_bp = Blueprint('integration', __name__)

@integration_bp.route('/to_subject', methods=['GET', 'POST'])
def assign_to_subject():
    facade = IntegrationFacade()

    competences, error=facade.get_competences()
    subjects, error= facade.get_subjects()
    teachers, error= facade.get_teachers()

    if error:
        flash(f"Error desconocido: {str(error)}", "danger")

    if request.method == 'POST':
        data = request.form.to_dict()
        print(f"Formulario recibido: {data}")
        try:
            selected_comp_id = data['competence_id']
            selected_subject_id = data['subject_id']
            selected_teacher_id = data ['teacher_id']
            time = data['time']
            sub_competence_data={
                'comp_description': data['cmp_subject_description'],
                'comp_type': data['comp_type'],
                'comp_level':data.get['comp_level']
            } 

            raa_data={'lout_description':data['lout_sub_description']}

            facade.assign_to_subject(selected_comp_id,selected_teacher_id,selected_subject_id, time)
            facade.create_subject_competence(sub_competence_data,raa_data)
            flash("Asignación exitosa y competencia de asignatura creada!", "success")
            return redirect(url_for('integration.assign_to_subject'))
        except KeyError as e:
            flash(f"Error: Falta el campo {str(e)} en el formulario.", "danger")
        except Exception as e:
            flash(f"Error al asignar y crear competencia: {e}", "danger")

    if competences or subjects or teachers is None:
        flash(f"Error: {error}", "danger")
        competences = []  # Asegurarse de que 'competences' sea una lista vacía si ocurre un error
        subjects = []  # Asegurarse de que 'subjects' sea una lista vacía si ocurre un error
        teachers = []  # Asegurarse de que 'teachers' sea una lista vacía si ocurre un error
    return render_template('Competence/assigns.html', competences=competences, subjects=subjects, teachers=teachers)
