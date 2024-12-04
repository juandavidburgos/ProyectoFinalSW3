from flask import Blueprint, render_template, request, redirect, url_for, flash
from Services.evaluatorService import EvaluatorService

#CONTROLADOR GESTION DE Evaluadores

#Blueprint para el controlador de evvaluador
evaluator_blueprint = Blueprint('evaluator', __name__)


# Metodo crear 
@evaluator_blueprint.route('/create_evaluator', methods=['GET', 'POST'])
def create_evaluator():
    if request.method == 'POST':
        #Se obtienen los datos del formulario y se convierten a un diccionario
        data = request.form.to_dict()
        print(f"Datos recibidos: {data}")#verificar que se esten pasando los datos
        #Se llama al servicio para crear el docente
        new_evaluator, error = EvaluatorService.create_evaluator(data)

        #En caso de que ocurra un error  
        if error:
            #se muestra un mensaje
            flash(error, 'error')
            #se redirige a la misma pagina para poder intentar de nuevo
            return redirect(url_for('evaluator.create_evaluator'))
        
        #En caso contrario se muestra un mensaje y se redirige a la misma pagina
        flash('Evaluador agregado exitosamente')
        return redirect(url_for('evaluator.create_evaluator'))
    
    #Si el metodo no es POST se muestra la vista del formulario
    return render_template('Evaluator/gestionEvaluator.html')

#Metodo para mostrar todos los docentes
@evaluator_blueprint.route('/search_allEvaluator')
def search_allEvaluator():
    #Se llama al servicio para obtener todos los docentes
    evaluators= EvaluatorService.get_all_evaluator()
    #Se muestra la vista de todos los docentes
    return render_template('Evaluator/searchEvaluator.html', evaluators=evaluators)

#Metodo para buscar un docente por su identificación
@evaluator_blueprint.route('/search_by_identificationEvaluator', methods=['GET', 'POST'])
def search_by_identificationEvaluator():
    if request.method == 'POST':
        #Se obtiene la identificación del formulario
        evaIdentification = request.form.get('evaIdentification')
        #Se llama al servicio
        byIdentificationEvaluator,error = EvaluatorService.search_by_identificationEvaluator(evaIdentification)
        #En caso de que ocurra un error
        if error:
            #Se muestra un mensaje
            flash(error, 'error')
            #Se redirige a la misma pagina para intentar de nuevo
            return redirect(url_for('evaluator.searchEvaluator'))
        #En caso contrario se muestra la vista con el docente encontrado
        return render_template('Evaluator/searchEvaluator.tml', evaluator=byIdentificationEvaluator)
    return render_template('Evaluator/searchEvaluator.html')

#Metodo para buscar un docente por su apellido
@evaluator_blueprint.route('/search_by_lastNameEvaluator', methods=['GET', 'POST'])
def search_by_lastNameEvaluator():
    if request.method == 'POST':
        #Se obtiene el apellido del formulario
        evaLastName = request.form.get('evaLastName')
        #print(f"Datos recibidos: {teLastName}")#verificar que se esten pasando los datos

        byLastNameEvaluator,error = EvaluatorService.search_by_identificationEvaluator(evaLastName)
        if error:
            flash(error, 'error')
            return redirect(url_for('evaluator.searchEvaluator'))
        #En caso contrario se muestra la vista con el docente encontrado
        return render_template('Evaluator/searchEvaluator.html', evaluator=byLastNameEvaluator)
    return render_template('Evaluator/searchEvaluator.html')
        
#Metodo para editar un docente
@evaluator_blueprint.route('/edit_evaluator/<teIdentification>', methods=['GET', 'POST'])
def edit_evaluator(evaIdentification):
    if request.method == 'POST':
        # Obtener datos del formulario
        data = request.form.to_dict()
        print(f"Datos recibidos para editar: {data}")  # Para depuración

        # Llamar al servicio para actualizar 
        updated_evañuator, error = EvaluatorService.edit_evaluator(evaIdentification, data)
    
        # En caso de error, mostrar mensaje y redirigir
        if error:
            flash(error, 'error')
            return redirect(url_for('evaluator.edit_evaluator', evaIdentification=evaIdentification))

        # Mostrar mensaje de éxito
        flash('Evaluador actualizado exitosamente')
        return redirect(url_for('Evaluator/evaluator.search_allevaluator'))

    # Si es GET, buscar el evaluador y mostrar los datos en el formulario
    evaluator, error = EvaluatorService.search_by_identificationEvaluator(evaIdentification)
    if error:
        flash(error, 'error')
        return redirect(url_for('evaluator.search_allEvaluator'))

    return render_template('Evaluator/editEvaluator.html', evaluator=evaluator)

