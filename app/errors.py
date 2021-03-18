from abc import ABC
from typing import Optional, List
from flask import jsonify


class ErrorBase(ABC):
    _code: int
    _message: str

    @property
    def message(self):
        return (
            jsonify(
                {
                    "message": self._message,
                }
            ),
            self._code,
        )


class BadRequestError(ErrorBase):
    _code = 400
    _message = "Invalid input parameters!"

    def __init__(self, errors: Optional[List[str]] = None):
        if errors:
            self._message = f"{self._message[:-1]}:\n {errors}"
        super().__init__()


class AuthenticationError(ErrorBase):
    _code = 401
    _message = "Missing or invalid authentication header!"


class AuthorizationError(ErrorBase):
    _code = 403
    _message = "You don't have permission for this operation!"


class NotFoundError(ErrorBase):
    _code = 404
    _message = "Oops, resource or page not found!"


class InternalError(ErrorBase):
    _code = 500
    _message = "Something went wrong, please try again later."
