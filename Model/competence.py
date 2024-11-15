#Clase
#*COMPETENCIA
class competence:
    def __init__(self, id=None, descripcion=None, tipo=None, nivel=None, tbl_comp_id=None):
        self.id = id
        self.descripcion = descripcion
        self.tipo = tipo
        self.nivel = nivel
        self.tbl_comp_id = tbl_comp_id  # Referencia a la competencia de programa (si es una competencia de asignatura)

    def to_dict(self):
        return {
            "id": self.id,
            "descripcion": self.descripcion,
            "tipo": self.tipo,
            "nivel": self.nivel,
            "tbl_comp_id": self.tbl_comp_id  # Incluimos la referencia en el diccionario
        }

    @staticmethod
    def from_dict(data):
        return competence(
            id=data.get("id"),
            descripcion=data.get("descripcion"),
            tipo=data.get("tipo"),
            nivel=data.get("nivel"),
            tbl_comp_id=data.get("tbl_comp_id")
        )