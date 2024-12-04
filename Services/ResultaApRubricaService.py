from Model.ResultaApRubrica import ResultaApRubrica
from Model.rubric import Rubric
from Model.evaluator import Evaluator
from Model.learningOutcome import LearningOutcome
from Model.competence import Competence
from Model.connection import db

class ResultaApRubricaService:

    @staticmethod
    def create_learning_outcome_rubric(lo_id, rubric_id):
        "Se le asigna un RA a una rubrica"
        try:
            # Crear una nueva instancia de ResultaApRubrica con los datos proporcionados
            resultaApRubrica = ResultaApRubrica(lo_id=lo_id, rubric_id=rubric_id)
            
            # Agregar la relación a la sesión y hacer commit
            db.session.add(resultaApRubrica)
            db.session.commit()

            return "Asignación realizada exitosamente", None
        except Exception as e:
            db.session.rollback()  # Si hay error, hacer rollback
            return None, f"Error al realizar la asignación: {str(e)}"
    @staticmethod    
    def get_next_learning_id():
        #obtiene el siguiente ID disponible para rubric_id para no tener conflictos
        max_rubric_id = db.session.query(db.func.max(LearningOutcome.lout_id)).scalar()
        return (max_rubric_id or 0) + 1  # Si no hay registros, comienza desde 1
    
    @staticmethod
    def create_rubric_learning_outcome(rubric_data,lo_data):
        try:
            # Crear una nueva instancia de Rubric con los datos proporcionados
            rubric = Rubric(**rubric_data)
            db.session.add(rubric)
            db.session.commit()

            # Obtener el siguiente ID disponible para LearningOutcome
            next_lo_id = ResultaApRubricaService.get_next_learning_id()

            # Crear una nueva instancia de LearningOutcome con los datos proporcionados
            learning_outcome = LearningOutcome(lout_id=next_lo_id, **lo_data)
            db.session.add(learning_outcome)
            db.session.commit()

            # Asociar el LearningOutcome a la Rubric
            return ResultaApRubricaService.create_learning_outcome_rubric(learning_outcome.lout_id, rubric.rubric_id)
        except Exception as e:
            db.session.rollback()
            return None, f"Error al crear la rúbrica y asociar el resultado de aprendizaje: {str(e)}"

    @staticmethod
    def update_learning_outcome(lo_id, data):
        """Actualiza un Resultado de Aprendizaje existente"""
        # Buscar el Resultado de Aprendizaje por su ID
        try:
            learning_outcome = LearningOutcome.query.get(lo_id)
            if not learning_outcome:
                return None, "El Resultado de Aprendizaje no existe"
            learning_outcome.comp_id = int(data.get('lo_id', learning_outcome.lo_id))
            learning_outcome.comp_id = int(data.get('comp_id', learning_outcome.comp_id))
            learning_outcome.lo_description = data.get('lo_description', learning_outcome.lo_description)

            db.session.commit()
            return  learning_outcome,None
        except ValueError:
            db.session.rollback()
            return None, ValueError("Datos proporcionados NO validos.")
        except Exception as e:
            db.session.rollback()
            return None, f"Error inesperado: {str(e)}"

    @staticmethod
    def get_learning_outcomes_by_rubric(rubric_id):
        """Obtiene todos los Resultados de Aprendizaje asociados a una rubrics"""
        # Validar que la rubrica existe
        rubric = rubric.query.get(rubric_id)
        if not rubric:
            return None, "La competencia especificada no existe"

        # Consultar los Resultados de Aprendizaje asociados
        learning_outcomes = LearningOutcome.query.filter_by(rubric_id=rubric_id).all()
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
def get_learning_outcomes_by_competence_type(competence_type):
    """Obtiene todos los Resultados de Aprendizaje asociados a una competencia de tipo asignatura"""
    try:
        # Consultar los Resultados de Aprendizaje asociados a competencias de tipo asignatura
        learning_outcomes = (db.session.query(LearningOutcome)
                             .join(Competence, LearningOutcome.comp_id == Competence.comp_id)
                             .filter(Competence.type == competence_type)
                             .all())
        return [lo.to_dict() for lo in learning_outcomes], None
    except Exception as e:
        return None, f"Error al obtener los Resultados de Aprendizaje: {str(e)}"
    
@staticmethod
def update_rubric_score(rubric_id, evaluator_id, new_score):
    """Actualiza la nota de una rúbrica por su ID y el ID del evaluador"""
    try:
        # Buscar la rúbrica por su ID
        rubric = Rubric.query.get(rubric_id)
        if not rubric:
            return None, "La rúbrica no existe"

        # Buscar el evaluador por su ID
        evaluator = Evaluator.query.get(evaluator_id)
        if not evaluator:
            return None, "El evaluador no existe"

        # Actualizar la nota de la rúbrica
        rubric.score = new_score

        db.session.commit()
        return "Nota actualizada exitosamente", None
    except Exception as e:
        db.session.rollback()
        return None, f"Error al actualizar la nota de la rúbrica: {str(e)}"