from typing import Any, Dict
from uuid import UUID

from schema import And, Optional, Schema, Use


def generic(field_name: str, value_type):
    return Use(
        value_type,
        error=f"{field_name.capitalize()} expected to be a(n) {value_type.__name__}.",
    )


def fixed_length_string(field_name: str, min_length: int, max_length: int):
    return And(
        str,
        lambda x: min_length <= len(x) <= max_length,
        error=f"{field_name.capitalize()} expected to be a string with a length of [{min_length}, {max_length}].",
    )


feedback_schema = Schema(
    {
        Optional("challenge_id", default=None): And(str, len, Use(UUID)),
        "data": dict,
    }
)


feedback_search_schema = Schema({Optional("challenge_id"): And(str, len, Use(UUID))})


class FeedbackSchema:
    _challenge_id = generic("challenge_id", UUID)
    _data = generic("data", dict)
    _feedback_data = {
        "score": generic("score", int),
        "feedback": fixed_length_string("feedback", 0, 1000),
    }
    _url = fixed_length_string("url", 1, 500)
    _is_support = generic("is_support", bool)

    _post_schema = Schema(
        {Optional("challenge_id"): _challenge_id, "data": _data}, ignore_extra_keys=True
    )

    _challenge_data_schema = Schema(
        {
            "user_effort": _feedback_data,
            "educational_value": _feedback_data,
            "url": _url,
            Optional("is_support"): _is_support,
        },
        ignore_extra_keys=True,
    )

    _platform_data_schema = Schema(
        {
            "platform_ux": _feedback_data,
            "url": _url,
            Optional("is_support"): _is_support,
        },
        ignore_extra_keys=True,
    )

    @classmethod
    def validate_post(cls, data: Dict[str, Any]) -> Dict[str, Any]:
        data = cls._post_schema.validate(data)
        data["data"] = (
            cls.validate_challenge_data(data["data"])
            if data.get("challenge_id")
            else cls.validate_platform_data(data["data"])
        )
        return data

    @classmethod
    def validate_challenge_data(cls, data: Dict[str, Any]) -> Dict[str, Any]:
        return cls._challenge_data_schema.validate(data)

    @classmethod
    def validate_platform_data(cls, data: Dict[str, Any]) -> Dict[str, Any]:
        return cls._platform_data_schema.validate(data)
