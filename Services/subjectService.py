#Servicio para asignatura
from Model.subject import Subject
from Model.connection import db

class SubjectService:
    @staticmethod
    def create_subject(data):
        # Validaciones de los datos
        if not data.get('name') or not data.get('credits') or not data.get('semester'):
            return None, "El nombre, creditos y semestre es requerido"

        try:
            data['credits'] = int(data['credits'])
            if data['credits'] <= 0:
                return None, "Los creditos deben ser positivos"
        except ValueError:
            return None, "Los creditos deben ser positivos y enteros"

        # Crear la nueva asignatura
        new_subject = Subject(
            #No se pone el id porque se genera automaticamente cuando se crea una nueva instancia
            name=data['name'],
            credits=data['credits'],
            goals=data.get('goals'),
            semester=data['semester']
        )

        try:
            db.session.add(new_subject)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return None, f"Error en la base de datos: {str(e)}"

        return new_subject, None
    
    @staticmethod
    def get_all_subjects():
        #*Obtiene todas las asignaturas
        try:
            # Consultar todas las asignaturas 
            subjects = db.session.query(Subject.id, Subject.name).all()
            # Convertir los objetos de asignaturas a diccionarios y ver su contenido con un print
            subjects_dict = [sub.to_dict() for sub in subjects]
            print(subjects_dict)  # Esto imprimirá el contenido de los diccionarios
            
            return subjects_dict, None  # Devolver los resultados como lista de diccionarios
        except Exception as e:
            # En caso de error, devolver el mensaje de error
            return [], f"Error al obtener las asignaturas: {str(e)}"

    @staticmethod
    def get_subject_by_name(name):
        # Validaciones de los datos
        if not name:
            return None, "El nombre es requerido"

        subject = Subject.query.filter_by(name=name).first()
        if not subject:
            return None, f"No se encontro una asignatura con el nombre {name}."
        return subject, None

    @staticmethod
    def update_subject(name, data):
        subject = Subject.query.filter_by(name=name).first()
        if not subject:
            return None, f"No se encontro una asignatura con el nombre: {name}"

        try:
            subject.name = data.get('name', subject.name)#Actualiza el campo subject.name con 'name' que es el que llega
            subject.credits = int(data.get('credits', subject.credits)) 
            subject.goals = data.get('goals', subject.goals)
            subject.semester = int(data.get('semester', subject.semester))

            db.session.commit()
            return  subject,None
        except ValueError:
            db.session.rollback()
            return None, ValueError("Datos proporcionados NO validos.")
        except Exception as e:
            db.session.rollback()
            return None, f"Error inesperado: {str(e)}"

