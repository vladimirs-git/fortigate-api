"""unittest address.py"""

import unittest

from fortigate_api.address import Address
from tests.helper__tst import ADDR1, NAME3, SLASH, MockFortigate


# noinspection DuplicatedCode
class Test(MockFortigate):
    """Address"""

    def setUp(self):
        """setUp"""
        super().setUp()
        self.obj = Address(rest=self.rest)

    def test_valid__create(self):
        """Address.create()"""
        for name, req in [
            (ADDR1, 200),  # present in the Fortigate, no need create
            ("ADDR9", 500),  # error
            (NAME3, 200),  # absent in the Fortigate, need create
            (SLASH, 200),  # name with slash, present in the Fortigate, no need create
        ]:
            result = self.obj.create(data={"name": name}).status_code
            self.assertEqual(result, req, msg=f"{name=}")

    def test_valid__delete(self):
        """Address.delete()"""
        for kwargs, req in [
            (dict(uid=ADDR1), 200),
            (dict(uid="ADDR9"), 500),
            (dict(filter=f"name=={ADDR1}"), 200),
            (dict(filter="name==ADDR9"), 200),
        ]:
            result = self.obj.delete(**kwargs).status_code
            self.assertEqual(result, req, msg=f"{kwargs=}")

    def test_invalid__delete(self):
        """Address.delete()"""
        for kwargs, error in [
            (dict(uid=""), ValueError),
            (dict(uid=ADDR1, filter=f"name=={ADDR1}"), KeyError),
        ]:
            with self.assertRaises(error, msg=f"{kwargs=}"):
                self.obj.delete(**kwargs)

    def test_valid__get(self):
        """Address.get()"""
        for kwargs, req in [
            (dict(uid=ADDR1), [ADDR1]),
            (dict(uid=SLASH), [SLASH]),
            (dict(uid="ADDR9"), []),
            (dict(uid=ADDR1, filter=f"name=={ADDR1}"), [ADDR1]),
            (dict(filter=f"name=={ADDR1}"), [ADDR1]),
            (dict(filter="name==ADDR9"), []),
        ]:
            result_ = self.obj.get(**kwargs)
            result = [d["name"] for d in result_]
            self.assertEqual(result, req, msg=f"{kwargs=}")

    def test_invalid__get(self):
        """Address.get()"""
        for kwargs, error in [
            (dict(id=ADDR1), KeyError),
        ]:
            with self.assertRaises(error, msg=f"{kwargs=}"):
                self.obj.get(**kwargs)

    def test_valid__update(self):
        """Address.update()"""
        for kwargs, req in [
            (dict(uid=ADDR1, data=dict(name=ADDR1)), 200),
            (dict(uid="ADDR9", data=dict(name="ADDR9")), 500),
            (dict(data=dict(name=ADDR1)), 200),
            (dict(data=dict(name="ADDR9")), 500),
        ]:
            result = self.obj.update(**kwargs).status_code
            self.assertEqual(result, req, msg=f"{kwargs=}")

    def test_valid__is_exist(self):
        """Address.is_exist()"""
        for uid, req in [
            (ADDR1, True),
            ("ADDR9", False),
        ]:
            result = self.obj.is_exist(uid=uid)
            self.assertEqual(result, req, msg=f"{uid=}")


if __name__ == "__main__":
    unittest.main()
