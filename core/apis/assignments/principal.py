from flask import jsonify # type: ignore
from models import Assignment

def get_all_assignments():
    assignments = Assignment.query.filter_by(state='graded').all()
    return jsonify([assignment.to_dict() for assignment in assignments])