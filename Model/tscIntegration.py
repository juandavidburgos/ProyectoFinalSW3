#Clase
#*ASIGNATURA-COMPETENCIA-DOCENTE
from .connection import db  # Importa db desde connection.py

class IntegrationTSC(db.Model):
    __tablename__ = 'ASIG_COMP_DOCENTE'  # Nombre de la tabla

    # Claves primarias compuestas (todas son foráneas)
    subj_id = db.Column('ASIG_ID', db.Integer, db.ForeignKey('TBL_ASIGNATURA.ASIG_ID'), primary_key=True, nullable=False)  
    teach_id = db.Column('DOC_ID', db.Integer, db.ForeignKey('TBL_DOCENTE.DOC_ID'), primary_key=True, nullable=False)  
    comp_id = db.Column('COMP_ID', db.Integer, db.ForeignKey('TBL_COMPETENCIA.COMP_ID'), primary_key=True, nullable=False)

    time = db.Column('PERIODO', db.String(250), nullable=False)    

    def __init__(self, subj_id,comp_id,teach_id, time):
        self.subj_id = subj_id
        self.comp_id = comp_id
        self.teach_id=teach_id
        self.time=time 
        

    def to_dict(self):
        return {
            "subj_id": self.subj_id,
            "comp_id": self.comp_id,
            "teach_id": self.teach_id,
            "time":self.time
        }

    @staticmethod
    def from_dict(data):
        return IntegrationTSC(
            subj_id=data.get("subj_id"),
            comp_id=data.get("comp_id"),
            teach_id=data.get("teach_id"),
            time=data.get("time")
            
        )