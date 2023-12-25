"""unittest fortigate.py"""
from unittest.mock import patch

import pytest
from pytest_mock import MockerFixture
from requests import Session

from fortigate_api import Fortigate, fortigate
from tests import helper__tst as tst

QUERY = "api/v2/cmdb/firewall/policy"


@pytest.fixture
def fgt():
    """Init Fortigate"""
    fgt_ = Fortigate(host="host")
    fgt_._session = Session()
    return fgt_


@pytest.mark.parametrize("kwargs, expected", [
    # username password
    (dict(host="a", username="b", password="c"),
     "Fortigate(host='a', username='b')"),
    (dict(host="a", username="b", password="c", scheme="https", port=443, timeout=15, vdom="root"),
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
])
def test__repr__(kwargs, expected):
    """Fortigate.__repr__()"""
    fgt = Fortigate(**kwargs)
    actual = f"{fgt!r}"
    assert actual == expected


def test__enter__(mocker: MockerFixture):
    """Fortigate.__enter__() Fortigate.__exit__()"""
    fgt = Fortigate(host="host")
    session = fgt._session
    assert session is None

    # __enter__
    session_m = mocker.Mock()
    mocker.patch("requests.Session.post", return_value=session_m)
    mocker.patch("requests.Session.get", return_value=tst.crate_response(200))
    with patch("fortigate_api.Fortigate._get_token_from_cookies", return_value="token"):
        with Fortigate(host="host") as fgt:
            session = fgt._session
            assert isinstance(session, Session) is True


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
    ("https://host/api/v2/cmdb/firewall/policy/2", 404),
    ("https://host/api/v2/cmdb/firewall/typo/1", 400),
])
def test__delete(fgt: Fortigate, mocker: MockerFixture, url, expected):
    """Fortigate.delete()"""
    mocker.patch("requests.Session.delete",
                 side_effect=lambda *args, **kw: tst.session_delete(mocker, *args, **kw))
    response = fgt.delete(url=url)
    actual = response.status_code
    assert actual == expected


@pytest.mark.parametrize("url, expected", [
    ("https://host/api/v2/cmdb/firewall/policy/1", [1]),
    ("https://host/api/v2/cmdb/firewall/policy/2", []),
    ("https://host/api/v2/cmdb/firewall/typo/1", []),
])
def test__get(fgt: Fortigate, mocker: MockerFixture, url, expected):
    """Fortigate.get()"""
    mocker.patch("requests.Session.get",
                 side_effect=lambda *args, **kw: tst.session_get(mocker, *args, **kw))
    result = fgt.get(url=url)
    actual = [d["policyid"] for d in result]
    assert actual == expected


@pytest.mark.parametrize("url, data, expected", [
    ("https://host/api/v2/cmdb/firewall/policy/1", {"name": "POL1"}, 500),
    ("https://host/api/v2/cmdb/firewall/policy/2", {"name": "POL2"}, 200),
    ("https://host/api/v2/cmdb/firewall/typo/2", {"name": "POL2"}, 400),
])
def test__post(fgt: Fortigate, mocker: MockerFixture, url, data, expected):
    """Fortigate.post()"""
    mocker.patch("requests.Session.post",
                 side_effect=lambda *args, **kw: tst.session_post(mocker, *args, **kw))
    response = fgt.post(url=url, data=data)
    actual = response.status_code
    assert actual == expected


@pytest.mark.parametrize("url, expected", [
    ("https://host/api/v2/cmdb/firewall/policy/1", 200),
    ("https://host/api/v2/cmdb/firewall/policy/2", 404),
    ("https://host/api/v2/cmdb/firewall/typo/1", 400),
])
def test__put(fgt: Fortigate, mocker: MockerFixture, url, expected):
    """Fortigate.put()"""
    mocker.patch("requests.Session.put",
                 side_effect=lambda *args, **kw: tst.session_put(mocker, *args, **kw))
    response = fgt.put(url=url, data={"name": "POL1"})
    actual = response.status_code
    assert actual == expected


@pytest.mark.parametrize("url, expected", [
    ("https://host/api/v2/cmdb/firewall/policy/1", 200),
    ("https://host/api/v2/cmdb/firewall/policy/3", 404),
    ("https://host/api/v2/cmdb/firewall/typo/1", 400),
])
def test__exist(fgt: Fortigate, mocker: MockerFixture, url, expected):
    """Fortigate.exist()"""
    mocker.patch("requests.Session.get",
                 side_effect=lambda *args, **kw: tst.session_get(mocker, *args, **kw))
    response = fgt.exist(url=url)
    actual = response.status_code
    assert actual == expected


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
    mocker.patch("requests.Session.post", return_value=mock_response)
    mocker.patch("requests.Session.get", return_value=tst.crate_response(200))
    with patch("fortigate_api.Fortigate._get_token_from_cookies", return_value="token"):
        session = fgt._get_session()
        assert isinstance(session, Session) is True


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
    session: Session = tst.create_session_w_cookie(name, "\"token\"")
    if isinstance(expected, str):
        actual = fgt._get_token_from_cookies(session=session)
        assert actual == expected
    else:
        with pytest.raises(expected):
            fgt._get_token_from_cookies(session=session)


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
def test__init_port(fgt: Fortigate, kwargs, scheme, expected):
    """Fortigate._init_port()"""
    fgt.scheme = scheme
    if isinstance(expected, int):
        actual = fgt._init_port(**kwargs)
        assert actual == expected
    else:
        with pytest.raises(expected):
            fgt._init_port(**kwargs)


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


@pytest.mark.parametrize("kwargs, expected", [
    ({}, "https"),
    (dict(scheme=""), "https"),
    (dict(scheme="https"), "https"),
    (dict(scheme="http"), "http"),
    (dict(scheme="ssh"), ValueError),
])
def test__init_scheme(kwargs, expected):
    """Fortigate._init_scheme()"""

    if isinstance(expected, str):
        actual = fortigate._init_scheme(**kwargs)
        assert actual == expected
    else:
        with pytest.raises(expected):
            fortigate._init_scheme(**kwargs)


@pytest.mark.parametrize("kwargs, expected", [
    ({}, ""),
    (dict(token="token"), "token"),
    (dict(token="token", username="username"), ValueError),
    (dict(token="token", password="password"), ValueError),
])
def test__init_token(kwargs, expected):
    """Fortigate._init_token()"""

    if isinstance(expected, str):
        actual = fortigate._init_token(**kwargs)
        assert actual == expected
    else:
        with pytest.raises(expected):
            fortigate._init_token(**kwargs)
