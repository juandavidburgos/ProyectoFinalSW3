#Clase
#*ASIGNATURA
from connection import db  # Importa el db correctamente desde connection.py

class Subject(db.Model):  
    __tablename__ = 'TBL_ASIGNATURA'  # Nombre de la tabla en la base de datos

    # Definición de los atributos/columnas de la tabla
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    credits = db.Column(db.Integer)
    goals = db.Column(db.String(500))
    semester = db.Column(db.Integer)

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
            name=data.get("name"),
            credits=data.get("credits"),
            goals=data.get("goals"),
            semester=data.get("semester")
        )

    # Método para mostrar la representación de la clase
    #def __repr__(self):
        #return f"<Subject {self.name}>"
