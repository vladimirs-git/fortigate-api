"""unittest fortigate.py"""
import json
import unittest
from http.cookiejar import Cookie
from typing import Any
from unittest.mock import patch

import pytest
from pytest_mock import MockerFixture
from requests import Session, Response

from fortigate_api import Fortigate, FortigateAPI
from tests.helper__tst import NAME1, MockSession

QUERY = "api/v2/cmdb/firewall/address"


class MockCookie:
    """Mock Cookie."""

    def __init__(self, name: str, value: str):
        """Init Cookie."""
        self.name = name
        self.value = value


def crate_response(status_code: int) -> Response:
    """Return Response object with status_code=200."""
    response = Response()
    response.status_code = status_code
    return response


@pytest.fixture
def fgt():
    """Init Fortigate"""
    fgt_ = Fortigate(host="host")
    fgt_._session = Session()
    return fgt_


@pytest.fixture
def api(fgt: Fortigate):
    """Init FortigateAPI"""
    api_ = FortigateAPI(host="host")
    api_.rest = fgt
    return api_


def create_cookie(name: str, value: str) -> Cookie:
    """Return Cookie object."""
    return Cookie(
        version=0,
        name=name,
        value=value,
        port=None,
        port_specified=False,
        domain="host.local",
        domain_specified=False,
        domain_initial_dot=False,
        path="/",
        path_specified=True,
        secure=True,
        expires=None,
        discard=True,
        comment=None,
        comment_url=None,
        rest={},
    )


def create_session_w_cookie(name: str, value: str) -> Session:
    """Return Session object with cookies."""
    cookie = create_cookie(name, value)
    session = Session()
    session.cookies = [cookie]  # type: ignore
    return session


def create_response(method: str, url: str, status_code: int, data: Any = None) -> Response:
    """Create response."""
    resp = Response()
    resp.url = url
    resp.status_code = status_code
    data_ = {"http_method": method.upper(), "revision": "1", "status": "success"}
    if status_code >= 400:
        data_.update({"status": "error"})
    if data is not None:
        data_["results"] = data
    text = json.dumps(data_)
    resp._content = text.encode("utf-8")
    return resp


def mock_response(mocker: MockerFixture, response: Response) -> Response:
    """Crate mock based on Response"""
    resp: Response = mocker.Mock(spec=Response)
    resp.url = response.url
    resp.status_code = response.status_code
    resp.ok = response.ok  # type: ignore
    resp.reason = ""
    resp.json.return_value = response.json()  # type: ignore
    return resp


def mock_session_delete(mocker: MockerFixture, url, *args, **kwargs) -> Response:
    """Mock Session.delete()"""
    _ = args, kwargs
    if url == 'https://host/api/v2/cmdb/firewall/policy/1':
        resp = create_response("delete", url, 200)
    elif url == 'https://host/api/v2/cmdb/firewall/policy/2':
        resp = create_response("delete", url, 404)
    else:
        resp = create_response("delete", url, 400)
    return mock_response(mocker, resp)


def mock_session_get(mocker: MockerFixture, url, *args, **kwargs) -> Response:
    """Mock Session.get()"""
    _ = args, kwargs
    if url == 'https://host/api/v2/cmdb/firewall/policy/1':
        resp = create_response("get", url, 200, [{"id": "1", "name": NAME1}])
    elif url == 'https://host/api/v2/cmdb/firewall/policy/2':
        resp = create_response("get", url, 200, [])
    else:
        resp = create_response("get", url, 400)
    return mock_response(mocker, resp)


def mock_session_post(mocker: MockerFixture, url, *args, **kwargs) -> Response:
    """Mock Session.post()"""
    _ = args, kwargs
    if url == 'https://host/api/v2/cmdb/firewall/policy/1':
        resp = create_response("post", url, 200)
    elif url.find("https://host/api/v2/cmdb/firewall/policy") > -1:
        resp = create_response("post", url, 500)
    else:
        resp = create_response("post", url, 400)
    return mock_response(mocker, resp)


