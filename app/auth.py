from functools import wraps
from typing import Optional

from flask import g, request
from jwt import DecodeError, decode

from app.errors import AuthenticationError
from app.models import UserModel


def auth_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        auth_header = _extract_token_from_authorization_header(
            request.headers.get("Authorization")
        )
        if auth_header:
            user_model = _authenticate_user(auth_header)
            if user_model:
                g.current_user = user_model
                return f(*args, **kwargs)
        return AuthenticationError().message

    return wrap


def _extract_token_from_authorization_header(
    authorization_header: Optional[str],
) -> Optional[str]:
    bearer = "Bearer "
    if authorization_header is not None:
        if authorization_header.startswith(bearer):
            return authorization_header[len(bearer) :]
    return None


def _authenticate_user(token: str) -> Optional[UserModel]:
    try:
        payload = decode(token, options={"verify_signature": False})
    except DecodeError:
        return None

    return UserModel.query.get(payload.get("user_id"))
