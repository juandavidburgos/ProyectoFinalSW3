#Clase
#*EVALUADOR
from enum import Enum
from .connection import db  # Importa el db desde connection.py

class Evaluator(db.Model):
    __tablename__ = 'TBL_EVALUADOR'  # Nombre de la tabla en la base de datos

    # Definición de las columnas
    evId = db.Column('EVA_ID', db.Integer, primary_key=True, autoincrement=True)  # Identificador único
    evTypeIdentification = db.Column('EVA_TIPOIDENTIFICACION', db.String(100), nullable=False)  # Tipo de identificación
    evIdentification = db.Column('EVA_IDENTIFICACION', db.String(100), nullable=False)  # Número de identificación
    evName = db.Column('EVA_NOMBRE', db.String(100), nullable=False)  # Nombre del evaluador
    evLastName = db.Column('EVA_APELLIDO', db.String(100), nullable=False)  # Apellido del evaluador
    evEmail = db.Column('EVA_CORREO', db.String(100), nullable=False)  # Correo del evaluador

    # Constructor
    def __init__(self, evTypeIdentification=None, evIdentification=None, evName=None, evLastName=None, evEmail=None):
        self.evTypeIdentification = evTypeIdentification
        self.evIdentification = evIdentification
        self.evName = evName
        self.evLastName = evLastName
        self.evEmail = evEmail

    # Convierte una instancia a un diccionario
    def to_dict(self):
        return {
            "evId": self.evId,
            "evTypeIdentification": self.evTypeIdentification.value,
            "evIdentification": self.evIdentification,
            "evName": self.evName,
            "evLastName": self.evLastName,
            "evEmail": self.evEmail
        }

    # Convierte un diccionario a una instancia
    @staticmethod
    def from_dict(data):
        return Evaluator(
            evTypeIdentification=TypeIdentification(data.get("evTypeIdentification")),
            evIdentification=data.get("evIdentification"),
            evName=data.get("evName"),
            evLastName=data.get("evLastName"),
            evEmail=data.get("evEmail")
        )