from enum import Enum
from .connection import db  # Importa la conexión a la base de datos

class TypeIdentification(Enum):
    CIVILREGISTRY = 'Registro Civil'
    TARJETAIDENTIDAD = 'Tarjeta de identidad'
    CEDULA = 'Cédula'
    PASAPORTE = 'Pasaporte'
    CEDULAEXTRANJERIA = 'Cédula extranjeria'

class Coordinator(db.Model):
    __tablename__ = 'TBL_CORDINADOR'  # Nombre de la tabla en la base de datos

    # Definición de las columnas que corresponden a los atributos de la clase
    coId = db.Column('COR_ID', db.Integer, primary_key=True, autoincrement=True)
    coTypeIdentification = db.Column('COR_TIPOIDENTIFICACION', db.Enum(TypeIdentification))
    coIdentification = db.Column('COR_IDENTIFICACION', db.String(100), nullable=False)
    coName = db.Column('COR_NOMBRES', db.String(100), nullable=False)
    coLastName = db.Column('COR_APELLIDOS', db.String(100), nullable=False)
    coEmail = db.Column('COR_CORREO', db.String(100), nullable=False)
    coState = db.Column('COR_ESTADO', db.String(50), default=True)

    # Constructor de la clase
    def __init__(self, coTypeIdentification=None, coIdentification=None, coName=None, coLastName=None, coEmail=None, coState=None):
        self.coTypeIdentification = coTypeIdentification
        self.coIdentification = coIdentification
        self.coName = coName
        self.coLastName = coLastName
        self.coEmail = coEmail
        self.coState = coState

    # Convierte una instancia de la clase Coordinator en un diccionario
    def to_dict(self):
        return {
            "coId": self.coId,
            "coTypeIdentification": self.coTypeIdentification.value,
            "coIdentification": self.coIdentification,
            "coName": self.coName,
            "coLastName": self.coLastName,
            "coEmail": self.coEmail,
            "coState": self.coState
        }
    
    # Convierte un diccionario en una instancia de la clase Coordinator
    @staticmethod
    def from_dict(data):
        return Coordinator(
            coTypeIdentification=TypeIdentification(data.get("coTypeIdentification")),
            coIdentification=data.get("coIdentification"),
            coName=data.get("coName"),
            coLastName=data.get("coLastName"),
            coEmail=data.get("coEmail"),
            coState=data.get("coState")
        )
