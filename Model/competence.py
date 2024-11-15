#Clase
#*COMPETENCIA
class Competence:
    def __init__(self, id=None, description=None, type=None, level=None, parent_id=None):
        self.id = id
        self.description = description
        self.type = type
        self.level = level
        self.parent_id = parent_id

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "type": self.type,
            "level": self.level,
            "parent_id": self.parent_id
        }

    @staticmethod
    def from_dict(data):
        return Competence(
            id=data.get("id"),
            description=data.get("description"),
            type=data.get("type"),
            level=data.get("level"),
            parent_id=data.get("parent_id")
        )
