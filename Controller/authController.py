from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_jwt_extended import create_access_token
from Services.authService import AuthService

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/login', methods=['POST'])
def login():
    # Obtener los datos del formulario
    email = request.form.get('usuario')
    password = request.form.get('clave')

    # Pasar los datos al servicio de autenticación
    data = {'email': email, 'password': password}
    response, error = AuthService.login_user(data)

    if error:
        # Si hubo un error, renderizar el formulario de inicio de sesión con un mensaje de error
        return render_template('index.html', error=error)

    # Si no hay error, obtenemos el token y el rol
    token = response['token']
    role = response['role']

    # Redirigir según el rol del usuario
    if role == "Docente":
        return redirect(url_for('teacher.create_teacher', token=token))  # Redirigir al dashboard de Docente
    elif role == "Coordinador":
        return redirect(url_for('coordinator_dashboard', token=token))  # Redirigir al dashboard de Coordinador
    elif role == "Evaluador":
        return redirect(url_for('evaluator_dashboard', token=token))  # Redirigir al dashboard de Evaluador
    else:
        # Si el rol no se reconoce, redirigir al login
        flash('Rol no reconocido')
        return redirect(url_for('auth.login'))