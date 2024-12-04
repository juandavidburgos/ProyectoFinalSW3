#Clase
#*EVALUADOR
from enum import Enum
from .connection import db # Importa el db desde connection.py

class Evaluator(db.Model):
    __tablename__ = 'TBL_EVALUADOR'  # Nombre de la tabla en la base de datos

    #Se definen las columnas que tiene la tabla en la base de datos
    # Definición de las columnas
    evaId = db.Column('EVA ID', db.Integer, primary_key=True, autoincrement=True)  # Identificador único
    evaTypeIdentification = db.Column('EVA TIPOIDENTIFICACION',db.String(50), nullable=False)  # Tipo de identificación
    evaIdentification = db.Column('EVA IDENTIFICACION', db.String(100), nullable=False)  # Número de identificación
    evaName = db.Column('EVA NOMBRE', db.String(100), nullable=False)  # Nombre del evaluador
    evaLastName = db.Column('EVA APELLIDO', db.String(100), nullable=False)  # Apellido del evaluador
    evaEmail = db.Column('EVA CORREO', db.String(100), nullable=False)  # Correo del evaluador
    
    evaluator = db.relationship('ResultaApRubrica', backref='evaluator') # Relación con Integration
    
    #Constructor de la clase
    def __init__(self,evaTypeIdentification=None, evaIdentification=None, evaName=None, evaLastName=None,evaEmail=None):
        self.evaTypeIdentification = evaTypeIdentification
        self.evaIdentification = evaIdentification
        self.evaName = evaName
        self.evaLastName = evaLastName 
        self.evaEmail = evaEmail

#convierte una instancia de la clase Teacher en un diccionario
#Esto es util para convertir el objeto en un JSON
    def to_dict(self):
        return {
            "evaId": self.evaId,
            "evaTypeIdentification": self.evaTypeIdentification,
            "evaIdentification": self.evaIdentification,
            "evaName": self.evaName,
            "evaLastName": self.evaLastName,
            "evaEmail": self.evaEmail
        }
    
#convierte un diccionario en una instancia de la clase Teacher
    @staticmethod
    def from_dict(data): 
        return Evaluador(
            evaId=data.get("evaId"),
            evaTypeIdentification=data.get("evaTypeIdentification"),
            evaIdentification=data.get("evaIdentification"),
            evaName=data.get("evaName"),
            evaLastName=data.get("evaLastName"),
            evaEmail=data.get("evaEmail")
        )
        

        
        