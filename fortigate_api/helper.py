"""Helper functions"""
from typing import Any
from urllib.parse import urlencode, urlparse, parse_qs, quote, ParseResult

from fortigate_api.types_ import DAny, StrInt, DStr


# =============================== int ================================

def int_(key: str, **kwargs) -> int:
    """Gets key=value from kwargs and return value as integer"""
    value_ = 0
    value: StrInt
    if value := kwargs.get(key) or "":
        try:
            value_ = int(value)
        except (TypeError, ValueError):
            raise ValueError(f"invalid {key}={value}")
    return value_


# =============================== str ================================

def add_params_to_url(url: str, params: DStr) -> str:
    """Adds params to URL
    :param url: URL with old params
    :param params: New params
    :return: URL with old and new params
    :example:
        url: "https://fomain.com?a=a"
        params: {"b": ["b", "B"]}
        return: "https://fomain.com?a=a&b=b&b=B"
    """
    url_parsed: ParseResult = urlparse(url)
    params_or: DAny = parse_qs(url_parsed.query)
    params_: DAny = {**params_or, **params}
    query: str = urlencode(params_, doseq=True)
    url_parsed = url_parsed._replace(query=query)
    url_: str = url_parsed.geturl()
    return url_


def str_(key: str, **kwargs) -> str:
    """Gets key=value from kwargs and return value as string"""
    if value := kwargs.get(key) or "":
        if not isinstance(value, str):
            raise ValueError(f"invalid {key}={value}")
    return value


def quote_(string: Any) -> str:
    """quote name of the object. Example: "10.0.0.0/8" > "10.0.0.0%2F8" """
    return quote(string=string, safe="")
