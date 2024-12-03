#Clase
#*RESULTADO DE APRENDIZAJE
from .connection import db  # Importa db desde connection.py

class LearningOutcome(db.Model):
    __tablename__ = 'TBL_RA'  # Nombre de la tabla

    lout_id = db.Column('RAP_ID', db.Integer, primary_key=True, autoincrement=True)  # ID del resultado de aprendizaje
    lout_description = db.Column('RAP_DESCRIPCION', db.String(250), nullable=False)  # Descripción del resultado de aprendizaje
    lout_subject_id =db.Column('RASIG_ID',db.Integer, db.ForeignKey('TBL_RA.RAP_ID'), nullable=True)  # Relación recursiva

    comp_id = db.Column(db.Integer, db.ForeignKey('TBL_COMPETENCIA.COMP_ID'), nullable=False)  # Relación con Competencia (clave foránea)

    # Relación recursiva con el propio RA (si es necesario)
    raProgram = db.relationship('LearningOutcome', remote_side=[lout_id], backref='sublearningoutcome', lazy=True)

    def __init__(self, lout_description,comp_id,lout_subject_id=None):
        self.lout_description = lout_description
        self.lout_subject_id=lout_subject_id 
        self.comp_id = comp_id

    def to_dict(self):
        return {
            "lout_id": self.lout_id,
            "comp_id": self.comp_id,
            "lout_description": self.lout_description,
            "lout_subject_id":self.lout_subject_id if self.lout_subject_id is not None else 'null'
        }

    @staticmethod
    def from_dict(data):
        return LearningOutcome(
            lout_id=data.get("lout_id"),
            comp_id=data.get("comp_id"),
            lout_description=data.get("lout_description"),
            lout_subject_id=data.get("lout_subject_id")
            
        )

    