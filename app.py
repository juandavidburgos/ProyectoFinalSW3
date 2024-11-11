#Aplicacion principal
from flask import Flask, render_template, request, redirect, url_for
from Controller.teacherManagementController  import *
from Model.connection import Connection


# Inicializacion de la aplicacion Flask
app = Flask(__name__)  
#Clave secreta
app.secret_key = 'mysecretkey'  # Necesario para usar 'flash'
# Inicializacion de la conexión MySQL ANTES de definir las rutas
mysql = Connection.init_database(app)

#TODO : Rutas y vistas HTML

#Comprobar que el archivo que se esta ejecutando es el principal
if __name__ == '__main__':
    app.run(debug=True, port= 3000) #debug = true, actualiza cada vez que hacemos cambios en el servidor
                        # Se podria poner otro parámetro: port, para definir el puerto, por defecto Flask se ejecuta en el puerto 5000
