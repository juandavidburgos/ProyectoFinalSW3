from Model.competence import Competence
from Model.learningOutcome import LearningOutcome
from Model.tscIntegration import IntegrationTSC
from Model.connection import db
from Model.subject import Subject
from Model.teacher import Teacher


class IntegrationService:
    @staticmethod
    def create_subject_assign(comp_id, teacher_id, subject_id,time):
        try:
            # Crear una nueva instancia de IntegrationTSC con los datos proporcionados
            integration = IntegrationTSC(subj_id=subject_id, comp_id=comp_id,teach_id=teacher_id,time=time)
            
            # Agregar la relación a la sesión y hacer commit
            db.session.add(integration)
            db.session.commit()

            return "Asignación realizada exitosamente", None
        except Exception as e:
            db.session.rollback()  # Si hay error, hacer rollback
            return None, f"Error al realizar la asignación: {str(e)}"
        
    @staticmethod    
    def get_next_subject_id():
        #*Obtiene el siguiente ID disponible para comp_subject_id para no tener conflictos
        
        max_subject_id = db.session.query(db.func.max(Competence.comp_subject_id)).scalar()
        return (max_subject_id or 0) + 1  # Si no hay registros, comienza desde 1
    """"
    @staticmethod    
    def get_next_lout_id():
        #*Obtiene el siguiente ID disponible para lout_subject_id para no tener conflictos
        
        max_subject_id = db.session.query(db.func.max(LearningOutcome.lout_subject_id)).scalar()
        return (max_subject_id or 0) + 1  # Si no hay registros, comienza desde 1
    """


    @staticmethod
    def create_subject_competence(subcompetence_data,raa_data):
        try:
            # Obtener el siguiente ID disponible para comp_subject_id
            next_subject_id = IntegrationService.get_next_subject_id()
            #next_lout_id = IntegrationService.get_next_lout_id()

            subject_competence = Competence(comp_description=subcompetence_data['comp_description'],
                                comp_type=subcompetence_data['comp_type'],
                                comp_level=None,  # Puede ser None si es de tipo programa
                                comp_subject_id=next_subject_id 
                                )
            
            print("SUBJECT COMPETENCE CREADA------------------------------------------------------------")
            print(subject_competence)
            # Agregar la competencia a la sesión de la base de datos
            db.session.add(subject_competence)
            # Confirmar y guardar los cambios en la base de datos para obtener el ID de la competencia
            db.session.commit()

            # Crear el RAP (LearningOutcome) asociado con la competencia recién creada
            loutcome = LearningOutcome(lout_description=raa_data['lout_description'],
                                        comp_id=subject_competence.comp_id,  # Asociar el RAP con la competencia
                                        #lout_subject_id=next_lout_id  # El RAP puede o no tener un 'subject_id'
                                    )
            # Agregar el RAP a la sesión de la base de datos
            db.session.add(loutcome)

            # Confirmar y guardar los cambios en la base de datos
            db.session.commit()
            return "Competencia de asignatura creada exitosamente", None
        except Exception as e:
            db.session.rollback()  # Si hay error, hacer rollback
            return None, f"Error al crear la competencia de asignatura: {str(e)}"
        
    @staticmethod
    def get_all_assignments():
        try:
            # Consultar todas las asignaciones 
            assignments = db.session.query(IntegrationTSC).all()
            # Convertir los objetos de asignaciones a diccionarios y ver su contenido con un print
            # !No se usa el MEtodo to_dict() porque son campos especificos.
            assignments_dict = [ass.to_dict() for ass in assignments]
            # Recuperar nombres correspondientes a los IDs
            enriched_assignments = []
            for ass in assignments_dict:
                subj_name = db.session.query(Subject.name).filter(Subject.id == ass["subj_id"]).scalar()
                teach_name = db.session.query(Teacher.teName).filter(Teacher.teId == ass["teach_id"]).scalar()
                #comp_desc = db.session.query(Competence.comp_description).filter(Competence.comp_id == ass["comp_id"]).scalar()
                
                # Enriquecer la información con los nombres
                enriched_assignments.append({
                    "subject_name": subj_name,
                    "teacher_name": teach_name,
                    "comp_id": ass["comp_id"],
                    "time": ass["time"]
                })
            
            print("ASIGNACIONES ENRIQUECIDAS")
            print(enriched_assignments)  # Imprimir resultados enriquecidos
            
            return enriched_assignments, None  
        except Exception as e:
            # En caso de error, devolver el mensaje de error
            print(f"Error: {str(e)}")
            return [], f"Error al obtener las asignaciones: {str(e)}" 
        
    @staticmethod
    def get_assign_by_teacher(tea_id):
        """
        Obtiene todas las asignaciones para un profesor específico basado en su ID.
        """
        try:
            # Consultar las asignaciones del profesor
            assignments = IntegrationTSC.query.filter_by(teach_id=tea_id).all()

            if not assignments:
                return None, f"No se encontraron asignaciones para el docente con ID {tea_id}"

            # Convertir los resultados a diccionarios
            return [assignment.to_dict() for assignment in assignments], None
            

        except Exception as e:
            return None, f"Error al consultar las asignaciones: {str(e)}"

    @staticmethod
    def get_competences_names_by_ids(comp_ids):
        try:
            # Consulta de competencias
            competencias = (
                db.session.query(Competence.comp_id, Competence.comp_description)
                .filter(Competence.comp_id.in_(comp_ids))
                .all()
            )
            # Convertir los resultados a una lista de diccionarios
            return [{"comp_id": comp[0], "comp_description": comp[1]} for comp in competencias],None
        except Exception as e:
            
            return [], f"Error al consultar competencias: {e}"
        
    @staticmethod
    def get_louts_names_by_ids(louts_ids):
        try:
            # Consulta de competencias
            louts = (
                db.session.query(LearningOutcome.lout_id, LearningOutcome.lout_description)
                .filter(LearningOutcome.lout_id.in_(louts_ids))
                .all()
            )
            # Convertir los resultados a una lista de diccionarios
            return [{"lout_id": lo[0], "lout_description": lo[1]} for lo in louts],None
        except Exception as e:
            
            return [], f"Error al consultar resultados de aprendizaje: {e}"