def mock_session_put(mocker: MockerFixture, url, *args, **kwargs) -> Response:
    """Mock Session.put()"""
    _ = args, kwargs
    if url == 'https://host/api/v2/cmdb/firewall/policy/1':
        resp = create_response("put", url, 200)
    elif url.find("https://host/api/v2/cmdb/firewall/policy") > -1:
        resp = create_response("put", url, 404)
    else:
        resp = create_response("put", url, 400)
    return mock_response(mocker, resp)


class Test(unittest.TestCase):
    """Fortigate"""

    def setUp(self):
        """setUp"""
        patch.object(Fortigate, "_get_session", return_value=MockSession()).start()
        self.rest = Fortigate(host="host", username="username", password="")
        self.url_policy = f"{self.rest.url}/api/v2/cmdb/firewall/policy/"

    def test_valid__repr__(self):
        """Fortigate.__repr__()"""
        default = dict(scheme="https", port=443, timeout=15, vdom="root")
        for kwargs, req in [
            # username password
            (dict(host="a", username="b", password="c"),
             "Fortigate(host='a', username='b')"),
            (dict(host="a", username="b", password="c", **default),
             "Fortigate(host='a', username='b')"),
            (dict(host="a", username="b", password="c", port=80),
             "Fortigate(host='a', username='b', port=80)"),
            (dict(host="a", username="b", password="c", scheme="https", port=80),
             "Fortigate(host='a', username='b', port=80)"),
            (dict(host="a", username="b", password="c", scheme="http", port=80),
             "Fortigate(host='a', username='b', scheme='http', port=80)"),
            (dict(host="a", username="b", password="c", timeout=1),
             "Fortigate(host='a', username='b', timeout=1)"),
            (dict(host="a", username="b", password="c", vdom="d"),
             "Fortigate(host='a', username='b', vdom='d')"),
            (dict(host="a", username="b", password="c", vdom="d", timeout=1, port=80),
             "Fortigate(host='a', username='b', port=80, timeout=1, vdom='d')"),
            (dict(host="a", username="b", password="c", verify=True),
             "Fortigate(host='a', username='b', verify=True)"),
            (dict(host="a", username="b", password="c", verify=False),
             "Fortigate(host='a', username='b')"),
            # token
            (dict(host="a", token="b"), "Fortigate(host='a', username='')"),
        ]:
            fgt = Fortigate(**kwargs)
            result = f"{fgt!r}"
            self.assertEqual(result, req, msg=f"{fgt=}")

    def test_valid__enter__(self):
        """Fortigate.__enter__() Fortigate.__exit__()"""
        with patch("requests.session", return_value=MockSession()):
            with Fortigate(host="host", username="username", password="") as fgt:
                session = fgt._session
                if session is not None:
                    result = session.__class__.__name__
                    req = "MockSession"
                    self.assertEqual(result, req, msg="MockSession")

    # ============================= init =============================

    def test_valid__init_port(self):
        """Fortigate._init_port()"""
        https = "https"
        for kwargs, scheme, req in [
            ({}, https, 443),
            ({}, "http", 80),
            (dict(port=""), https, 443),
            (dict(port=""), "http", 80),
            (dict(port=0), https, 443),
            (dict(port=0), "http", 80),
            (dict(port="0"), https, 443),
            (dict(port="0"), "http", 80),
            (dict(port=1), https, 1),
            (dict(port="1"), "http", 1),
        ]:
            self.rest.scheme = scheme
            result = self.rest._init_port(**kwargs)
            self.assertEqual(result, req, msg=f"{kwargs=}")

    def test_invalid__init_port(self):
        """Fortigate._init_port()"""
        for kwargs, error in [
            (dict(port="typo"), ValueError),
        ]:
            with self.assertRaises(error, msg=f"{kwargs=}"):
                self.rest._init_port(**kwargs)

    def test_valid__init_scheme(self):
        """Fortigate._init_scheme()"""
        https = "https"
        for kwargs, req in [
            ({}, https),
            (dict(scheme=""), https),
            (dict(scheme="https"), https),
            (dict(scheme="http"), "http"),
        ]:
            result = self.rest._init_scheme(**kwargs)
            self.assertEqual(result, req, msg=f"{kwargs=}")

    def test_invalid__init_scheme(self):
        """Fortigate._init_scheme()"""
        for kwargs, error in [
            (dict(scheme="ssh"), ValueError),
        ]:
            with self.assertRaises(error, msg=f"{kwargs=}"):
                self.rest._init_scheme(**kwargs)

    def test_valid__init_token(self):
        """Fortigate._init_token()"""
        fgt = Fortigate(host="", username="", password="")
        for kwargs, req in [
            ({}, ""),
            (dict(token="a"), "a"),
        ]:
            result = fgt._init_token(**kwargs)
            self.assertEqual(result, req, msg=f"{kwargs=}")

    def test_invalid__init_token(self):
        """Fortigate._init_token()"""
        for kwargs, error in [
            (dict(host="", username="username"), ValueError),
            (dict(host="", password="password"), ValueError),
        ]:
            fgt = Fortigate(**kwargs)
            with self.assertRaises(error, msg=f"{kwargs=}"):
                fgt._init_token(token="token")


