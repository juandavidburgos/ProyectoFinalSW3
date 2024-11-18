#Clase
#*RUBRICA
class rubric:
    #Constructor (__init__): Cada clase tiene un constructor que define los atributos de la entidad.
    def __init__(self, id=None, nombre=None, nota=None, criterio_desc=None, nivel=None, evaluador_id=None):
        self.id = id
        self.nombre = nombre
        self.nota = nota
        self.criterio_desc = criterio_desc
        self.nivel = nivel
        self.evaluador_id = evaluador_id

    #Método to_dict: Convierte los atributos de la instancia en un diccionario, útil para devolver datos en formato JSON.
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "nota": self.nota,
            "criterio_desc": self.criterio_desc,
            "nivel": self.nivel,
            "evaluador_id": self.evaluador_id
        }

    @staticmethod
    #Método from_dict: Método estático para crear una instancia de la clase a partir de un diccionario de datos (por ejemplo, cuando se recibe una solicitud JSON en la API).
    def from_dict(data):
        return rubric(
            id=data.get("id"),
            nombre=data.get("nombre"),
            nota=data.get("nota"),
            criterio_desc=data.get("criterio_desc"),
            nivel=data.get("nivel"),
            evaluador_id=data.get("evaluador_id")
        )
