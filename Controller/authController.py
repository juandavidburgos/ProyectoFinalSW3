from flask import Blueprint, request, redirect, url_for, flash, render_template
from Services.authService import AuthService

# Blueprint para el controlador de autenticación
auth_blueprint = Blueprint('auth', __name__)

# Ruta para iniciar sesión
@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Obtener los datos del formulario
        data = request.form.to_dict()
        print(f"Datos recibidos para login: {data}")

        # Llamar al servicio de login
        auth_data, error = AuthService.login_user(data)
        if error:
            flash(error, 'error')
            return redirect(url_for('auth.login'))

        user = auth_data['user']
        role = auth_data['role']
        flash(f"Bienvenido, {user.teName if role == 'Docente' else user.coName if role == 'Coordinador' else user.evName} ({role})", 'success')

        # Redirigir al dashboard o página según el rol
        return redirect(url_for('dashboard.index'))

    return render_template('auth/login.html')
