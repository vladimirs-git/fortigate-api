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
        patch.object(Fortigate, "login", return_value=MockSession()).start()
        self.fgt = Fortigate(host="host", username="username", password="")
        self.url_policy = f"{self.fgt.url}/api/v2/cmdb/firewall/policy/"

    def test_valid__url(self):
        """Fortigate._init_url()"""
        domain, ip_ = "domain.com", "127.0.0.255"
        for host, port, req in [
            (domain, 1, f"https://{domain}:1"),
            (ip_, 1, f"https://{ip_}:1"),
            (domain, 443, f"https://{domain}"),
            (ip_, 443, f"https://{ip_}"),
        ]:
            self.fgt.host, self.fgt.port = host, port
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
        for kwargs, url, req in [
            (dict(host="host", username="username", password="", port=443),
             "api/v2/cmdb/firewall/address/",
             "https://host/api/v2/cmdb/firewall/address/"),
            (dict(host="host", username="username", password="", port=444),
             "api/v2/cmdb/firewall/address/",
             "https://host:444/api/v2/cmdb/firewall/address/"),
            (dict(host="host", username="username", password="", port=443),
             "https://host/api/v2/cmdb/firewall/address/",
             "https://host/api/v2/cmdb/firewall/address/"),
            (dict(host="host", username="username", password="", port=444),
             "https://host:444/api/v2/cmdb/firewall/address/",
             "https://host:444/api/v2/cmdb/firewall/address/"),

        ]:
            fgt = Fortigate(**kwargs)
            result = fgt._valid_url(url=url)
            self.assertEqual(result, req, msg=f"{url=}")


if __name__ == "__main__":
    unittest.main()
