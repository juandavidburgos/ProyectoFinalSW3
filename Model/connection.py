#Clase
#*CONEXIÓN BASE DE DATOS
from flask_mysqldb import MySQL
#*Conexion a base de datos
class Connection:
    @staticmethod #Se utiliza porque la funcion no necesita usar ninguna instancia de la clase
    def init_database(app):
        #Configuración de la abse de datos
        app.config['MYSQL_HOST'] = 'localhost' #Servidor local
        app.config['MYSQL_USER'] = 'root' #Por defecto lo da MySQL Workbench
        app.config['MYSQL_PASSWORD'] = '1234' #Establecida al momentod e instalar MySQL Workbench
        app.config['MYSQL_DB'] = 'bdacademic_management' #Nombre base de datos

        #Retornar la conexión
        return MySQL(app)
    
