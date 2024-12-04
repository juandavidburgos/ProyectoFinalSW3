from Model.learningOutcome import LearningOutcome
from Model.connection import db
from Model.competence import Competence  # Importar la clase Competence para validar comp_id
class LearningOutcomeService:
    @staticmethod
    def create_learning_outcome(data):
        """Crea un nuevo Resultado de Aprendizaje"""
        # Validaciones de los datos
        if not data.get('lout_description') or not data.get('comp_id'):
            return None, "La descripción y el ID de la competencia son requeridos"

        # Validar que el comp_id esté asociado a una competencia existente
        competence = Competence.query.get(data['comp_id'])
        if not competence:
            return None, "El ID de la competencia proporcionado no existe"

        # Crear el nuevo Resultado de Aprendizaje
        new_learning_outcome = LearningOutcome(
            comp_id=data['comp_id'],
            lo_description=data['lout_description']
        )

        try:
            db.session.add(new_learning_outcome)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return None, f"Error en la base de datos: {str(e)}"

        return new_learning_outcome, None
    
    @staticmethod
    def update_learning_outcome(lout_id, data):
        #Actualiza un Resultado de Aprendizaje existente
        # Buscar el Resultado de Aprendizaje por su ID
        try:
            learning_outcome = LearningOutcome.query.filter_by(lout_id=lout_id).first()
            if not learning_outcome:
                return None, "El Resultado de Aprendizaje no existe"
            learning_outcome.lout_description = data.get('lout_description', learning_outcome.lout_description)

            db.session.commit()
            return  learning_outcome,None
        except ValueError:
            db.session.rollback()
            return None, ValueError("Datos proporcionados NO validos.")
        except Exception as e:
            db.session.rollback()
            return None, f"Error inesperado: {str(e)}"

    @staticmethod
    def get_learning_outcomes_by_competencia(comp_id):
        """Obtiene todos los Resultados de Aprendizaje asociados a una Competencia"""
        # Validar que la competencia existe
        print("ENTRO?")
        competence = Competence.query.get(comp_id)
        if not competence:
            return None, "La competencia especificada no existe"

        # Consultar los Resultados de Aprendizaje asociados
        learning_outcomes = LearningOutcome.query.filter_by(comp_id=comp_id).all()
        return [lo.to_dict() for lo in learning_outcomes], None
    
    @staticmethod
    def get_all_learning_outcomes():
        """Obtiene todos los Resultados de Aprendizaje"""
        try:
            # Consultar todos los Resultados de Aprendizaje
            learning_outcomes = LearningOutcome.query.all()
            print (learning_outcomes)
            # Convertir los objetos a diccionarios
            return [lo.to_dict() for lo in learning_outcomes], None
        except Exception as e:
            return None, f"Error al obtener los Resultados de Aprendizaje: {str(e)}"
    
    @staticmethod
    def get_learning_outcome_by_id(lout_id):
        # Validaciones de los datos
        if not lout_id:
            return None, "El ID es requerido"

        learningOutcome = LearningOutcome.query.filter_by(lout_id=lout_id).first()
        if not learningOutcome:
            return None, f"No se encontro un RA con ese ID {lout_id}."
        learningOutcome_dict = learningOutcome.to_dict()
        return learningOutcome_dict, None

