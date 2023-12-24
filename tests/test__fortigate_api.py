"""unittest fortigate_api.py"""
import unittest
from unittest.mock import patch

import pytest

from fortigate_api import FortigateAPI, Fortigate
from tests.helper__tst import MockSession


@pytest.fixture
def api():
    """Init FortigateAPI."""
    return FortigateAPI(host="host")


class Test(unittest.TestCase):
    """FortigateAPI"""

    def setUp(self):
        """setUp"""
        patch.object(Fortigate, "_get_session", return_value=MockSession()).start()
        self.rest = Fortigate(host="host", username="username", password="")
        self.url_policy = f"{self.rest.url}/api/v2/cmdb/firewall/policy/"

    def test_valid__enter__(self):
        """FortigateAPI.__enter__() Fortigate.__exit__()"""
        with patch("requests.session", return_value=MockSession()):
            with FortigateAPI(host="host", username="username", password="") as api:
                session = api.rest._session
                if session is not None:
                    result = session.__class__.__name__
                    req = "MockSession"
                    self.assertEqual(result, req, msg="MockSession")


if __name__ == "__main__":
    unittest.main()
