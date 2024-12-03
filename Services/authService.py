from Model.teacher import Teacher
from Model.coordinator import Coordinator
from Model.evaluator import Evaluator

class AuthService:

    @staticmethod
    def login_user(data):
        print(f"Datos recibidos para login: {data}")
        # Validar datos requeridos
        if not data.get('email') or not data.get('password'):
            return None, "Correo y contraseña son requeridos"

        # Buscar en las tablas: Teacher, Coordinator, Evaluator
        user = (
            Teacher.query.filter_by(teEmail=data['email'], teIdentification=data['password']).first() or
            Coordinator.query.filter_by(coEmail=data['email'], coIdentification=data['password']).first() or
            Evaluator.query.filter_by(evEmail=data['email'], evIdentification=data['password']).first()
        )

        if not user:
            return None, "Correo o contraseña incorrectos"

        # Identificar el rol del usuario
        if isinstance(user, Teacher):
            role = "Docente"
        elif isinstance(user, Coordinator):
            role = "Coordinador"
        elif isinstance(user, Evaluator):
            role = "Evaluador"
        else:
            role = "Desconocido"

        return {"user": user, "role": role}, None