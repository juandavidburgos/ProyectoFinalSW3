#Servicio Docente
from Model.teacher import Teacher
from Model.connection import db

class TeacherService:

    @staticmethod
    def create_teacher(data):
        # Validacion de los datos requeridos
        if not data.get('teTypeIdentification') or not data.get('teIdentification') \
            or not data.get('teTypeTeacher') or not data.get('teName')\
            or not data.get('teLastName') or not data.get('teLastTitle')\
            or not data.get('teEmail'):

            return None, "Todos los campos son requeridos"
        
        """ #Validacion del tipo de identificacion          
        if data['teTypeIdentification'] not in ['Registro Civil','Tarjeta de identidad','Cédula''Pasaporte','Cédula extranjeria']:
            return None, "El tipo de identificacion es invalido"
        
        #Validacion del tipo de docente
        if data['teTypeTeacher'] not in ['Planta', 'Tiempo completo', 'Catedra']:
            return None, "El tipo de docente es invalido"""

        # Crear un nuevo docente
        new_teacher = Teacher(
            teTypeIdentification=data['teTypeIdentification'],
            teIdentification=data['teIdentification'],
            teTypeTeacher=data['teTypeTeacher'],
            teName=data['teName'],
            teLastName=data['teLastName'],
            teLastTitle=data['teLastTitle'],
            teEmail=data['teEmail']
        )
        
        try:
            db.session.add(new_teacher)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return None, f"Ha ocurrido un error en la base de datos: {str(e)}"

        return new_teacher, None

