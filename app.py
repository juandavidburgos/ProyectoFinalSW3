from flask import Flask, render_template
from Model.connection import Connection
from Controller.teacherManagementController import teacher_blueprint
from Controller.mainController import main_bp
from Controller.subjectManagementController import subject_bp
from Controller.competenceManagementController import competence_bp
from Controller.learningOutcomeManagementController import learning_outcome_bp
from Controller.integrationController import integration_bp

# Inicialización de la aplicación Flask
app = Flask(__name__)  
# Clave secreta
app.secret_key = 'mysecretkey'  # Necesario para usar 'flash'

# Inicialización de la conexión MySQL ANTES de definir las rutas
db = Connection.init_database(app)  # Obtiene el objeto db

# Configuración e inicialización de JWT
jwt = Connection.config_JWT(app)  # Obtiene el objeto `jwt`

# Registro de los controladores
app.register_blueprint(main_bp)  # Controlador de la página principal
app.register_blueprint(subject_bp, url_prefix='/subject')  # Controlador de la gestión de asignaturas
app.register_blueprint(competence_bp, url_prefix='/competence')  # Controlador de la gestión de competencias
app.register_blueprint(learning_outcome_bp, url_prefix='/learning_outcome')  # Controlador de la gestión de RA
app.register_blueprint(teacher_blueprint, url_prefix='/teacher')  # Controlador de la gestión de docentes
app.register_blueprint(integration_bp, url_prefix='/asign')  # Controlador de la integración asignatura-competencia-docente

# Definir rutas adicionales si es necesario
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/coordinator')
def mainCoordinator():
    return render_template('coordinator/mainCoordinator.html')

@app.route('/teacher')
def mainTeacher():
    return render_template('mainTeacher.html')

if __name__ == '__main__':
    app.run(debug=True, port=3000)  # debug = true, actualiza cada vez que hacemos cambios en el servidor
