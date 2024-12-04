from connection import db  # Importa db desde connection.py

class ResultaApRubrica(db.Model):
    __tablename__ = 'RESULTAAP_RUBRICA'  #Nombre de la tabla

    rap_id = db.Column('RAP_ID', db.Integer, primary_key=True,nullable=False)# ID del resultado de aplicación
    rub_id = db.Column('IDRUBRICA', db.Integer, primary_key=True,nullable=False)# ID de la rubrica


    def __init__(self, rap_id, rub_id):
        self.rap_id = rap_id,
        self.rub_id = rub_id
       
    def to_dict(self):
        return {
            "rap_id": self.rap_id,
            "rub_id": self.rub_id
        }

    @staticmethod
    def from_dict(data):
        return ResultaApRubrica(
            rap_id=data.get("rap_id"),
            rub_id=data.get("rub_id")
        )

    