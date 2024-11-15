#Clase DOCENTE
from enum import Enum
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class TipoDocente(Enum):
    PLANTA = 'Planta'
    TIEMPOCOMPLETO = 'Tiempo completo'
    CATEDRA = 'Catedra'

class TipoIdentificacion(Enum):
    REGISTROCIVIL = 'Registro Civil'
    TARJETAIDENTIDAD = 'Tarjeta de identidad'
    CEDULA = 'Cedula'
    PASAPORTE = 'Pasaporte'
    CEDULAEXTRANJERIA = 'cedula extranjeria'

    class Teacher(db.Model):
        docId = db.Column(db.Integer, primary_key=True, nullable=False)
        docTipoIdentificacion = db.Column(db.Enum(TipoIdentificacion), nullable=False)
        docIdentificacion = db.Column(db.String(50), nullable=False)
        docTipoDocente = db.Column(db.Enum(TipoDocente), nullable=False)
        docNombres = db.Column(db.String(100), nullable=False)
        docApellidos = db.Column(db.String(100), nullable=False)
        docUltimoTitulo = db.Column(db.String(100), nullable=False)
        docCorreo = db.Column(db.String(100), nullable=False)

#convierte una instancia de la clase Teacher en un diccionario
#Esto es util para convertir el objeto en un JSON
        def agregarDiccionario(self):
            return {
                'docId': self.docId,
                'docTipoIdentificacion': self.docTipoIdentificacion.value,
                'docIdentificacion': self.docIdentificacion,
                'docTipoDocente': self.docTipoDocente.value,
                'docNombres': self.docNombres,
                'docApellidos': self.docApellidos,
                'docUltimoTitulo': self.docUltimoTitulo,
                'docCorreo': self.docCorreo
            }
        
"""class Teacher:
    def __init__(self, docId =None, docTipoIdentificacion=None, docIdentificacion=None, docTipoDocente=None, docNombres=None,docApellidos=None, docUltimoTitulo=None, docCorreo=None):
        self.docId = docId
        self.docTipoIdentificacion = docTipoIdentificacion
        self.docIdentificacion = docIdentificacion
        self.docTipoDocente = docTipoDocente
        self.docNombres = docNombres
        self.docApellidos = docApellidos 
        self.docUltimoTitulo = docUltimoTitulo 
        self.docCorreo = docCorreo"""

        
        