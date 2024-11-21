#Clase DOCENTE
from enum import Enum
from .connection import db # Importa el db desde connection.py

class TypeTeacher(Enum):
    PLANT = 'Planta'
    FULLTIME = 'Tiempo completo'
    CATHEDRA = 'Catedra'

class TypeIdentification(Enum):
    CIVILREGISTRY = 'Registro Civil'
    TARJETAIDENTIDAD = 'Tarjeta de identidad'
    CEDULA = 'Cédula'
    PASAPORTE = 'Pasaporte'
    CEDULAEXTRANJERIA = 'Cédula extranjeria'

class Teacher(db.Model):
    __tablename__ = 'TBL_Docente'  # Nombre de la tabla en la base de datos

    #Se definen las columnas que tiene la tabla en la base de datos
    teId= db.Column('DOC_ID',db.Integer, primary_key=True,  autoincrement=True)
    teTypeIdentification = db.Column('DOC_TIPOIDENTIFICACION',db.Enum(TypeIdentification))
    teIdentification = db.Column('DOC_IDENTIFICACION',db.String(100), nullable=False)
    teTypeTeacher = db.Column('DOC_TIPODOCENTE',db.Enum(TypeTeacher))
    teName = db.Column('DOC_NOMBRES',db.String(100), nullable=False)
    teLastName = db.Column('DOC_APELLIDOS',db.String(100), nullable=False)
    teLastTitle = db.Column('DOC_TITULO',db.String(100), nullable=False)
    teEmail = db.Column('DOC_CORREO',db.String(100), nullable=False)
    teState = db.Column('DOC_ESTADO',db.String(50), default=True)

    #Constructor de la clase
    def __init__(self,teTypeIdentification=None, teIdentification=None, teTypeTeacher=None, teName=None,teLastName=None, teLastTitle=None, teEmail=None, teState = None):
        self.teTypeIdentification = teTypeIdentification
        self.teIdentification = teIdentification
        self.teTypeTeacher = teTypeTeacher
        self.teName = teName
        self.teLastName = teLastName 
        self.teLastTitle = teLastTitle 
        self.teEmail = teEmail
        self.teState = teState

#convierte una instancia de la clase Teacher en un diccionario
#Esto es util para convertir el objeto en un JSON
    def to_dict(self):
        return {
            "teId": self.teId,
            "teTypeIdentification": self.teTypeIdentification.value,
            "teIdentification": self.teIdentification,
            "teTypeTeacher": self.teTypeTeacher.value,
            "teName": self.teName,
            "teLastName": self.teLastName,
            "teLastTitle": self.teLastTitle,
            "teEmail": self.teEmail,
            "teState": self.teState
        }
    
#convierte un diccionario en una instancia de la clase Teacher
    @staticmethod
    def from_dict(data): #TODO: Se debe pasar el id?
        return Teacher(
            teId=data.get("teId"),
            teTypeIdentification=TypeIdentification(data.get("teTypeIdentification")),
            teIdentification=data.get("teIdentification"),
            teTypeTeacher=TypeTeacher(data.get("teTypeTeacher")),
            teName=data.get("teName"),
            teLastName=data.get("teLastName"),
            teLastTitle=data.get("teLastTitle"),
            teEmail=data.get("teEmail"),
            teState=data.get("teEstado")
        )
        

        
        