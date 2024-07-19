from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment
from core.models.principals import Principal

from .schema import AssignmentSchema, AssignmentSubmitSchema, TeachersSchema, AssignmentGradeSchema
principal_assignments_resources = Blueprint('principal_assignments_resources', __name__)

@principal_assignments_resources.route("/assignments",methods=['GET'],strict_slashes=False)
@decorators.authenticate_principal
def list_assignments(p):
    """Returns list of submitted or graded assignments"""
    submitted_and_graded = Assignment.get_submitted_or_graded_assignments()
    submitted_and_graded_dump = AssignmentSchema().dump(submitted_and_graded,many=True)
    return APIResponse.respond(data=submitted_and_graded_dump)

@principal_assignments_resources.route("/teachers",methods=['GET'],strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p):
    """Returns list of all teachers"""
    teachers = Principal.get_teachers()
    teachers_dump = TeachersSchema().dump(teachers,many=True)
    return APIResponse.respond(data=teachers_dump)

@principal_assignments_resources.route("/assignments/grade",methods=['POST'],strict_slashes=False)
@decorators.accept_payload
@decorators.authenticate_principal
def grade_assignment(p, incoming_payload):
    """Grade an assignment"""
    grade_assignment_payload = AssignmentGradeSchema().load(incoming_payload)

    graded_assignment = Assignment.re_grade(
        _id=grade_assignment_payload.id,
        grade=grade_assignment_payload.grade,
        auth_principal=p
    )
    db.session.commit()
    graded_assignment_dump = AssignmentSchema().dump(graded_assignment)
    return APIResponse.respond(data=graded_assignment_dump)