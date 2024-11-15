#Clase
#*RESULTADO DE APRENDIZAJE
class LearningOutcome:
    def __init__(self, id=None, description=None, comp_id=None):
        self.id = id
        self.description = description
        self.comp_id = comp_id

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "comp_id": self.comp_id
        }

    @staticmethod
    def from_dict(data):
        return LearningOutcome(
            id=data.get("id"),
            description=data.get("description"),
            comp_id=data.get("comp_id")
        )
    