# =========================== property ===========================


@pytest.mark.parametrize("session, expected", [
    (None, False),
    (Session(), True),
])
def test__is_connected(fgt: Fortigate, session, expected):
    """Fortigate.is_connected()"""
    fgt._session = session
    actual = fgt.is_connected
    assert actual == expected


@pytest.mark.parametrize("scheme, host, port, expected", [
    ("https", "host", 80, "https://host:80"),
    ("https", "127.0.0.255", 80, "https://127.0.0.255:80"),
    ("https", "host", 443, "https://host"),
    ("https", "127.0.0.255", 443, "https://127.0.0.255"),
    ("http", "host", 80, "http://host"),
    ("http", "127.0.0.255", 80, "http://127.0.0.255"),
    ("http", "host", 443, "http://host:443"),
    ("http", "127.0.0.255", 443, "http://127.0.0.255:443"),
])
def test__url(scheme, host, port, expected):
    """Fortigate.url()"""
    fgt = Fortigate(host=host, scheme=scheme, port=port)
    actual = fgt.url
    assert actual == expected

    # =========================== methods ============================


@pytest.mark.parametrize("url, expected", [
    ("https://host/api/v2/cmdb/firewall/policy/1", 200),
    # ("https://host/api/v2/cmdb/firewall/policy/2", 404),
    # ("https://host/api/v2/cmdb/firewall/typo/1", 400),
])
def test__delete(api: FortigateAPI, mocker: MockerFixture, url, expected):
    """Fortigate.delete()"""
    fgt: Fortigate = api.rest
    mocker.patch("requests.Session.delete",
                 side_effect=lambda *args, **kw: mock_session_delete(mocker, *args, **kw))

    response = fgt.delete(url=url)
    actual = response.status_code
    assert actual == expected


# @pytest.mark.parametrize("url, expected", [
#     ("https://host/api/v2/cmdb/firewall/policy/1", [{"id": "1", "name": "NAME1"}]),
#     ("https://host/api/v2/cmdb/firewall/policy/2", []),
#     ("https://host/api/v2/cmdb/firewall/typo/1", []),
# ])
# def test__get(api: FortigateAPI, mocker: MockerFixture, url, expected):
#     """Fortigate.get()"""
#     fgt: Fortigate = api.rest
#     mocker.patch("requests.Session.get",
#                  side_effect=lambda *args, **kw: mock_session_get(mocker, *args, **kw))
#
#     actual = fgt.get(url=url)
#     assert actual == expected
#
#
# @pytest.mark.parametrize("url, expected", [
#     ("https://host/api/v2/cmdb/firewall/policy/1", 200),
#     ("https://host/api/v2/cmdb/firewall/policy/2", 500),
#     ("https://host/api/v2/cmdb/firewall/typo/1", 400),
# ])
# def test__post(api: FortigateAPI, mocker: MockerFixture, url, expected):
#     """Fortigate.post()"""
#     fgt: Fortigate = api.rest
#     mocker.patch("requests.Session.post",
#                  side_effect=lambda *args, **kw: mock_session_post(mocker, *args, **kw))
#
#     response = fgt.post(url=url, data={"name": "NAME1"})
#     actual = response.status_code
#     assert actual == expected
#
#
# @pytest.mark.parametrize("url, expected", [
#     ("https://host/api/v2/cmdb/firewall/policy/1", 200),
#     ("https://host/api/v2/cmdb/firewall/policy/2", 404),
#     ("https://host/api/v2/cmdb/firewall/typo/1", 400),
# ])
# def test__put(api: FortigateAPI, mocker: MockerFixture, url, expected):
#     """Fortigate.put()"""
#     fgt: Fortigate = api.rest
#     mocker.patch("requests.Session.put",
#                  side_effect=lambda *args, **kw: mock_session_put(mocker, *args, **kw))
#
#     response = fgt.put(url=url, data={"name": "NAME1"})
#     actual = response.status_code
#     assert actual == expected


