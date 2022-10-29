"""Tools for String"""
import re
from typing import Any
from urllib import parse
from urllib.parse import urlencode, urlparse, parse_qs, ParseResult

from fortigate_api.types_ import DAny, T2Str, T3Str


def findall1(pattern: str, string: str, flags=0) -> str:
    """Return 1st item of re.findall(). If nothing is found, return an empty string.
    Group with parentheses in pattern is required.
    """
    return (re.findall(pattern=pattern, string=string, flags=flags) or [""])[0]


def findall2(pattern: str, string: str, flags=0) -> T2Str:
    """Return 2 items of re.findall(). If nothing is found, return empty strings.
    Group with parentheses in pattern is required.
    """
    return (re.findall(pattern=pattern, string=string, flags=flags) or [("", "")])[0]


def findall3(pattern: str, string: str, flags=0) -> T3Str:
    """Return 3 items of re.findall(). If nothing is found, return empty strings.
    Group with parentheses in pattern is required.
    """
    return (re.findall(pattern=pattern, string=string, flags=flags) or [("", "", "")])[0]


def make_url(url: str, **params) -> str:
    """Adds params to URL
    :param url: URL with old params
    :param params: New params
    :return: URL with old and new params
    :example:
        str_: "https://fomain.com?a=a"
        params: {"b": ["b", "B"]}
        return: "https://fomain.com?a=a&b=b&b=B"
    """
    url_parsed: ParseResult = urlparse(url)
    params_or: DAny = parse_qs(url_parsed.query)
    params_: DAny = {**params_or, **params}
    query: str = urlencode(params_, doseq=True)
    url_parsed = url_parsed._replace(query=query)
    return url_parsed.geturl()


def quote(string: Any) -> str:
    """Quote name of the string
    :param string: Line to by quoted
    :example: "10.0.0.0/8" > "10.0.0.0%2F8"
    """
    string_ = str(string)
    return parse.quote(string=string_, safe="")
