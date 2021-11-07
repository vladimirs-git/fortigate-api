"""unittest firewall/fortigate.py"""

from __future__ import annotations

import unittest
from unittest.mock import patch

import requests  # type: ignore

from fortigate_api.fortigate import Fortigate
from tests.helper__tst import NAME1, NAME2, NAME3
from tests.mock_session import MockSession


class Test(unittest.TestCase):
    """unittest firewall/fortigate.py"""

    def setUp(self):
        patch.object(Fortigate, "login", return_value=MockSession()).start()
        self.fgt = Fortigate(host="", username="", password="")
        self.url_policy = f"{self.fgt.url}/api/v2/cmdb/firewall/policy/"

    def test_valid__port(self):
        """Fortigate._port()"""
        for port, req_port in [
            ("", 443),
            (443, 443),
            ("443", 443),
        ]:
            result = self.fgt._port(port=port)
            self.assertEqual(result, req_port, msg=f"{port=}")

    def test_invalid__port(self):
        """Fortigate._port()"""
        for port in [
            "port=443",
            dict(port=443),
        ]:
            with self.assertRaises(ValueError, msg=f"{port=}"):
                self.fgt._port(port=port)

    def test_valid__timeout(self):
        """Fortigate._timeout()"""
        for timeout, req_timeout in [
            ("", 15),
            (1, 1),
            ("1", 1),
        ]:
            result = self.fgt._timeout(timeout=timeout)
            self.assertEqual(result, req_timeout, msg=f"{timeout=}")

    def test_invalid__timeout(self):
        """Fortigate._timeout()"""
        for timeout in [
            "timeout=10",
            dict(timeout=10),
        ]:
            with self.assertRaises(ValueError, msg=f"{timeout=}"):
                self.fgt._timeout(timeout=timeout)

    def test_valid__vdom(self):
        """Fortigate._vdom()"""
        for kwargs, req_vdom in [
            ({"vdom": ""}, "root"),
            ({"vdom": None}, "root"),
            ({"vdom": "name"}, "name"),
        ]:
            result = self.fgt._vdom(**kwargs)
            self.assertEqual(result, req_vdom, msg=f"{kwargs=}")

    def test_invalid__vdom(self):
        """Fortigate._vdom()"""
        for kwargs in [
            {"vdom": {"vdom": "name"}},
        ]:
            with self.assertRaises(ValueError, msg=f"{kwargs=}"):
                self.fgt._vdom(**kwargs)

    def test_valid__url(self):
        """Fortigate._init_url()"""
        domain, ip_ = "domain.com", "127.0.0.255"
        for host, port, req_url in [
            (domain, 1, f"https://{domain}:1"),
            (ip_, 1, f"https://{ip_}:1"),
            (domain, 443, f"https://{domain}"),
            (ip_, 443, f"https://{ip_}"),
        ]:
            self.fgt.host, self.fgt.port = host, port
            result = self.fgt.url
            self.assertEqual(result, req_url, msg=f"{host=} {port=}")

    def test_valid__delete(self):
        """Fortigate.delete()"""
        for policy_id, req_status in [
            (1, 200),
            (2, 500),
        ]:
            url = f"{self.url_policy}{policy_id}"
            result = self.fgt.delete(url=url)
            self.assertEqual(result.status_code, req_status, msg=f"{policy_id=}")

    def test_valid__get(self):
        """Fortigate.get()"""
        for policy_id, req_data in [
            (1, [{"name": NAME1}]),
            (2, []),
        ]:
            url = f"{self.url_policy}{policy_id}"
            result = self.fgt.get(url=url)
            self.assertEqual(result, req_data, msg=f"{policy_id=}")

    def test_valid__post(self):
        """Fortigate.post()"""
        for name, req_status in [
            (NAME1, 200),
            (NAME2, 500),
            (NAME3, 200),
        ]:
            url = f"{self.url_policy}"
            result = self.fgt.post(url=url, data={"name": name})
            self.assertEqual(result.status_code, req_status, msg=f"{name=}")

    def test_valid__put(self):
        """Fortigate.put()"""
        for policy_id, req_status in [
            (1, 200),
            (2, 500),
        ]:
            url = f"{self.url_policy}{policy_id}"
            result = self.fgt.put(url=url, data={"name": NAME1})
            self.assertEqual(result.status_code, req_status, msg=f"{policy_id=}")

    def test_valid__exist(self):
        """Fortigate.exist()"""
        for policy_id, req_status in [
            (1, 200),
            (2, 500),
        ]:
            policy_id = f"{self.url_policy}{policy_id}"
            result = self.fgt.exist(url=policy_id)
            self.assertEqual(result.status_code, req_status, msg=f"{policy_id=}")

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
        req_hidden = "_<hidden>_"
        for string, password in [
            ("_a_", "a"),
            ("_%5B_", "["),
        ]:
            self.fgt.password = password
            result = self.fgt._hide_secret(string=string)
            self.assertEqual(result, req_hidden, msg=f"{string=}, {password=}")


if __name__ == "__main__":
    unittest.main()
