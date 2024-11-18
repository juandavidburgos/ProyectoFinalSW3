#Clase DOCENTE
from enum import Enum
from connection import db  # Importa el db desde connection.py

class TypeTeacher(Enum):
    PLANT = 'Planta'
    FULLTIME = 'Tiempo completo'
    CATHEDRA = 'Catedra'

class TypeIdentification(Enum):
    CIVILREGISTRY = 'Registro Civil'
    TARJETAIDENTIDAD = 'Tarjeta de identidad'
    CEDULA = 'Cedula'
    PASAPORTE = 'Pasaporte'
    CEDULAEXTRANJERIA = 'cedula extranjeria'

    
class Teacher(db.Model):
    __tablename__ = 'TBL_Docente'  # Nombre de la tabla en la base de datos

    #Se definen las columnas que tiene la tabla en la base de datos
    teId= db.Column(db.Integer, primary_key=True, nullable=False)
    teTypeIdentification = db.Column(db.Enum(TypeIdentification), nullable=False)
    teIdentification = db.Column(db.String(100), nullable=False)
    teTypeTeacher = db.Column(db.Enum(TypeTeacher), nullable=False)
    teName = db.Column(db.String(100), nullable=False)
    teLastName = db.Column(db.String(100), nullable=False)
    teLastTitle = db.Column(db.String(100), nullable=False)
    teEmail = db.Column(db.String(100), nullable=False)

    #Constructor de la clase
    def __init__(self,teTypeIdentification=None, teIdentification=None, teTypeTeacher=None, teName=None,teLastName=None, teLastTitle=None, teEmail=None):
        self.teTypeIdentification = teTypeIdentification
        self.teIdentification = teIdentification
        self.teTypeTeacher = teTypeTeacher
        self.teName = teName
        self.teLastName = teLastName 
        self.teLastTitle = teLastTitle 
        self.teEmail = teEmail

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
            "teEmail": self.teEmail
        }
    
#convierte un diccionario en una instancia de la clase Teacher
def from_dict(data): #TODO: Se debe pasar el id?
    return Teacher(
        teId=data.get("teId"),
        teTypeIdentification=TypeIdentification(data.get("teTypeIdentification")),
        teIdentification=data.get("teIdentification"),
        teTypeTeacher=TypeTeacher(data.get("teTypeTeacher")),
        teName=data.get("teName"),
        teLastName=data.get("teLastName"),
        teLastTitle=data.get("teLastTitle"),
        teEmail=data.get("teEmail")
    )
        

        
        