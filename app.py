#Aplicacion principal
from flask import Flask
from Model.connection import Connection
from Controller.teacherManagementController  import *
from Controller.mainController import main_bp
from Controller.subjectManagementController import subject_bp




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
app.register_blueprint(subject_bp, url_prefix='/subject')

#Comprobar que el archivo que se esta ejecutando es el principal
if __name__ == '__main__':
    app.run(debug=True, port= 3000) #debug = true, actualiza cada vez que hacemos cambios en el servidor
                        # Se podria poner otro parámetro: port, para definir el puerto, por defecto Flask se ejecuta en el puerto 5000
