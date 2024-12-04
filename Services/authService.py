import jwt
import datetime
from flask import current_app
from flask_jwt_extended import create_access_token
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
            user_id = user.teId
        elif isinstance(user, Coordinator):
            role = "Coordinador"
            user_id = user.coId
        elif isinstance(user, Evaluator):
            role = "Evaluador"
            user_id = user.evId
        else:
            return None, "Rol no reconocido"

        # Crear token JWT
        try:
            #token = create_access_token(identity={"user_id": user_id, "role": role})
            payload = {
                "user_id": user_id,
                "role": role,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=12)  # Token válido por 12 horas
            }
            token = jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm="HS256")
        except Exception as e:
            return None, f"Error al generar el token: {str(e)}"

        return {"token": token, "role": role}, None
