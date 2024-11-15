#Clase
#*RESULTADO DE APRENDIZAJE
class learningOutcome:
    def __init__(self, id=None, descripcion=None, competencia_id=None):
        self.id = id
        self.descripcion = descripcion
        self.competencia_id = competencia_id

    def to_dict(self):
        return {
            "id": self.id,
            "descripcion": self.descripcion,
            "competencia_id": self.competencia_id
        }

    @staticmethod
    def from_dict(data):
        return learningOutcome(
            id=data.get("id"),
            descripcion=data.get("descripcion"),
            competencia_id=data.get("competencia_id")
        )
