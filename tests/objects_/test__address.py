"""unittest address.py"""

import unittest

from fortigate_api.objects.address import Address
from tests.helper__tst import NAME1, NAME2, NAME3, SLASH, MockFortigate


class Test(MockFortigate):
    """unittest address.py"""

    def setUp(self):
        """setUp"""
        super().setUp()
        self.obj = Address(fgt=self.fgt)

    def test_valid__create(self):
        """Address.create()"""
        for name, req_status in [
            (NAME1, 200),  # present in the Fortigate, no need create
            (NAME2, 500),  # error
            (NAME3, 200),  # absent in the Fortigate, need create
            (SLASH, 200),  # name with slash, present in the Fortigate, no need create
        ]:
            result = self.obj.create(data={"name": name})
            self.assertEqual(result.status_code, req_status, msg=f"{name=}")

    def test_valid__delete(self):
        """Address.delete()"""
        for name, req_status in [
            (NAME1, 200),
            (NAME2, 500),
        ]:
            result = self.obj.delete(name=name)
            self.assertEqual(result.status_code, req_status, msg=f"{name=}")

    def test_valid__get(self):
        """Address.get()"""
        for kwargs, req_names in [
            (dict(name=NAME1), [NAME1]),
            (dict(name=NAME2), []),
            (dict(filter=f"name=={NAME1}"), [NAME1]),
            (dict(filter=f"name=={NAME2}"), []),
        ]:
            result = self.obj.get(**kwargs)
            names = [d["name"] for d in result]
            self.assertEqual(names, req_names, msg=f"{kwargs=}")

    def test_valid__update(self):
        """Address.update()"""
        for name, req_status in [
            (NAME1, 200),
            (NAME2, 500),
        ]:
            result = self.obj.update(data={"name": name})
            self.assertEqual(result.status_code, req_status, msg=f"{name=}")

    def test_valid__is_exist(self):
        """Address.is_exist()"""
        for name, req in [
            (NAME1, True),
            (NAME2, False),
        ]:
            result = self.obj.is_exist(name=name)
            self.assertEqual(result, req, msg=f"{name=}")


if __name__ == "__main__":
    unittest.main()
