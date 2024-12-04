from flask import Blueprint, request, jsonify
from Model.evaluator import Evaluator, db

evaluator_bp = Blueprint("evaluator", __name__, url_prefix="/evaluators")

@evaluator_bp.route("/<int:evaluator_id>/rubrics", methods=["GET"])
def get_rubrics_by_evaluator(evaluator_id):
    evaluator = Evaluator.query.get_or_404(evaluator_id)
    rubrics = evaluator.get_rubrics()
    return jsonify(rubrics)

@evaluator_bp.route("/<int:evaluator_id>/report", methods=["GET"])
def generate_evaluator_report(evaluator_id):
    evaluator = Evaluator.query.get_or_404(evaluator_id)
    report = evaluator.generate_report()
    return jsonify(report)
