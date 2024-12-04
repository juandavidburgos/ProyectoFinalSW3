#Clase
#*EVALUADOR
from enum import Enum
from .connection import db  # Importa el db desde connection.py

class Evaluator(db.Model):
    __tablename__ = 'TBL_EVALUADOR'  # Nombre de la tabla en la base de datos

    # Definición de las columnas
    evaId = db.Column('EVA_ID', db.Integer, primary_key=True, autoincrement=True)  # Identificador único
    evaTypeIdentification = db.Column('EVA_TIPOIDENTIFICACION', db.String(100), nullable=False)  # Tipo de identificación
    evaIdentification = db.Column('EVA_IDENTIFICACION', db.String(100), nullable=False)  # Número de identificación
    evaName = db.Column('EVA_NOMBRE', db.String(100), nullable=False)  # Nombre del evaluador
    evaLastName = db.Column('EVA_APELLIDO', db.String(100), nullable=False)  # Apellido del evaluador
    evaEmail = db.Column('EVA_CORREO', db.String(100), nullable=False)  # Correo del evaluador

    # Constructor
    def __init__(self, evaTypeIdentification=None, evaIdentification=None, evaName=None, evaLastName=None, evaEmail=None):
        self.evaTypeIdentification = evaTypeIdentification
        self.evaIdentification = evaIdentification
        self.evaName = evaName
        self.evaLastName = evaLastName
        self.evaEmail = evaEmail

    # Convierte una instancia a un diccionario
    def to_dict(self):
        return {
            "evaId": self.evaId,
            "evaTypeIdentification": self.evaTypeIdentification,
            "evaIdentification": self.evaIdentification,
            "evaName": self.evaName,
            "evaLastName": self.evaLastName,
            "evaEmail": self.evaEmail
        }

    # Convierte un diccionario a una instancia
    @staticmethod
    def from_dict(data):
        return Evaluator(
            evaTypeIdentification=data.get("evaTypeIdentification"),
            evaIdentification=data.get("evaIdentification"),
            evaName=data.get("evaName"),
            evaLastName=data.get("evaLastName"),
            evaEmail=data.get("evaEmail")
        )