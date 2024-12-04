#Clase
#*COORDINADOR
from .connection import db  # Importa el db desde connection.py

class Coordinator(db.Model):
    __tablename__ = 'TBL_CORDINADOR'  # Nombre de la tabla en la base de datos

    # Definición de las columnas
    coId = db.Column('COR_ID', db.Integer, primary_key=True, autoincrement=True)  # Identificador único
    coTypeIdentification = db.Column('COR_TIPOIDENTIFICACION', db.String(100), nullable=False)  # Tipo de identificación
    coIdentification = db.Column('COR_IDENTIFICACION', db.String(100), nullable=False)  # Número de identificación
    coName = db.Column('COR_NOMBRES', db.String(100), nullable=False)  # Nombre del coordinador
    coLastName = db.Column('COR_APELLIDOS', db.String(100), nullable=False)  # Apellido del coordinador
    coEmail = db.Column('COR_CORREO', db.String(100), nullable=False)  # Correo del coordinador

    # Constructor
    def _init_(self, coTypeIdentification=None, coIdentification=None, coName=None, coLastName=None, coEmail=None):
        self.coTypeIdentification = coTypeIdentification
        self.coIdentification = coIdentification
        self.coName = coName
        self.coLastName = coLastName
        self.coEmail = coEmail

    # Convierte una instancia a un diccionario
    def to_dict(self):
        return {
            "coId": self.coId,
            "coTypeIdentification": self.coTypeIdentification,
            "coIdentification": self.coIdentification,
            "coName": self.coName,
            "coLastName": self.coLastName,
            "coEmail": self.coEmail
        }

    # Convierte un diccionario a una instancia
    @staticmethod
    def from_dict(data):
        return Coordinator(
            coTypeIdentification=data.get("coTypeIdentification"),
            coIdentification=data.get("coIdentification"),
            coName=data.get("coName"),
            coLastName=data.get("coLastName"),
            coEmail=data.get("coEmail")
        )