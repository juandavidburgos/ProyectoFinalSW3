#Clase
#*CONEXIÓN BASE DE DATOS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db=SQLAlchemy() #Definir objeto db para usarlo en otros archivos
class Connection:
    @staticmethod #Se utiliza porque la funcion no necesita usar ninguna instancia de la clase
    def init_database(app):
        # Configuración de la base de datos MySQL
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/bdacademic_management' #! CAMBIAR SEGUN SU USUARIO Y CONTRASEÑA
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desactiva las notificaciones de cambios en SQLAlchemy

        # Inicialización de extensiones
        db.init_app(app) # Objeto para manejar la base de datos
        return db
    
    @staticmethod
    def config_JWT(app):
        # Configuración de JWT
        app.config['JWT_SECRET_KEY'] = 'super_secret_key'  # Cambia esta clave a una más segura en producción
        app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600  # Tokens de acceso expiran en 1 hora
        app.config['JWT_TOKEN_LOCATION'] = ['cookies']  # Usar cookies para almacenar tokens
        app.config['JWT_COOKIE_SECURE'] = False  # Cambiar a True en producción para usar HTTPS
        app.config['JWT_ACCESS_COOKIE_PATH'] = '/'  # Cookie accesible para toda la app
        app.config['JWT_REFRESH_COOKIE_PATH'] = '/token/refresh'  # Ruta para la cookie de refresh
        app.config['JWT_COOKIE_CSRF_PROTECT'] = True  # Protección contra CSRF

        jwt = JWTManager(app)  # Objeto para manejar JWT
        return jwt

