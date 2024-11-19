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

