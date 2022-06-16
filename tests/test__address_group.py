"""unittest address_group.py"""

import unittest

from fortigate_api.address_group import AddressGroup
from tests.helper__tst import ADDGR1, NAME3, MockFortigate


# noinspection DuplicatedCode
class Test(MockFortigate):
    """unittest address_group.py"""

    def setUp(self):
        """setUp"""
        super().setUp()
        self.obj = AddressGroup(fgt=self.fgt)

    def test_valid__create(self):
        """AddressGroup.create()"""
        for name, req in [
            (ADDGR1, 200),  # present in the Fortigate, no need create
            ("ADDGR9", 500),  # error
            (NAME3, 200),  # absent in the Fortigate, need create
        ]:
            result = self.obj.create(data={"name": name}).status_code
            self.assertEqual(result, req, msg=f"{name=}")

    def test_valid__delete(self):
        """AddressGroup.delete()"""
        for kwargs, req in [
            (dict(uid=ADDGR1), 200),
            (dict(uid="ADDGR9"), 500),
            (dict(filter=f"name=={ADDGR1}"), 200),
            (dict(filter="name==ADDGR9"), 200),
        ]:
            result = self.obj.delete(**kwargs).status_code
            self.assertEqual(result, req, msg=f"{kwargs=}")

    def test_invalid__delete(self):
        """AddressGroup.delete()"""
        for kwargs, error in [
            (dict(uid=""), ValueError),
            (dict(uid=ADDGR1, filter=f"name=={ADDGR1}"), KeyError),
        ]:
            with self.assertRaises(error, msg=f"{kwargs=}"):
                self.obj.delete(**kwargs)

    def test_valid__get(self):
        """AddressGroup.get()"""
        for kwargs, req in [
            (dict(uid=ADDGR1), [ADDGR1]),
            (dict(uid="ADDGR9"), []),
            (dict(uid=ADDGR1, filter=f"name=={ADDGR1}"), [ADDGR1]),
            (dict(filter=f"name=={ADDGR1}"), [ADDGR1]),
            (dict(filter="name==ADDGR9"), []),
        ]:
            result_ = self.obj.get(**kwargs)
            result = [d["name"] for d in result_]
            self.assertEqual(result, req, msg=f"{kwargs=}")

    def test_invalid__get(self):
        """AddressGroup.get()"""
        for kwargs, error in [
            (dict(id=ADDGR1), KeyError),
        ]:
            with self.assertRaises(error, msg=f"{kwargs=}"):
                self.obj.get(**kwargs)

    def test_valid__update(self):
        """AddressGroup.update()"""
        for kwargs, req in [
            (dict(uid=ADDGR1, data=dict(name=ADDGR1)), 200),
            (dict(uid="ADDGR9", data=dict(name="ADDGR9")), 500),
            (dict(data=dict(name=ADDGR1)), 200),
            (dict(data=dict(name="ADDGR9")), 500),
        ]:
            result = self.obj.update(**kwargs).status_code
            self.assertEqual(result, req, msg=f"{kwargs=}")

    def test_valid__is_exist(self):
        """AddressGroup.is_exist()"""
        for uid, req in [
            (ADDGR1, True),
            ("ADDGR9", False),
        ]:
            result = self.obj.is_exist(uid=uid)
            self.assertEqual(result, req, msg=f"{uid=}")


if __name__ == "__main__":
    unittest.main()
