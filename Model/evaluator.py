#Clase
#*EVALUADOR

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Evaluator(db.Model):
    __tablename__ = "TBL_EVALUADOR"

    eva_id = db.Column("EVA_ID", db.Integer, primary_key=True, autoincrement=True)
    eva_tipoidentificacion = db.Column("EVA_TIPOIDENTIFICACION", db.String(50), nullable=False)
    eva_nombre = db.Column("EVA_NOMBRE", db.String(100), nullable=False)
    eva_apellido = db.Column("EVA_APELLIDO", db.String(100), nullable=False)
    eva_correo = db.Column("EVA_CORREO", db.String(100), nullable=False, unique=True)
    eva_identificacion = db.Column("EVA_IDENTIFICACION", db.String(100), nullable=False, unique=True)

    def __init__(self, tipoidentificacion, nombre, apellido, correo, identificacion):
        self.eva_tipoidentificacion = tipoidentificacion
        self.eva_nombre = nombre
        self.eva_apellido = apellido
        self.eva_correo = correo
        self.eva_identificacion = identificacion

    def to_dict(self):
        return {
            "eva_id": self.eva_id,
            "eva_tipoidentificacion": self.eva_tipoidentificacion,
            "eva_nombre": self.eva_nombre,
            "eva_apellido": self.eva_apellido,
            "eva_correo": self.eva_correo,
            "eva_identificacion": self.eva_identificacion,
        }
