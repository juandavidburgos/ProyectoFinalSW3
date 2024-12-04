from flask import Blueprint, render_template, request, redirect, url_for, flash, session

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/login', methods=['POST'])
def login():
    usuario = request.form.get('usuario')
    clave = request.form.get('clave')

    # Validar credenciales (puedes usar un servicio o modelo para esto)
    if usuario == 'coordinador' and clave == 'password123':  # Ejemplo simple
        session['user'] = usuario
        return redirect(url_for('coordinator.main_dashboard'))
    
    flash("Usuario o contraseña incorrectos", 'error')
    return render_template('index.html', error="Credenciales inválidas")
