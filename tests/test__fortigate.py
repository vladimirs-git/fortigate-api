"""unittest firewall/fortigate.py"""

import unittest
from unittest.mock import patch

import requests

from fortigate_api.fortigate import Fortigate
from tests.helper__tst import NAME1, NAME2, NAME3, POL1, MockSession


class Test(unittest.TestCase):
    """unittest firewall/fortigate.py"""

    def setUp(self):
        """setUp"""
        patch.object(Fortigate, "_get_session", return_value=MockSession()).start()
        self.fgt = Fortigate(host="host", username="username", password="")
        self.url_policy = f"{self.fgt.url}/api/v2/cmdb/firewall/policy/"

    def test_valid__repr__(self):
        """Fortigate.__repr__()"""
        default = dict(scheme="https", port=443, timeout=15, vdom="root")
        for fgt, req in [
            (Fortigate(host="a", username="b", password="c"),
             "Fortigate(host='a', username='b', password='*')"),
            (Fortigate(host="a", username="b", password="c", **default),
             "Fortigate(host='a', username='b', password='*')"),
            (Fortigate(host="a", username="b", password="c", port=80),
             "Fortigate(host='a', username='b', password='*', port=80)"),
            (Fortigate(host="a", username="b", password="c", scheme="https", port=80),
             "Fortigate(host='a', username='b', password='*', port=80)"),
            (Fortigate(host="a", username="b", password="c", scheme="http", port=80),
             "Fortigate(host='a', username='b', password='*', scheme='http', port=80)"),
            (Fortigate(host="a", username="b", password="c", timeout=1),
             "Fortigate(host='a', username='b', password='*', timeout=1)"),
            (Fortigate(host="a", username="b", password="c", vdom="d"),
             "Fortigate(host='a', username='b', password='*', vdom='d')"),
            (Fortigate(host="a", username="b", password="c", vdom="d", timeout=1, port=80),
             "Fortigate(host='a', username='b', password='*', port=80, timeout=1, vdom='d')"),
        ]:
            result = f"{fgt!r}"
            self.assertEqual(result, req, msg=f"{fgt=}")

    def test_valid__init_scheme(self):
        """Fortigate._init_scheme()"""
        https = "https"
        for kwargs, req in [
            ({}, https),
            (dict(scheme=""), https),
            (dict(scheme="https"), https),
            (dict(scheme="http"), "http"),
        ]:
            result = self.fgt._init_scheme(**kwargs)
            self.assertEqual(result, req, msg=f"{kwargs=}")

    def test_invalid__init_scheme(self):
        """Fortigate._init_scheme()"""
        for kwargs, error in [
            (dict(scheme="ssh"), ValueError),
        ]:
            with self.assertRaises(error, msg=f"{kwargs=}"):
                self.fgt._init_scheme(**kwargs)

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
            self.fgt.scheme = scheme
            result = self.fgt._init_port(**kwargs)
            self.assertEqual(result, req, msg=f"{kwargs=}")

    def test_invalid__init_port(self):
        """Fortigate._init_port()"""
        for kwargs, error in [
            (dict(port="typo"), ValueError),
        ]:
            with self.assertRaises(error, msg=f"{kwargs=}"):
                self.fgt._init_port(**kwargs)

    def test_valid__url(self):
        """Fortigate._init_url()"""
        https, domain, ip_ = "https", "domain.com", "127.0.0.255"
        for scheme, host, port, req in [
            (https, domain, 1, f"https://{domain}:1"),
            (https, ip_, 1, f"https://{ip_}:1"),
            (https, domain, 443, f"https://{domain}"),
            (https, ip_, 443, f"https://{ip_}"),
        ]:
            self.fgt.scheme, self.fgt.host, self.fgt.port = scheme, host, port
            result = self.fgt.url
            self.assertEqual(result, req, msg=f"{host=} {port=}")

    def test_valid__delete(self):
        """Fortigate.delete()"""
        for policy_id, req in [
            (1, 200),
            (2, 500),
        ]:
            url = f"{self.url_policy}{policy_id}"
            result = self.fgt.delete(url=url).status_code
            self.assertEqual(result, req, msg=f"{policy_id=}")

    def test_valid__get(self):
        """Fortigate.get()"""
        for policy_id, req in [
            (1, [POL1]),
            (2, []),
        ]:
            url = f"{self.url_policy}{policy_id}"
            result_ = self.fgt.get(url=url)
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
            result = self.fgt.post(url=url, data={"name": name}).status_code
            self.assertEqual(result, req, msg=f"{name=}")

    def test_valid__put(self):
        """Fortigate.put()"""
        for policy_id, req in [
            (1, 200),
            (2, 500),
        ]:
            url = f"{self.url_policy}{policy_id}"
            result = self.fgt.put(url=url, data={"name": NAME1}).status_code
            self.assertEqual(result, req, msg=f"{policy_id=}")

    def test_valid__exist(self):
        """Fortigate.exist()"""
        for policy_id, req in [
            (1, 200),
            (2, 500),
        ]:
            policy_id = f"{self.url_policy}{policy_id}"
            result = self.fgt.exist(url=policy_id).status_code
            self.assertEqual(result, req, msg=f"{policy_id=}")

    def test_valid__get_session(self):
        """Fortigate._get_session()"""
        for session in [
            None,
            requests.session(),
        ]:
            result = self.fgt._get_session()
            self.assertEqual(result.__class__.__name__, "MockSession", msg=f"{session=}")

    def test_valid__hide_secret(self):
        """Fortigate._hide_secret()"""
        req = "_<hidden>_"
        for string, password in [
            ("_a_", "a"),
            ("_%5B_", "["),
        ]:
            self.fgt.password = password
            result = self.fgt._hide_secret(string=string)
            self.assertEqual(result, req, msg=f"{string=}, {password=}")

    def test_valid__valid_url(self):
        """Fortigate._valid_url()"""
        default = dict(host="host", username="username", password="", port=443)
        query = "api/v2/cmdb/firewall/address/"
        url_ = f"https://host/{query}"
        for kwargs, url, req in [
            ({}, query, url_),
            ({}, f"/{query}", url_),
            ({}, "api/v2/cmdb/firewall/address", url_),
            ({}, url_, url_),
            (dict(port=80), query, f"https://host:80/{query}"),
            (dict(port=80), f"https://host:80/{query}", f"https://host:80/{query}"),
            (dict(scheme="http", port=80), query, f"http://host:80/{query}"),
            (dict(scheme="http", port=80), f"http://host:80/{query}", f"http://host:80/{query}"),
        ]:
            kwargs_ = {**default, **kwargs}
            fgt = Fortigate(**kwargs_)
            result = fgt._valid_url(url=url)
            self.assertEqual(result, req, msg=f"{url=}")


if __name__ == "__main__":
    unittest.main()
