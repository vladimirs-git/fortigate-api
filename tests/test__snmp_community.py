"""unittest snmp_community.py"""

import unittest

from fortigate_api.snmp_community import SnmpCommunity
from tests.helper__tst import NAME1, NAME3, MockFortigate


# noinspection DuplicatedCode
class Test(MockFortigate):
    """unittest snmp_community.py"""

    def setUp(self):
        """setUp"""
        super().setUp()
        self.obj = SnmpCommunity(fgt=self.fgt)

    def test_valid__create(self):
        """SnmpCommunity.create()"""
        for name, req in [
            (NAME1, 200),  # present in the Fortigate, no need create
            ("NAME9", 500),  # error
            (NAME3, 200),  # absent in the Fortigate, need create
        ]:
            result = self.obj.create(data={"name": name}).status_code
            self.assertEqual(result, req, msg=f"{name=}")

    def test_valid__delete(self):
        """SnmpCommunity.delete()"""
        for kwargs, req in [
            (dict(uid="1"), 200),
            (dict(uid=1), 200),
            (dict(uid=9), 500),  # absent
            (dict(filter="id==1"), 200),
            (dict(filter="id==9"), 200),  # absent
            (dict(filter=f"name=={NAME1}"), 200),
            (dict(filter="name==NAME9"), 200),  # absent
        ]:
            result = self.obj.delete(**kwargs).status_code
            self.assertEqual(result, req, msg=f"{kwargs=}")

    def test_valid__get(self):
        """SnmpCommunity.get()"""
        for kwargs, req in [
            ({}, [NAME1, NAME3]),
            (dict(uid=1), [NAME1]),
            (dict(uid=9), []),  # absent
            (dict(uid=1, filter=f"name=={NAME1}"), [NAME1]),
            (dict(filter=f"name=={NAME1}"), [NAME1]),
            (dict(filter="name==POL9"), []),
        ]:
            result_ = self.obj.get(**kwargs)
            result = [d["name"] for d in result_]
            self.assertEqual(result, req, msg=f"{kwargs=}")

    def test_invalid__get(self):
        """Policy.get()"""
        for kwargs, error in [
            (dict(name=NAME1), KeyError),
        ]:
            with self.assertRaises(error, msg=f"{kwargs=}"):
                self.obj.get(**kwargs)

    def test_valid__update(self):
        """SnmpCommunity.update()"""
        for kwargs, req in [
            (dict(uid=NAME1, data=dict(name=NAME1)), 200),
            (dict(uid="NAME9", data=dict(name="NAME9")), 500),
        ]:
            result = self.obj.update(**kwargs).status_code
            self.assertEqual(result, req, msg=f"{kwargs=}")

    def test_valid__is_exist(self):
        """Address.is_exist()"""
        for uid, req in [
            (NAME1, True),
            ("NAME9", False),
        ]:
            result = self.obj.is_exist(uid=uid)
            self.assertEqual(result, req, msg=f"{uid=}")


if __name__ == "__main__":
    unittest.main()
