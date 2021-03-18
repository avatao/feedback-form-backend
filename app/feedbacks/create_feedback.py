from json import dumps
from typing import Any, Dict, Optional
from uuid import UUID

from sqlalchemy.orm.session import Session

from app.models import FeedbackModel, UserModel


class CreateFeedback:
    def __init__(
        self,
        db_session: Session,
        current_user: UserModel,
        data: Dict[str, Any],
        challenge_id: Optional[UUID] = None,
    ):
        self._db_session = db_session
        self._current_user = current_user
        self._data = data
        self._challenge_id = challenge_id

    def execute(self) -> FeedbackModel:
        feedback_model = FeedbackModel(
            user_id=self._current_user.id,
            data=dumps(self._data),
            challenge_id=str(self._challenge_id),
        )
        self._db_session.add(feedback_model)
        self._db_session.commit()

        return feedback_model
