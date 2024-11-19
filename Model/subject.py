#Clase
#*ASIGNATURA
from .connection import db  # Importa el db correctamente desde connection.py

class Subject(db.Model):  
    __tablename__ = 'TBL_ASIGNATURA'  # Nombre de la tabla en la base de datos

    # Definición de los atributos/columnas de la tabla
    # ! Se debe poner como primer parametro exactamente el nombre de la columna de la abse de datos
    # *El segundo parametro corresponde al tipo de dato
    id = db.Column('ASIG_ID', db.Integer, primary_key=True, autoincrement=True) 
    name = db.Column('ASIG_NOMBRE', db.String(100))
    credits = db.Column('ASIG_CREDITOS', db.Integer)
    goals = db.Column('ASIG_OBJETIVOS', db.String(500))
    semester = db.Column('ASIG_SEMESTRE', db.Integer)

    # Constructor de la clase
    def __init__(self, name, credits, goals, semester):
        self.name = name
        self.credits = credits
        self.goals = goals
        self.semester = semester

    # Método para convertir a diccionario (útil para respuestas JSON)
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "credits": self.credits,
            "goals": self.goals,
            "semester": self.semester
        }

    # Método estático para crear un objeto de clase a partir de un diccionario
    @staticmethod
    def from_dict(data):
        return Subject(
            id=data.get("id"),
            name=data.get("name"),
            credits=data.get("credits"),
            goals=data.get("goals"),
            semester=data.get("semester")
        )

    # Método para mostrar la representación de la clase
    #def __repr__(self):
        #return f"<Subject {self.name}>"
