from Services.competenceService import CompetenceService
from Services.teacherService import TeacherService
from Services.subjectService import SubjectService
from Services.integrationService import IntegrationService

class IntegrationFacade:
    def __init__(self):
        self.competence_service = CompetenceService()
        self.teacher_service = TeacherService()
        self.subject_service = SubjectService()
        self.integration_service=IntegrationService()

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


