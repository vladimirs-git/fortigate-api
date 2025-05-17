"""Test fortigate_base.py"""
from collections import OrderedDict
from unittest.mock import patch

import pytest
import requests_mock
from pytest_mock import MockerFixture
from requests import Session

from fortigate_api import fortigate_base
from fortigate_api.fortigate import FortiGate
from tests import helpers__tst as tst

QUERY = "api/v2/cmdb/firewall/policy"


@pytest.fixture
def api() -> FortiGate:
    """Init FortiGate."""
    return FortiGate(host="host")


@pytest.mark.parametrize("kwargs, expected", [
    # username password
    (dict(host="a", username="b", password="c"),
     "FortiGate(host='a', username='b')"),
    (dict(host="a", username="b", password="c", scheme="https", port=443, timeout=15, vdom="root"),
     "FortiGate(host='a', username='b')"),
    (dict(host="a", username="b", password="c", port=80),
     "FortiGate(host='a', username='b', port=80)"),
    (dict(host="a", username="b", password="c", scheme="https", port=80),
     "FortiGate(host='a', username='b', port=80)"),
    (dict(host="a", username="b", password="c", scheme="http", port=80),
     "FortiGate(host='a', username='b', scheme='http', port=80)"),
    (dict(host="a", username="b", password="c", timeout=1),
     "FortiGate(host='a', username='b', timeout=1)"),
    (dict(host="a", username="b", password="c", vdom="d"),
     "FortiGate(host='a', username='b', vdom='d')"),
    (dict(host="a", username="b", password="c", vdom="d", timeout=1, port=80),
     "FortiGate(host='a', username='b', port=80, timeout=1, vdom='d')"),
    (dict(host="a", username="b", password="c", verify=True),
     "FortiGate(host='a', username='b', verify=True)"),
    (dict(host="a", username="b", password="c", verify=False),
     "FortiGate(host='a', username='b')"),
    # token
    (dict(host="a", token="b"), "FortiGate(host='a', username='')"),
])
def test__repr__(kwargs, expected):
    """FortiGateBase.__repr__()"""
    fgt = FortiGate(**kwargs)
    actual = f"{fgt!r}"
    assert actual == expected


def test__enter__(mocker: MockerFixture):
    """FortiGateBase.__enter__() FortiGateBase.__exit__()"""
    fgt = FortiGate(host="host")
    session = fgt._session
    assert session is None

    # __enter__
    session_m = mocker.Mock()
    mocker.patch(target="requests.Session.post", return_value=session_m)
    mocker.patch(target="requests.Session.get", return_value=tst.crate_response(200))
    with patch("fortigate_api.FortiGate._get_token_from_cookies", return_value="TOKEN"):
        with FortiGate(host="host") as fgt:
            session = fgt._session
            assert isinstance(session, Session) is True


# =========================== property ===========================

@pytest.mark.parametrize("session, expected", [
    (None, False),
    (Session(), True),
])
def test__is_connected(api: FortiGate, session, expected):
    """FortiGateBase.is_connected()"""
    api._session = session
    actual = api.is_connected
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
    """FortiGateBase.url()"""
    fgt = FortiGate(host=host, scheme=scheme, port=port)
    actual = fgt.url
    assert actual == expected


# ============================ login =============================

# noinspection PyUnresolvedReferences
@pytest.mark.parametrize("token, expected, headers", [
    ("", "TOKEN", ("X-CSRFTOKEN", "TOKEN")),
    ("TOKEN", "", None),
])
def test__login(token, expected, headers):
    """FortiGateBase.login() for username."""
    api = FortiGate(host="HOST", token=token)
    with requests_mock.Mocker() as mock:
        if token:
            mock.get("https://host/api/v2/monitor/system/status")
        else:
            mock.post("https://host/logincheck")

        with patch("fortigate_api.FortiGate._get_token_from_cookies", return_value=expected):
            api.login()
            assert isinstance(api._session, Session)
            store: OrderedDict = getattr(api._session.headers, "_store")
            actual = store.get("x-csrftoken")
            assert actual == headers


# =========================== helpers ============================

