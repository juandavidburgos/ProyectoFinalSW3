import jwt
import datetime
from flask import current_app
from flask_jwt_extended import create_access_token
from Model.teacher import Teacher
from Model.coordinator import Coordinator
from Model.evaluator import Evaluator
import time

class AuthService:
    # Diccionario para almacenar intentos fallidos y tiempos de bloqueo
    failed_attempts = {}

    @staticmethod
    def login_user(data):
        email = data.get('email')
        print(f"Datos recibidos para login: {data}")

        # Validar datos requeridos
        if not email or not data.get('password'):
            return None, "Correo y contraseña son requeridos"

        # Validar si el usuario está bloqueado
        if email in AuthService.failed_attempts:
            block_info = AuthService.failed_attempts[email]
            if block_info['locked_until'] and time.time() < block_info['locked_until']:
                remaining_time = int(block_info['locked_until'] - time.time())
                return None, f"Cuenta bloqueada. Inténtelo nuevamente en {remaining_time} segundos."

        # Buscar en las tablas: Teacher, Coordinator, Evaluator
        user = (
            Teacher.query.filter_by(teEmail=email, teIdentification=data['password']).first() or
            Coordinator.query.filter_by(coEmail=email, coIdentification=data['password']).first() or
            Evaluator.query.filter_by(evaEmail=email, evaIdentification=data['password']).first()
        )

        if not user:
            # Registrar intento fallido
            if email not in AuthService.failed_attempts:
                AuthService.failed_attempts[email] = {"attempts": 0, "locked_until": None}
            
            AuthService.failed_attempts[email]['attempts'] += 1

            if AuthService.failed_attempts[email]['attempts'] >= 3:
                AuthService.failed_attempts[email]['locked_until'] = time.time() + 30  # 30 segundos de bloqueo
                return None, "Demasiados intentos fallidos. Inténtelo nuevamente en 30 segundos."

            remaining_attempts = 3 - AuthService.failed_attempts[email]['attempts']
            return None, f"Correo o contraseña incorrectos. Te quedan {remaining_attempts} intentos."

        # Si el login es exitoso, reiniciar intentos fallidos
        if email in AuthService.failed_attempts:
            del AuthService.failed_attempts[email]

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
            payload = {
                "user_id": user_id,
                "role": role,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=12)  # Token válido por 12 horas
            }
            token = jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm="HS256")
        except Exception as e:
            return None, f"Error al generar el token: {str(e)}"

        return {"token": token, "role": role}, None

