from Services.competenceService import CompetenceService
class CmpLoutFacade:
    #*Fachada que integra los servicios de competencia y RAP.

    def __init__(self):
        self.competence_service = CompetenceService()

    def create_competence_with_rap(self, competence_data, rap_data):

        #*Crea una competencia y un RAP utilizando el servicio correspondiente.
        return self.competence_service.create_competence_with_rap(competence_data, rap_data)