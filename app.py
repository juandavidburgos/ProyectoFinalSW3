#Aplicacion principal
from flask import Flask, render_template, request, redirect, url_for
from Controller.teacherManagementController  import *
from Model.connection import Connection


# Inicializacion de la aplicacion Flask
app = Flask(__name__)  
#Clave secreta
app.secret_key = 'mysecretkey'  # Necesario para usar 'flash'
# Inicializacion de la conexión MySQL ANTES de definir las rutas
db = Connection.init_database(app) # Obtiene el objeto `db`

# Configuración e inicialización de JWT
jwt = Connection.config_JWT(app)  # Obtiene el objeto `jwt`s


#Comprobar que el archivo que se esta ejecutando es el principal
if __name__ == '__main__':
    app.run(debug=True, port= 3000) #debug = true, actualiza cada vez que hacemos cambios en el servidor
                        # Se podria poner otro parámetro: port, para definir el puerto, por defecto Flask se ejecuta en el puerto 5000
>>>>>>> 474ab0bf0988b6d99df0e17a5753b099aa1c3e51
