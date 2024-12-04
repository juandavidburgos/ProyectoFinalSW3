#Servicio Evaluador
from Model.evaluator import Evaluator
from Model.rubric import Rubric
from Model.connection import db

class EvaluatorService:

    @staticmethod
    def create_evaluator(data):
        print(f"Datos recibidos en el servicio: {data}")
        # Validacion de los datos requeridos
        if not data.get('evaTypeIdentification') or not data.get('evaIdentification') \
            or not data.get('evaName') or not data.get('evaLastName') or not data.get('evaEmail'):

            return None, "Todos los campos son requeridos"
        
        # Crear un nuevo evaluador
        new_evaluator = Evaluator(
            evaTypeIdentification= ['evaTypeIdentification'],
            evaIdentification=data['evaIdentification'],
            evaName=data['evaName'],
            evaLastName=data['evaLastName'],
            evaEmail=data['evaEmail']
        )
        
        try:
            db.session.add(new_evaluator)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return None, f"Ha ocurrido un error en la base de datos: {str(e)}"

        return new_evaluator, None
    
    @staticmethod
    def get_all_evaluator():
        #*Obtiene todos los evaluadores
        try:
            # Consultar todos los evaluadores 
            # Consultar solo los campos requeridos
            evaluators = db.session.query(Evaluator.evaId , Evaluator.evaName, Evaluator.evaLastName).all()

            if not evaluators:
                return [], "No se encontraron evaluadores."
            # Convertir las tuplas resultantes en una lista de diccionarios
            evaluators_dict = [{"evaId": evalu.evaId, "evaName": evalu.teName, "evaLastName": evalu.evaLastName} for evalu in evaluators]
        
            print(evaluators_dict)  # Esto imprimirá el contenido de los diccionarios
            
            return evaluators_dict, None  # Devolver los resultados como lista de diccionarios
        except Exception as e:
            # En caso de error, devolver el mensaje de error
            return [], f"Error al obtener los evaluadores: {str(e)}"
        
    @staticmethod
    def search_by_identificationEvaluator(evaIdentification):
        try:
            #Busca todos los evaluadores por su identificación
            teacher = Evaluator.query.filter_by(evaIdentification=evaIdentification).all()
            if teacher:
                return teacher, None
            return None, "Evaluador no encontrado"
        except Exception as e:
            return None, f"Error al buscar al evaluador {str(e)}"
    
    @staticmethod
    def search_by_lastNameEvaluator(evaLastName):
        try:
            #Buscar todos los evaluadores por su apellido
            teacher = Evaluator.query.filter_by(evaLastName=evaLastName).all()
            if teacher:
                return teacher, None
            return None, "No se encontraron evaluadores con el apellido especificado"
        except Exception as e:
            return None, f"Error al buscar al evaluador {str(e)}"
        
 
    @staticmethod
    def edit_evaluator(evaIdentification,data):
        
            #Buscar el evaluador por su identificación
            evaluator = Evaluator.query.filter_by(evaIdentification=data['evaIdentification']).first()
            if not evaluator:
                return None, "Evaluador no encontrado"
            try:
                #Actualizar los datos del evaluador
                evaluator.evaTypeIdentification = data['evaTypeIdentification']
                evaluator.evaIdentification = data['evaIdentification']
                evaluator.evaName = data['evaName']
                evaluator.evaLastName = data['evaLastName']
                evaluator.evaEmail = data['evaEmail']

                db.session.commit()
                return evaluator, None
            except ValueError:
                db.session.rollback()
                return None, ValueError("Datos proporcionados NO validos.")
            
            except Exception as e:
                db.session.rollback()
                return None, f"Error inesperado: {str(e)}"

        
"""- Evalua RA de de estudiantes con RUBRICAS PREDEFINIDAS
- NO PUEDE MODIFICAR RA NI COMPETENCIAS

>> Visualización de RA asignatura
- Se muestran las rubricas asociadas a ese RA
- Selecciona una rubrica (Boton al frente de cada una que diga "Seleccionar")
- Permite ingresar una puntuación (Nota), es decir, permite editar el campo NOTA de rubrica
- Guardar"""
@staticmethod
 def get_all_RASubject():
        try:
            rubric=db.session.query(Rubric.rubId, Rubric.rubName, Rubric.rubDescription, Rubric.criterion_description, Rubric.).all()
            # Consultar todos los RA de la asignatura
            RA = RA.query.all()
            print (RA)
            # Convertir los objetos a diccionarios
            return [ra.to_dict() for ra in RA], None
        except Exception as e:
            return None, f"Error al obtener los RA de la asignatura: {str(e)}"
        

        #*Obtiene todos los evaluadores
        try:
            # Consultar todos los evaluadores 
            # Consultar solo los campos requeridos
            evaluators = db.session.query(Evaluator.evaId , Evaluator.evaName, Evaluator.evaLastName).all()

            if not evaluators:
                return [], "No se encontraron evaluadores."
            # Convertir las tuplas resultantes en una lista de diccionarios
            evaluators_dict = [{"evaId": evalu.evaId, "evaName": evalu.teName, "evaLastName": evalu.evaLastName} for evalu in evaluators]
        
            print(evaluators_dict)  # Esto imprimirá el contenido de los diccionarios
            
            return evaluators_dict, None  # Devolver los resultados como lista de diccionarios
        except Exception as e:
            # En caso de error, devolver el mensaje de error
            return [], f"Error al obtener los evaluadores: {str(e)}"