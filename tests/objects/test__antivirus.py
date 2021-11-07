"""unittest objects/antivirus.py"""

from __future__ import annotations

import unittest

from fortigate_api.antivirus import Antivirus
from tests.helper__tst import NAME1, NAME2, NAME3
from tests.mock_fortigate import MockFortigate


class Test(MockFortigate):
    """unittest objects/antivirus.py"""

    def setUp(self):
        super().setUp()
        self.obj = Antivirus(fgt=self.fgt)

    def test_valid__create(self):
        """Antivirus.create()"""
        for name, req_status in [
            (NAME1, 200),  # present on Fortigate, no need create
            (NAME2, 500),  # error
            (NAME3, 200),  # absent on Fortigate, need create
        ]:
            result = self.obj.create(data={"name": name})
            self.assertEqual(result.status_code, req_status, msg=f"{name=}")

    def test_valid__delete(self):
        """Antivirus.delete()"""
        for name, req_status in [
            (NAME1, 200),
            (NAME2, 500),
        ]:
            result = self.obj.delete(name=name)
            self.assertEqual(result.status_code, req_status, msg=f"{name=}")

    def test_valid__get(self):
        """Antivirus.get()"""
        for name, req_names in [
            (NAME1, [NAME1]),
            (NAME2, []),
        ]:
            result = self.obj.get(name=name)
            names = [d["name"] for d in result]
            self.assertEqual(names, req_names, msg=f"{name=}")

    def test_valid__update(self):
        """Antivirus.update()"""
        for name, req_status in [
            (NAME1, 200),
            (NAME2, 500),
        ]:
            result = self.obj.update(data={"name": name})
            self.assertEqual(result.status_code, req_status, msg=f"{name=}")


if __name__ == "__main__":
    unittest.main()
