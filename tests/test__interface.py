"""unittest interface.py"""

import unittest

from fortigate_api.interface import Interface
from tests.helper__tst import NAME1, NAME2, NAME3, MockFortigate


# noinspection DuplicatedCode
class Test(MockFortigate):
    """Interface"""

    def setUp(self):
        """setUp"""
        super().setUp()
        self.obj = Interface(rest=self.rest)

    def test_valid__create(self):
        """Interface.create()"""
        for name, req in [
            (NAME1, 200),  # present in the Fortigate, no need create
            (NAME2, 500),  # error
            (NAME3, 200),  # not found in the Fortigate, need create
        ]:
            result = self.obj.create(data={"name": name}).status_code
            self.assertEqual(result, req, msg=f"{name=}")

    def test_valid__delete(self):
        """Interface.delete()"""
        for kwargs, req in [
            (dict(uid=NAME1), 200),
            (dict(uid=NAME2), 500),
            (dict(filter=f"name=={NAME1}"), 200),
            (dict(filter=f"name=={NAME2}"), 200),
        ]:
            result = self.obj.delete(**kwargs).status_code
            self.assertEqual(result, req, msg=f"{kwargs=}")

    def test_valid__get(self):
        """Interface.get()"""
        for kwargs, req in [
            (dict(uid=NAME1), [NAME1]),
            (dict(uid=NAME2), []),
            (dict(uid=NAME3), []),  # vdom3
            (dict(filter=f"name=={NAME1}"), [NAME1]),
            (dict(filter=f"name=={NAME2}"), []),
            (dict(filter=f"name=={NAME3}"), []),  # vdom3
            (dict(all=True), [NAME1, NAME3]),
            (dict(all=True, uid=NAME1), [NAME1]),
            (dict(all=True, uid=NAME2), []),
            (dict(all=True, uid=NAME3), [NAME3]),
            (dict(all=True, filter=f"name=={NAME1}"), [NAME1]),
            (dict(all=True, filter=f"name=={NAME2}"), []),
            (dict(all=True, filter=f"name=={NAME3}"), [NAME3]),
        ]:
            result_ = self.obj.get(**kwargs)
            result = [d["name"] for d in result_]
            self.assertEqual(result, req, msg=f"{kwargs=}")

    def test_invalid__get(self):
        """Interface.get()"""
        for kwargs, error in [
            (dict(name=NAME1), KeyError),
        ]:
            with self.assertRaises(error, msg=f"{kwargs=}"):
                self.obj.get(**kwargs)

    def test_valid__update(self):
        """Interface.update()"""
        for kwargs, req in [
            (dict(uid=NAME1, data=dict(name=NAME1)), 200),
            (dict(uid="NAME9", data=dict(name="NAME9")), 500),
            (dict(data=dict(name=NAME1)), 200),
            (dict(data=dict(name="NAME9")), 500),
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
