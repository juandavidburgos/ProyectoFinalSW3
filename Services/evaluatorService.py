#Servicio Evaluador
from Model.evaluator import Evaluator
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

        
      