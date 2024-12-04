from Services.competenceService import CompetenceService
from Services.teacherService import TeacherService
from Services.subjectService import SubjectService
from Services.integrationService import IntegrationService
from Services.learningOutcomeService import LearningOutcomeService

class IntegrationFacade:
    def __init__(self):
        self.competence_service = CompetenceService()
        self.teacher_service = TeacherService()
        self.subject_service = SubjectService()
        self.integration_service=IntegrationService()
        self.loutService = LearningOutcomeService()

    def assign_to_subject(self, comp_id, teacher_id, subject_id, time_data):
        message, error = self.integration_service.create_subject_assign(comp_id, teacher_id, subject_id,time_data)
        if error:
            return None, error
        return message, None
    
    def create_subject_competence(self,subject_competence_data, raa_data):
        message, error = self.integration_service.create_subject_competence(subject_competence_data,raa_data)
        if error:
            return None, error
        return message, None
    
    @staticmethod
    def get_subjects():
        subjects, error = SubjectService.get_all_subjects()
        if error:
            return None, error
        return subjects, None
    @staticmethod
    def get_teachers():
        teachers, error = TeacherService.get_all_teacher()
        if error:
            return None, error
        return teachers, None
    @staticmethod
    def get_competences():
        competences, error = CompetenceService.get_all_competences_description()
        if error:
            return None, error
        return competences, None 

    @staticmethod
    def get_all_competences():
        competences, error = CompetenceService.get_all_competences_1()
        if error:
            return None, error
        return competences, None  

    @staticmethod
    def get_assignments():  
        assignments , error = IntegrationService.get_all_assignments()
        if error:
            return None, error
        return assignments, None  

    @staticmethod
    def get_assignment_by_teacher(tea_id):
        assingment , error = IntegrationService.get_assign_by_teacher(tea_id)
        if error:
            return None, error
        return assingment, None 

    @staticmethod
    def get_competences_names_by_ids(comp_ids):
        competences , error = IntegrationService.get_competences_names_by_ids(comp_ids)
        if error:
            return None, error
        return competences, None  
    
    @staticmethod
    def get_lout_by_competence(comp_id):
        lout, error = LearningOutcomeService.get_learning_outcomes_by_competencia(comp_id)
        if error:
            return None, error
        return lout, None 
    
    @staticmethod
    def get_lout_names_by_ids(lout_ids):
        louts , error = IntegrationService.get_louts_names_by_ids(lout_ids)
        if error:
            return None, error
        return louts, None  
    
    def get_lout_by_id(self,lout_id):
        return self.loutService.get_learning_outcome_by_id(lout_id)
    
    def update_subject_lout(self,lout_id, data):
        return self.loutService.update_learning_outcome(lout_id,data)



