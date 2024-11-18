#Clase
#*COMPETENCIA
from connection import db  # Importa db desde connection.py
class Competence(db.Model):
    __tablename__ = 'TBL_COMPETENCIA'  # Nombre de la tabla

    comp_id = db.Column('COMP_ID', db.Integer, primary_key=True, autoincrement=True)  # ID de competencia
    comp_description = db.Column('COMP_DESCRIPCION', db.String(250), nullable=False)  # Descripción de la competencia
    comp_type = db.Column('COMP_TIPO', db.String(50), nullable=False)  # Tipo de competencia
    comp_level = db.Column('COMP_NIVEL', db.String(50), nullable=True)  # Nivel de competencia
    program_comp_id = db.Column('COMP_IDPROGRAMA', db.Integer, nullable=True)  # ID de la competencia de programa asociada

    def __init__(self, comp_description, comp_type, comp_level, program_comp_id):
        self.comp_description = comp_description
        self.comp_type = comp_type
        self.comp_level = comp_level
        self.program_comp_id = program_comp_id

    def to_dict(self):
        return {
            "comp_id": self.comp_id,
            "comp_description": self.comp_description,
            "comp_type": self.comp_type,
            "comp_level": self.comp_level,
            "program_comp_id": self.program_comp_id
        }

    @staticmethod
    def from_dict(data):
        return Competence(
            comp_id=data.get("comp_id"),
            comp_description=data.get("comp_description"),
            comp_type=data.get("comp_type"),
            comp_level=data.get("comp_level"),
            program_comp_id=data.get("program_comp_id")
        )
