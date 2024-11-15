#Clase
#*ASIGNATURA
class subject:
    def __init__(self, id=None, nombre=None, creditos=None, objetivos=None, semestre=None):
        self.id = id
        self.nombre = nombre
        self.creditos = creditos
        self.objetivos = objetivos
        self.semestre = semestre

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "creditos": self.creditos,
            "objetivos": self.objetivos,
            "semestre": self.semestre
        }

    @staticmethod
    def from_dict(data):
        return subject(
            id=data.get("id"),
            nombre=data.get("nombre"),
            creditos=data.get("creditos"),
            objetivos=data.get("objetivos"),
            semestre=data.get("semestre")
        )