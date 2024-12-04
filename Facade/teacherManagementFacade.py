from Services.teacherService import TeacherService

class TeacherManagementFacade:
    def __init__(self):
        self.teacher_service = TeacherService()

    def create_teacher(self, teacher_data):
        # Crear la profesor a través del servicio correspondiente
        return self.teacher_service.create_teacher(teacher_data)
    
    def get_all_teachers(self):
        return self.teacher_service.get_all_teacher()

