from json import loads

from flask import g, jsonify, request
from schema import SchemaError

from app.auth import auth_required
from app.errors import BadRequestError
from app.feedbacks import bp
from app.feedbacks.create_feedback import CreateFeedback
from app.feedbacks.schemas import FeedbackSchema
from app.models import FeedbackModel


@bp.route("/", strict_slashes=False, methods=["POST"])
@auth_required
def create_feedback():
    try:
        payload = FeedbackSchema.validate_post(request.get_json(force=True))
    except SchemaError as schema_error:
        return BadRequestError(errors=schema_error.code).message

    feedback_model: FeedbackModel = CreateFeedback(
        db_session=g.db_session,
        current_user=g.current_user,
        data=payload["data"],
        challenge_id=payload.pop("challenge_id", None),
    ).execute()

    return (
        jsonify(
            {
                "user_id": feedback_model.user_id,
                "data": loads(feedback_model.data),
                "challenge_id": feedback_model.challenge_id,
            }
        ),
        201,
    )


@bp.route("/", strict_slashes=False, methods=["GET"])
def test():
    feedbacks = FeedbackModel.query.all()
    return (
        jsonify(
            [
                {
                    "user_id": feedback_model.user_id,
                    "data": loads(feedback_model.data),
                    "challenge_id": feedback_model.challenge_id,
                }
                for feedback_model in feedbacks
            ]
        ),
        200,
    )
