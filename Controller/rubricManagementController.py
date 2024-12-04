#* CONTROLADOR GESTION RUBRICA
from flask import Blueprint, render_template, request, redirect, url_for, flash
from Services.rubricService import RubricService

#Blueprint para el controlador de rubrica
rubric_blueprint = Blueprint('rubric', __name__)

#GET:Sirve para mostrar el formulario para crear un docente 
#POST:Sirve para crear un docente en la base de datos 

# Metodo crear rubrica
@rubric_blueprint.route('/create_rubric', methods=['GET', 'POST'])
def create_rubric():
    if request.method == 'POST':
        #Se obtienen los datos del formulario y se convierten a un diccionario
        data = request.form.to_dict()
        print(f"Datos recibidos: {data}")#verificar que se esten pasando los datos
        #Se llama al servicio para crear el docente
        new_rubric, error = RubricService.create_rubric(data)

        #En caso de que ocurra un error  
        if error:
            #se muestra un mensaje
            flash(error, 'error')
            #se redirige a la misma pagina para poder intentar de nuevo
            return redirect(url_for('rubric.create_rubric'))
        
        #En caso contrario se muestra un mensaje y se redirige a la misma pagina
        flash('Rubrica agregada exitosamente')
        return redirect(url_for('rubric.create_rubric'))
    
    #Si el metodo no es POST se muestra la vista del formulario
    return render_template('Rubricc/createRubric.html')
#Metodo para mostrar todos las rubricas
@rubric_blueprint.route('/search_allRubric')
def search_allRubricr():
    #Se llama al servicio para obtener todos las rubricas
    rubrics = RubricService.get_all_Rubric()
    #Se muestra la vista de todos los docentes
    return render_template('Rubricc/createRubric.html', rubrics=rubrics)

#Metodo para buscar un 
@rubric_blueprint.route('/search_by_criterion_description', methods=['GET', 'POST'])
def search_by_criterion_description(criterion_description):
    if request.method == 'POST':
        #Se obtiene el apellido del formulario
        criterion_description = request.form.get('criterion_description')
        #Se llama al servicio
        byCriterion_description,error = RubricService.search_by_criterion_description(criterion_description)
        if error:
            flash(error, 'error')
            return redirect(url_for('rubric.searchRubric'))
        #En caso contrario se muestra la vista con el docente encontrado
        return render_template('rubric/searchRubric.html', rubrics=byCriterion_description)
    return render_template('Rubric/searchRubric.html')
        
    
#Metodo para buscar una rubrica por el nivel desempeño
@rubric_blueprint.route('/search_by_rub_level', methods=['GET', 'POST'])
def search_by_rub_level():
    if request.method == 'POST':
        #Se obtiene la identificación del formulario
        rub_level = request.form.get('rub_level')
        print(f"Datos recibidos: {rub_level}")#verificar que se esten pasando los datos
        #Se llama al servicio
        byRub_level,error = RubricService.search_by_rub_level(rub_level)
        #En caso de que ocurra un error
        if error:
            #Se muestra un mensaje
            flash(error, 'error')
            #Se redirige a la misma pagina para intentar de nuevo
            return redirect(url_for('rubric.searchRubric'))
        #En caso contrario se muestra la vista con el docente encontrado
        return render_template('Rubric/searchRubric.html', rubrics=byRub_level)
    return render_template('Rubric/searchRubric.html')

#Metodo para editar una rubrica
@rubric_blueprint.route('/edit_rubric/<rub_name>', methods=['GET', 'POST'])
def edit_rubric(rub_name):
    if request.method == 'POST':
        # Obtener datos del formulario
        data = request.form.to_dict()
        print(f"Datos recibidos para editar: {data}")  # Para depuración

        # Llamar al servicio para actualizar el docente
        updated_rubric, error = RubricService.edit_rubric(rub_name, data)

        # En caso de error, mostrar mensaje y redirigir
        if error:
            flash(error, 'error')
            return redirect(url_for('rubric.edit_rubric', rub_name=rub_name))

        # Mostrar mensaje de éxito
        flash('Docente actualizado exitosamente')
        return redirect(url_for('Rubric/.search_allRubric'))

    # Si es GET, buscar el docente y mostrar los datos en el formulario
    rubric, error = RubricService.search_by_name(rub_name)
    if error:
        flash(error, 'error')
        return redirect(url_for('rubric.search_allRubric'))

    return render_template('Rubric/editRubric.html', rubric=rubric)
