from Model.competence import Competence
from Model.connection import db
from Model.learningOutcome import LearningOutcome

class CompetenceService:
    @staticmethod
    def create_competence_with_rap(competence_data, rap_data):
        #*Crea una competencia (CP) y un RAP asociado.

        # Crear una nueva instancia de Competence con los datos proporcionados
        competence = Competence(comp_description=competence_data['comp_description'],
                                comp_type=competence_data['comp_type'],
                                comp_level=competence_data['comp_level'],  # Puede ser None si es de tipo programa
                                comp_subject_id=competence_data.get('comp_subject_id')  # Puede ser None para competencias de programa
                            )
        # Agregar la competencia a la sesión de la base de datos
        db.session.add(competence)
        # Confirmar y guardar los cambios en la base de datos para obtener el ID de la competencia
        db.session.commit()

        # Crear el RAP (LearningOutcome) asociado con la competencia recién creada
        loutcome = LearningOutcome(lout_description=rap_data['lout_description'],
                                    comp_id=competence.comp_id,  # Asociar el RAP con la competencia
                                    lout_subject_id=rap_data.get('lout_subject_id')   # El RAP puede o no tener un 'subject_id'
                                )
        # Agregar el RAP a la sesión de la base de datos
        db.session.add(loutcome)
        # Confirmar y guardar los cambios en la base de datos
        db.session.commit()

        # Retornar la competencia y el RAP creados
        return competence, loutcome
    
    @staticmethod
    def get_all_competences():
        #*Obtiene todas las competencias
        try:
            # Consultar todas las competencias utilizando outerjoin para incluir sus resultados
            competences = (
                db.session.query(Competence)  # Consulta sobre la tabla Competence
                .outerjoin(LearningOutcome, Competence.comp_id == LearningOutcome.comp_id)  # Realiza un outer join con LearningOutcome
                .options(db.contains_eager(Competence.programLearningOutcome)) # Indica que la relación se cargue de forma ansiosa
                .all()  # Ejecutar la consulta y obtener todos los resultados
            )                

            # Convertir los objetos de competencia a diccionarios y ver su contenido con un print
            competences_dict = [comp.to_dict() for comp in competences]
            print(competences_dict)  # Esto imprimirá el contenido de los diccionarios
            
            return competences_dict, None  # Devolver los resultados como lista de diccionarios
        except Exception as e:
            # En caso de error, devolver el mensaje de error
            return [], f"Error al obtener las competencias: {str(e)}"
        
    @staticmethod
    def get_all_competences_description():
        #*Obtiene todas las competencias y su descripcion e id
        try:
            # Consultar todas las asignaturas 
            competences = db.session.query(Competence.comp_id, Competence.comp_description).all()
            # Convertir los objetos de asignaturas a diccionarios y ver su contenido con un print
            competences_dict = [comp.to_dict() for comp in competences]
            print(competences_dict)  # Esto imprimirá el contenido de los diccionarios
            
            return competences_dict, None  # Devolver los resultados como lista de diccionarios
        except Exception as e:
            # En caso de error, devolver el mensaje de error
            return [], f"Error al obtener las competencias: {str(e)}"
        
    

    """"
    @staticmethod
    def create_competence(data):
        #Crea una nueva competencia.
        # Validaciones de los datos comunes
        if not data.get('comp_description') or not data.get('comp_type'):
            return None, "La descripción y el tipo de la competencia son requeridos"

        # Verificar que el tipo de competencia sea válido
        valid_types = ['Programa', 'Asignatura']
        if data['comp_type'] not in valid_types:
            return None, f"El tipo de competencia debe ser uno de los siguientes: {', '.join(valid_types)}"

         # Validar para competencias de tipo Programa
        if data['comp_type'] == 'Programa':
            data['program_comp_id'] = None

        # Validar el nivel solo para competencias de programa
        if data['comp_type'] == 'Programa':
            if not data.get('comp_level'):
                return None, "El nivel es requerido para competencias de programa"
            valid_levels = ['Basico', 'Intermedio', 'Avanzado']
            if data['comp_level'] not in valid_levels:
                return None, f"El nivel debe ser uno de los siguientes: {', '.join(valid_levels)}"
        else:
            # Si es una competencia de asignatura, establecer comp_level como None
            data['comp_level'] = None

            # Verificar que la competencia de asignatura tenga program_comp_id
            if not data.get('program_comp_id'):
                return None, "La competencia de asignatura debe estar asociada a una competencia de programa"

            # Opcional: verificar si program_comp_id corresponde a una competencia válida en la base de datos
            program_comp = Competence.query.filter_by(comp_id=data['program_comp_id'], comp_type='Programa').first()
            if not program_comp:
                return None, "El ID de la competencia de programa asociado no existe o no es válido"

        # Crear la competencia
        try:
            new_competence = Competence(
                comp_description=data['comp_description'],
                comp_type=data['comp_type'],
                comp_level=data['comp_level'],  # Será None para competencias de asignatura
                program_comp_id=data['program_comp_id']  # Puede ser None para competencias de programa
            )
            db.session.add(new_competence)
            db.session.commit()
            return new_competence, None  # Retorna la nueva competencia y sin error
        except Exception as e:
            db.session.rollback()  # En caso de error, hacer rollback
            return None, f"Error en la base de datos: {str(e)}"

    @staticmethod
    def update_competence(comp_id, data):
        #Actualiza una competencia existente.
        try:
            competence = Competence.query.get(comp_id)
            if not competence:
                return None, "Competencia no encontrada"

            # Actualiza los campos de la competencia
            competence.comp_description = data.get('comp_description', competence.comp_description)
            competence.comp_type = data.get('comp_type', competence.comp_type)
            competence.comp_level = data.get('comp_level', competence.comp_level)
            competence.program_comp_id = data.get('program_comp_id', competence.program_comp_id)

            db.session.commit()
            return competence, None
        except ValueError:
            db.session.rollback()
            return None, ValueError("Datos proporcionados NO validos.")
        except Exception as e:
            db.session.rollback()
            return None, f"Error al actualizar la competencia: {str(e)}"
    """
    """"
    @staticmethod
    def get_competence_by_id(comp_id):
        # Validaciones de los datos
        if not comp_id:
            return None, "El ID es requerido"

        competence = Competence.query.filter_by(comp_id=comp_id).first()
        if not competence:
            return None, f"No se encontro una asignatura con ese ID {comp_id}."
        return competence, None
    
    @staticmethod
    def get_competences_by_type(comp_type):
        #Obtiene todas las competencias por tipo.
        try:
            competences = Competence.query.filter_by(comp_type=comp_type).all()
            return [competence.to_dict() for competence in competences]
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def get_linked_competences(program_comp_id):
        #Obtiene competencias vinculadas a una competencia padre.
        try:
            linked_competences = Competence.query.filter_by(program_comp_id=program_comp_id).all()
            return [competence.to_dict() for competence in linked_competences]
        except Exception as e:
            return {"error": str(e)}"""