# @pytest.mark.parametrize("url, expected", [
#     ("https://host/api/v2/cmdb/firewall/policy/1", 200),
#     ("https://host/api/v2/cmdb/firewall/policy/2", 404),
# ])
# def test__exist(api: FortigateAPI, mocker: MockerFixture, url, expected):
#     """Fortigate.exist()"""
#     fgt: Fortigate = api.rest
#     mocker.patch("requests.Session.get",
#                  side_effect=lambda *args, **kw: mock_session_get(mocker, *args, **kw))
#
#     response = fgt.exist(url=url)
#     actual = response.status_code
#     assert actual == expected


# =========================== helpers ============================

def test__get_session(fgt: Fortigate, mocker: MockerFixture):
    """Fortigate._get_session()"""
    # session
    fgt._session = Session()
    session = fgt._get_session()
    assert isinstance(session, Session)

    # login
    fgt._session = None
    mock_response = mocker.Mock()
    mock_response.text = "Mocked response"
    mocker.patch("requests.Session.post", return_value=mock_response)
    mocker.patch("requests.Session.get", return_value=crate_response(200))
    with patch("fortigate_api.Fortigate._get_token_from_cookies", return_value="token"):
        session = fgt._get_session()
        assert isinstance(session, Session)


@pytest.mark.parametrize("name, expected", [
    ("ccsrftoken", "token"),  # < v7
    ("ccsrftoken_443", "token"),  # >= v7
    ("ccsrftoken_443_3334d10", "token"),  # >= v7
    ("ccsrftokenother-name", ValueError),
    ("ccsrftoken-other-name", ValueError),
    ("other-name", ValueError),
])
def test__get_token_from_cookies(fgt: Fortigate, name, expected):
    """Fortigate._get_token_from_cookies()"""
    session: Session = create_session_w_cookie(name, "\"token\"")
    if isinstance(expected, str):
        actual = fgt._get_token_from_cookies(session=session)
        assert actual == expected
    else:
        with pytest.raises(expected):
            fgt._get_token_from_cookies(session=session)


@pytest.mark.parametrize("kwargs, url, expected", [
    ({}, QUERY, f"https://host/{QUERY}"),
    ({}, f"/{QUERY}/", f"https://host/{QUERY}"),
    ({}, f"https://host/{QUERY}", f"https://host/{QUERY}"),
    ({}, f"https://host/{QUERY}/", f"https://host/{QUERY}"),
    (dict(port=80), QUERY, f"https://host:80/{QUERY}"),
    (dict(port=80), f"https://host:80/{QUERY}", f"https://host:80/{QUERY}"),
    (dict(scheme="http", port=80), QUERY, f"http://host:80/{QUERY}"),
    (dict(scheme="http", port=80), f"http://host:80/{QUERY}", f"http://host:80/{QUERY}"),
])
def test__valid_url(kwargs, url, expected):
    """Fortigate._valid_url()"""
    default = dict(host="host", username="username", password="", port=443)
    kwargs_ = {**default, **kwargs}
    fgt = Fortigate(**kwargs_)

    actual = fgt._valid_url(url=url)
    assert actual == expected


@pytest.mark.parametrize("string, password, expected", [
    ("", "", ""),
    ("", "secret", ""),
    ("text", "", "text"),
    ("text", "secret", "text"),
    ("_secret_", "secret", "_<hidden>_"),
    ("_%5B_", "secret", "_%5B_"),
    ("_secret%5B_", "secret[", "_<hidden>_"),
])
def test__hide_secret(string, password, expected):
    """Fortigate._hide_secret()"""
    fgt = Fortigate(host="host", password=password)
    actual = fgt._hide_secret(string=string)
    assert actual == expected
