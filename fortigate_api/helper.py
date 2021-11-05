"""Helper functions"""
from typing import Any
from urllib.parse import quote

from fortigate_api.typing_ import DAny, StrInt


def int_(key: StrInt, **kwargs) -> int:
    """Get key=value from kwargs and return value as integer"""
    if value := kwargs.get(key) or 0:
        try:
            value = int(value)
        except (TypeError, ValueError):
            raise ValueError(f"invalid {key}={value}")
    return value


def str_(key: str, **kwargs) -> str:
    """Get key=value from kwargs and return value as string"""
    if value := kwargs.get(key) or "":
        if not isinstance(value, str):
            raise ValueError(f"invalid {key}={value}")
    return value


def quote_(string: Any) -> str:
    """quote name of object. Example: "10.0.0.0/8" > "10.0.0.0%2F8" """
    return quote(string=string, safe="")


def name_to_filter(kwargs: DAny) -> None:
    """replace "name" argument to "filter" """
    if name := kwargs.get("name", ""):
        del kwargs["name"]
        kwargs["filter"] = f"name=={name}"
