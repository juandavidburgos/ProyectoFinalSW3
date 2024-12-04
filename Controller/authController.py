"""# controller/authController.py
from flask import Blueprint, render_template, request, redirect, url_for

# Crear el blueprint para la autenticación
auth_blueprint = Blueprint('auth', __name__)

# Diccionario de usuarios y contraseñas con roles
users = {
    'coordinador1': {'password': 'clavecoordinador', 'role': 'coordinador'},
    'profesor1': {'password': 'claveprofesor', 'role': 'profesor'},
}

@auth_blueprint.route('/login', methods=['POST'])
def login():
    usuario = request.form['usuario']
    clave = request.form['clave']
    
    # Verificar si el usuario existe en el diccionario y si la contraseña es correcta
    if usuario in users and users[usuario]['password'] == clave:
        role = users[usuario]['role']
        
        # Redirigir según el rol
        if role == 'coordinador':
            return redirect(url_for('mainCoordinator'))
        elif role == 'profesor':
            return redirect(url_for('mainTeacher'))
    
    # Si el usuario o la contraseña no son correctos, mostrar error
    return render_template('index.html', error="Usuario o contraseña incorrectos")
"""