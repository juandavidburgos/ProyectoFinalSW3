from Services.learningOutcomeService import LearningOutcomeService

class LoutFacade:
    def __init__(self):
        self.lo_service = LearningOutcomeService()

    def create_lo(self, lout_data):
        # Crear la asignatura a través del servicio correspondiente
        return self.lo_service.create_learning_outcome(lout_data)

    def get_all_louts(self):
        # Obtener todas las asignaturas del servicio
        return self.lo_service.get_all_learning_outcomes()
    
    def update_learning_outcome(self, lout_id, data):
        return self.lo_service.update_learning_outcome(lout_id, data)

    def get_learning_outcome_by_id(self,lo_id):
        return self.lo_service.get_learning_outcome_by_id(lo_id)