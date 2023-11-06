"""unittest fortigate.py"""

import unittest
from unittest.mock import Mock
from unittest.mock import patch

import requests

from fortigate_api import Fortigate
from tests.helper__tst import NAME1, NAME2, NAME3, POL1, MockSession


class MockCookie:
    """Mock Cookie."""

    def __init__(self, name: str, value: str):
        """Init Cookie."""
        self.name = name
        self.value = value


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

    def test_valid__is_connected(self):
        """Fortigate.is_connected()"""
        for session, req in [
            (requests.session(), True),
            (None, False),
        ]:
            self.rest._session = session
            result = self.rest.is_connected
            self.assertEqual(result, req, msg=f"{session=}")

    def test_valid__url(self):
        """Fortigate._init_url()"""
        https, domain, ip_ = "https", "domain.com", "127.0.0.255"
        for scheme, host, port, req in [
            (https, domain, 1, f"https://{domain}:1"),
            (https, ip_, 1, f"https://{ip_}:1"),
            (https, domain, 443, f"https://{domain}"),
            (https, ip_, 443, f"https://{ip_}"),
        ]:
            self.rest.scheme, self.rest.host, self.rest.port = scheme, host, port
            result = self.rest.url
            self.assertEqual(result, req, msg=f"{host=} {port=}")

    # =========================== methods ============================

    def test_valid__delete(self):
        """Fortigate.delete()"""
        for policy_id, req in [
            (1, 200),
            (2, 500),
        ]:
            url = f"{self.url_policy}{policy_id}"
            result = self.rest.delete(url=url).status_code
            self.assertEqual(result, req, msg=f"{policy_id=}")

    def test_valid__get(self):
        """Fortigate.get()"""
        for policy_id, req in [
            (1, [POL1]),
            (2, []),
        ]:
            url = f"{self.url_policy}{policy_id}"
            result_ = self.rest.get(url=url)
            result = [d["name"] for d in result_]
            self.assertEqual(result, req, msg=f"{policy_id=}")

    def test_valid__post(self):
        """Fortigate.post()"""
        for name, req in [
            (NAME1, 500),
            (NAME2, 500),
            (NAME3, 200),
        ]:
            url = f"{self.url_policy}"
            result = self.rest.post(url=url, data={"name": name}).status_code
            self.assertEqual(result, req, msg=f"{name=}")

    def test_valid__put(self):
        """Fortigate.put()"""
        for policy_id, req in [
            (1, 200),
            (2, 500),
        ]:
            url = f"{self.url_policy}{policy_id}"
            result = self.rest.put(url=url, data={"name": NAME1}).status_code
            self.assertEqual(result, req, msg=f"{policy_id=}")

    def test_valid__exist(self):
        """Fortigate.exist()"""
        for policy_id, req in [
            (1, 200),
            (2, 500),
        ]:
            policy_id = f"{self.url_policy}{policy_id}"
            result = self.rest.exist(url=policy_id).status_code
            self.assertEqual(result, req, msg=f"{policy_id=}")

    def test_valid__get_session(self):
        """Fortigate._get_session()"""
        for session in [
            None,
            requests.session(),
        ]:
            result = self.rest._get_session()
            self.assertEqual(result.__class__.__name__, "MockSession", msg=f"{session=}")

    def test_valid__hide_secret(self):
        """Fortigate._hide_secret()"""
        req = "_<hidden>_"
        for string, password in [
            ("_a_", "a"),
            ("_%5B_", "["),
        ]:
            self.rest.password = password
            result = self.rest._hide_secret(string=string)
            self.assertEqual(result, req, msg=f"{string=}, {password=}")

    def test_valid__valid_url(self):
        """Fortigate._valid_url()"""
        default = dict(host="host", username="username", password="", port=443)
        query = "api/v2/cmdb/firewall/address"
        full_url = f"https://host/{query}"
        https_80 = "https://host:80/"
        http_80 = "http://host:80/"
        for kwargs, url, req in [
            ({}, query, full_url),
            ({}, f"/{query}/", full_url),
            ({}, full_url, full_url),
            ({}, f"{full_url}/", full_url),
            (dict(port=80), query, f"{https_80}{query}"),
            (dict(port=80), f"{https_80}{query}", f"{https_80}{query}"),
            (dict(scheme="http", port=80), query, f"{http_80}{query}"),
            (dict(scheme="http", port=80), f"{http_80}{query}", f"{http_80}{query}"),
        ]:
            kwargs_ = {**default, **kwargs}
            fgt = Fortigate(**kwargs_)
            result = fgt._valid_url(url=url)
            self.assertEqual(result, req, msg=f"{url=}")

    # =========================== helpers ============================

    def test_valid__get_token_from_cookies(self):
        """Fortigate._get_token_from_cookies()"""
        for name, value, req_token in [
            ("ccsrftoken", "\"token\"", "token"),
            ("ccsrftoken_443", "\"token\"", "token"),
            ("ccsrftoken_443_3334d10", "\"token\"", "token"),
        ]:
            session = Mock()
            session.cookies = [MockCookie(name=name, value=value)]
            token = self.rest._get_token_from_cookies(session)
            self.assertEqual(token, req_token)

    def test_invalid__get_token_from_cookies(self):
        """Fortigate._get_token_from_cookies()"""
        for name, error in [
            ("ccsrftokenother-name", ValueError),
            ("ccsrftoken-other-name", ValueError),
            ("other-name", ValueError),
        ]:
            session = Mock()
            session.cookies = [MockCookie(name=name, value="\"token\"")]
            with self.assertRaises(error):
                self.rest._get_token_from_cookies(session)


if __name__ == "__main__":
    unittest.main()
