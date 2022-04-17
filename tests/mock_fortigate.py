"""mocked Fortigate"""

import unittest
from unittest.mock import patch

from fortigate_api.fortigate import Fortigate
from tests.mock_session import MockSession


class MockFortigate(unittest.TestCase):
    """mocked Fortigate"""

    def setUp(self):
        patch.object(Fortigate, "login", return_value=MockSession()).start()
        self.fgt = Fortigate(host="", username="", password="")
