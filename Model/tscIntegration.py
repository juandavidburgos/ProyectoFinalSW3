#Clase
#*ASIGNATURA-COMPETENCIA-DOCENTE
from .connection import db  # Importa db desde connection.py

class IntegrationTSC(db.Model):
    __tablename__ = 'ASIG_COMP_DOCENTE'  # Nombre de la tabla

    # Claves primarias compuestas con claves foráneas
    subj_id = db.Column('ASIG_ID', db.Integer, db.ForeignKey('TBL_ASIGNATURA.ASIG_ID'), primary_key=True)  
    teach_id = db.Column('DOC_ID', db.Integer, db.ForeignKey('TBL_DOCENTE.DOC_ID'), primary_key=True)  
    comp_subject_id = db.Column('COMP_ID', db.Integer, db.ForeignKey('TBL_COMPETENCIA.COMP_IDASIGNATURA'), primary_key=True)
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