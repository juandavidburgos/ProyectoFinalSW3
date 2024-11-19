#Aplicacion principal
from flask import Flask
from Model.connection import Connection
from Controller.teacherManagementController  import *
from Controller.mainController import main_bp
from Controller.subjectManagementController import subject_bp
from Controller.competenceManagementController import competence_bp



# Inicializacion de la aplicacion Flask
app = Flask(__name__)  
#Clave secreta
app.secret_key = 'mysecretkey'  # Necesario para usar 'flash'
# Inicializacion de la conexión MySQL ANTES de definir las rutas
db = Connection.init_database(app) # Obtiene el objeto `db`

# Configuración e inicialización de JWT
jwt = Connection.config_JWT(app)  # Obtiene el objeto `jwt`s

#Registro de los controladores
app.register_blueprint(main_bp) #Controlador de la pagina principal

#Controlador de la gestion de asignaturas
app.register_blueprint(subject_bp, url_prefix='/subject')
app.register_blueprint(competence_bp,url_prefix='/competence')

#Controlador de la gestion de docentes
app.register_blueprint(teacher_blueprint, url_prefix='/teacher')

#Comprobar que el archivo que se esta ejecutando es el principal
if __name__ == '__main__':
    app.run(debug=True, port= 3000) #debug = true, actualiza cada vez que hacemos cambios en el servidor
                        # Se podria poner otro parámetro: port, para definir el puerto, por defecto Flask se ejecuta en el puerto 5000
