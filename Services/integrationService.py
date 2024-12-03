from Model.competence import Competence
from Model.learningOutcome import LearningOutcome
from Model.tscIntegration import IntegrationTSC
from Model.connection import db


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

    @staticmethod    
    def get_next_lout_id():
        #*Obtiene el siguiente ID disponible para lout_subject_id para no tener conflictos
        
        max_subject_id = db.session.query(db.func.max(LearningOutcome.lout_subject_id)).scalar()
        return (max_subject_id or 0) + 1  # Si no hay registros, comienza desde 1



    @staticmethod
    def create_subject_competence(subcompetence_data,raa_data):
        try:
            # Obtener el siguiente ID disponible para comp_subject_id
            next_subject_id = IntegrationService.get_next_subject_id()
            next_lout_id = IntegrationService.get_next_lout_id()

            subject_competence = Competence(comp_description=subcompetence_data['comp_description'],
                                comp_type=subcompetence_data['comp_type'],
                                comp_level=None,  # Puede ser None si es de tipo programa
                                comp_subject_id=next_subject_id 
                                )
            

            # Agregar la competencia a la sesión de la base de datos
            db.session.add(subject_competence)
            # Confirmar y guardar los cambios en la base de datos para obtener el ID de la competencia
            db.session.commit()

            # Crear el RAP (LearningOutcome) asociado con la competencia recién creada
            loutcome = LearningOutcome(lout_description=raa_data['lout_sub_description'],
                                        comp_id=subcompetence_data.comp_id,  # Asociar el RAP con la competencia
                                        lout_subject_id=next_lout_id  # El RAP puede o no tener un 'subject_id'
                                    )
            # Agregar el RAP a la sesión de la base de datos
            db.session.add(loutcome)
            # Confirmar y guardar los cambios en la base de datos
            db.session.commit()
            return "Competencia de asignatura creada exitosamente", None
        except Exception as e:
            db.session.rollback()  # Si hay error, hacer rollback
            return None, f"Error al crear la competencia de asignatura: {str(e)}"
        
