from Model.learningOutcome import LearningOutcome
from Model.connection import db

class LearningOutcomeService:
    @staticmethod
    def create_learning_outcome(comp_id, lo_description):
        """Crea un nuevo resultado de aprendizaje (RA)."""
        try:
            new_learning_outcome = LearningOutcome(
                comp_id=comp_id,
                lo_description=lo_description
            )
            db.session.add(new_learning_outcome)
            db.session.commit()
            return {"message": "Learning Outcome created successfully", "data": new_learning_outcome.to_dict()}
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}

    @staticmethod
    def update_learning_outcome(lo_id, comp_id, lo_description):
        """Actualiza un resultado de aprendizaje (RA) existente."""
        try:
            learning_outcome = LearningOutcome.query.get(lo_id)
            if not learning_outcome:
                return {"error": "Learning Outcome not found"}

            learning_outcome.comp_id = comp_id
            learning_outcome.lo_description = lo_description

            db.session.commit()
            return {"message": "Learning Outcome updated successfully", "data": learning_outcome.to_dict()}
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}

    @staticmethod
    def get_learning_outcomes_by_competencia(comp_id):
        """Obtiene todos los RA asociados a una competencia específica."""
        try:
            learning_outcomes = LearningOutcome.query.filter_by(comp_id=comp_id).all()
            return [learning_outcome.to_dict() for learning_outcome in learning_outcomes]
        except Exception as e:
            return {"error": str(e)}
