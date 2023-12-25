"""unittest base.py"""

import pytest
from requests import Response

from fortigate_api import FortigateAPI
from tests.helper__tst import NAME1, SLASH, SLASH_

URL_BASE = "api/v2/cmdb/firewall/address/"


@pytest.fixture
def api():
    """Init FortigateAPI"""
    return FortigateAPI(host="host")


@pytest.mark.parametrize("status_codes, expected", [
    ([], 200),
    ([200, 200], 200),
    ([200, 500, 400], 500),
    ([200, 400, 500], 500),
])
def test__highest_response(api: FortigateAPI, status_codes, expected):
    """Base._highest_response()"""
    responses = []
    for status_code in status_codes:
        response = Response()
        response.status_code = status_code
        responses.append(response)
    response_: Response = api.address._highest_response(responses)
    actual = response_.status_code
    assert actual == expected


@pytest.mark.parametrize("url, expected", [
    ("", ""),
    (URL_BASE, URL_BASE),
    (f"{URL_BASE}{NAME1}", f"{URL_BASE}{NAME1}"),
    (f"{URL_BASE}{SLASH}", f"{URL_BASE}{SLASH_}"),
    (SLASH, SLASH),
])
def test__class_to_attr(api: FortigateAPI, url, expected):
    """Base._quote_url()"""
    actual = api.address._quote_url(url=url)
    assert actual == expected
