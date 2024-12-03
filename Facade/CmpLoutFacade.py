from Services.competenceService import CompetenceService
class CmpLoutFacade:
    def __init__(self):
        self.competence_service = CompetenceService()

    def create_competence_with_rap(self, competence_data, rap_data):
        # Crear la competencia y el RAP a través del servicio correspondiente
        return self.competence_service.create_competence_with_rap(competence_data, rap_data)

    def get_all_competences(self):
        # Obtener todas las competencias del servicio
        return self.competence_service.get_all_competences()

