from Services.competenceService import CompetenceService
from Services.rubricService import RubricService
from Services.evaluatorService import EvaluatorService
from Services.resultaApRubricaService import ResultaApRubricaService
from Services.learningOutcomeService import LearningOutcomeService

class IntegrationFacade:
    def __init__(self):
        self.competence_service = CompetenceService()
        self.evaluator_service = EvaluatorService()
        self.integrationRARubric_service=ResultaApRubricaService()
        self.loutService = LearningOutcomeService()





