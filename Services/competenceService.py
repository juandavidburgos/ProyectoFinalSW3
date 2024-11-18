from Model.competence import Competence
from Model.connection import db

class CompetenceService:
    @staticmethod
    def create_competence(comp_description, comp_type,comp_level, program_comp_id=None):
        """Crea una nueva competencia."""
        try:
            new_competence = Competence(
                comp_description=comp_description,
                comp_type=comp_type,
                comp_level=comp_level,
                program_comp_id=program_comp_id
            )
            db.session.add(new_competence)
            db.session.commit()
            return {"message": "Competence created successfully", "data": new_competence.to_dict()}
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}

    @staticmethod
    def update_competence(comp_id, comp_description, comp_type,comp_level, program_comp_id=None):
        """Actualiza una competencia existente."""
        try:
            competence = Competence.query.get(comp_id)
            if not competence:
                return {"error": "Competence not found"}

            competence.comp_description = comp_description
            competence.comp_type = comp_type
            competence.comp_level = comp_level
            competence.program_comp_id = program_comp_id

            db.session.commit()
            return {"message": "Competence updated successfully", "data": competence.to_dict()}
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}

    @staticmethod
    def get_competences_by_type(comp_type):
        """Obtiene todas las competencias por tipo."""
        try:
            competences = Competence.query.filter_by(comp_type=comp_type).all()
            return [competence.to_dict() for competence in competences]
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def get_linked_competences(program_comp_id):
        """Obtiene competencias vinculadas a una competencia padre."""
        try:
            linked_competences = Competence.query.filter_by(program_comp_id=program_comp_id).all()
            return [competence.to_dict() for competence in linked_competences]
        except Exception as e:
            return {"error": str(e)}
