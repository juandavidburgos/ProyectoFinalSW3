#Clase
#*RESULTADO DE APRENDIZAJE
from connection import db  # Importa db desde connection.py

class LearningOutcome(db.Model):
    __tablename__ = 'TBL_RA'  # Nombre de la tabla

    lo_id = db.Column('RAP_ID', db.Integer, primary_key=True, autoincrement=True)  # ID del resultado de aprendizaje
    comp_id = db.Column('COMP_ID', db.Integer, db.ForeignKey('TBL_COMPETENCIA.COMP_ID'), nullable=False)  # ID de competencia
    lo_description = db.Column('RAP_DESCRIPCION', db.String(250), nullable=False)  # Descripción del resultado de aprendizaje

    def __init__(self, comp_id, lo_description):
        self.comp_id = comp_id
        self.lo_description = lo_description

    def to_dict(self):
        return {
            "lo_id": self.lo_id,
            "comp_id": self.comp_id,
            "lo_description": self.lo_description
        }

    @staticmethod
    def from_dict(data):
        return LearningOutcome(
            lo_id=data.ge("lo_id"),
            comp_id=data.get("comp_id"),
            lo_description=data.get("lo_description")
        )

    