@pytest.mark.parametrize("session, expected", [
    (Session(), True),
    (None, TypeError),
])
def test__get_session(api: FortiGate, session, expected):
    """FortiGateBase.get_session()"""
    api._session = session

    if isinstance(expected, bool):
        session = api.get_session()
        assert isinstance(session, Session)

    else:
        with pytest.raises(expected):
            with patch.object(FortiGate, "login", return_value=None):
                api.get_session()


@pytest.mark.parametrize("name, expected", [
    ("ccsrftoken", "token"),  # < v7
    ("ccsrftoken_443", "token"),  # >= v7
    ("ccsrftoken_443_3334d10", "token"),  # >= v7
    ("other-name", ValueError),
])
def test__get_token_from_cookies(api: FortiGate, name, expected):
    """FortiGateBase._get_token_from_cookies()"""
    session: Session = tst.create_session_w_cookie(name, "\"token\"")
    if isinstance(expected, str):
        actual = api._get_token_from_cookies(session=session)
        assert actual == expected
    else:
        with pytest.raises(expected):
            api._get_token_from_cookies(session=session)


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
    """FortiGateBase._hide_secret()"""
    fgt = FortiGate(host="host", password=password)
    actual = fgt._hide_secret(string=string)
    assert actual == expected


@pytest.mark.parametrize("kwargs, scheme, expected", [
    ({}, "https", 443),
    ({}, "http", 80),
    (dict(port=""), "https", 443),
    (dict(port=""), "http", 80),
    (dict(port=0), "https", 443),
    (dict(port=0), "http", 80),
    (dict(port="0"), "https", 443),
    (dict(port="0"), "http", 80),
    (dict(port=1), "https", 1),
    (dict(port="1"), "http", 1),
    (dict(port="typo"), "https", ValueError),
    (dict(port="typo"), "http", ValueError),
])
def test__init_port(api: FortiGate, kwargs, scheme, expected):
    """FortiGateBase._init_port()"""
    api.scheme = scheme
    if isinstance(expected, int):
        actual = api._init_port(**kwargs)
        assert actual == expected
    else:
        with pytest.raises(expected):
            api._init_port(**kwargs)


@pytest.mark.parametrize("kwargs, url, expected", [
    ({}, QUERY, f"https://host/{QUERY}"),
    ({}, f"/{QUERY}/", f"https://host/{QUERY}"),
    ({}, f"https://host/{QUERY}", f"https://host/{QUERY}"),
    ({}, f"https://host/{QUERY}/", f"https://host/{QUERY}"),
    ({"port": 80}, QUERY, f"https://host:80/{QUERY}"),
    ({"port": 80}, f"https://host:80/{QUERY}", f"https://host:80/{QUERY}"),
    ({"scheme": "http", "port": 80}, QUERY, f"http://host/{QUERY}"),
    ({"scheme": "http", "port": 80}, f"http://host/{QUERY}", f"http://host/{QUERY}"),
])
def test__valid_url(kwargs, url, expected):
    """FortiGateBase._valid_url()"""
    default = dict(host="host", username="username", password="", port=443)
    kwargs_ = {**default, **kwargs}
    fgt = FortiGate(**kwargs_)

    actual = fgt._valid_url(url=url)
    assert actual == expected


# =========================== helpers ============================

@pytest.mark.parametrize("kwargs, expected", [
    ({}, "https"),
    (dict(scheme=""), "https"),
    (dict(scheme="https"), "https"),
    (dict(scheme="http"), "http"),
    (dict(scheme="ssh"), ValueError),
])
def test__init_scheme(kwargs, expected):
    """fortigate_base._init_scheme()"""

    if isinstance(expected, str):
        actual = fortigate_base._init_scheme(**kwargs)
        assert actual == expected
    else:
        with pytest.raises(expected):
            fortigate_base._init_scheme(**kwargs)


@pytest.mark.parametrize("kwargs, expected", [
    ({}, ""),
    (dict(token="token"), "token"),
    (dict(token="token", username="username"), ValueError),
    (dict(token="token", password="password"), ValueError),
])
def test__init_token(kwargs, expected):
    """fortigate_base._init_token()"""

    if isinstance(expected, str):
        actual = fortigate_base._init_token(**kwargs)
        assert actual == expected
    else:
        with pytest.raises(expected):
            fortigate_base._init_token(**kwargs)
