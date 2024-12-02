#Clase
#*COMPETENCIA
from .connection import db  # Importa db desde connection.py
class Competence(db.Model):
    __tablename__ = 'TBL_COMPETENCIA'  # Nombre de la tabla

    comp_id = db.Column('COMP_ID', db.Integer, primary_key=True, autoincrement=True)  # ID de competencia
    comp_description = db.Column('COMP_DESCRIPCION', db.String(250), nullable=False)  # Descripción de la competencia
    comp_type = db.Column('COMP_TIPO', db.String(50), nullable=False)  # Tipo de competencia
    comp_level = db.Column('COMP_NIVEL', db.String(50), nullable=False)  # Nivel de competencia
    comp_subject_id =db.Column('COMP_IDASIGNATURA',db.Integer, db.ForeignKey('TBL_COMPETENCIA.COMP_ID'), nullable=True)  # Relación recursiva

    # Relación con ResultProgram
    programLearningOutcome = db.relationship('LearningOutcome', backref='competence', lazy=True)

    # Relación recursiva con la propia competencia (si es necesario)
    programCompetence = db.relationship('Competence', remote_side=[comp_id], backref='subcompetencies', lazy=True)

    def __init__(self, comp_description, comp_type, comp_level, comp_subject_id=None):
        self.comp_description = comp_description
        self.comp_type = comp_type
        self.comp_level = comp_level
        self.comp_subject_id = comp_subject_id

    def to_dict(self):
        return {
            "comp_id": self.comp_id,
            "comp_description": self.comp_description,
            "comp_type": self.comp_type,
            "comp_level": self.comp_level,
            "comp_subject_id": self.comp_subject_id if self.comp_subject_id is not None else 'null',
            'programLearningOutcome': [rap.to_dict() for rap in self.programLearningOutcome]  # Aquí estamos asegurándonos de incluir los RAPs
        }

    @staticmethod
    def from_dict(data):
        return Competence(
            comp_id=data.get("comp_id"),
            comp_description=data.get("comp_description"),
            comp_type=data.get("comp_type"),
            comp_level=data.get("comp_level"),
            comp_subject_id=data.get("comp_subject_id")
        )
