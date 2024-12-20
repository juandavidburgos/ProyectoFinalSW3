#Clase
#*RUBRICA
from connection import db  # Importa db desde connection.py

class Rubric(db.Model):
    __tablename__ = 'TBL_RUBRICA'  # Nombre de la tabla

    rub_id = db.Column('IDRUBRICA', db.Integer, primary_key=True, autoincrement=True)  # ID de la rúbrica
    evaluation_id = db.Column('EVA_ID', db.Integer, nullable=True)  # ID de evaluación
    rub_name = db.Column('RUB_NOMBRE', db.String(100), nullable=False)  # Nombre de la rúbrica
    rub_score = db.Column('RUB_NOTA', db.String(100), nullable=False)  # Nota de la rúbrica
    criterion_description = db.Column('RUB_CRITERIODESC', db.String(100), nullable=True)  # Descripción del criterio
    rub_level = db.Column('RUB_NIVEL', db.String(100), nullable=True)  # Nivel de la rúbrica

    def __init__(self, evaluation_id, rub_name, rub_score, criterion_description, rub_level):
        self.evaluation_id = evaluation_id
        self.rub_name = rub_name
        self.rub_score = rub_score
        self.criterion_description = criterion_description
        self.rub_level = rub_level

    def to_dict(self):
        return {
            "rub_id": self.rub_id,
            "evaluation_id": self.evaluation_id,
            "rub_name": self.rub_name,
            "rub_score": self.rub_score,
            "criterion_description": self.criterion_description,
            "rub_level": self.rub_level
        }

    @staticmethod
    def from_dict(data):
        return Rubric(
            rub_id=data.get("rub_id"),
            evaluation_id=data.get("evaluation_id"),
            rub_name=data.get("rub_name"),
            rub_score=data.get("rub_score"),
            criterion_description=data.get("criterion_description"),
            rub_level=data.get("rub_level")
        )

    