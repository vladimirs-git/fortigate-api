"""unittest objects/policy.py"""

from __future__ import annotations

import unittest

from fortigate_api.policy import Policy
from tests.helper__tst import NAME1, NAME2, NAME3
from tests.mock_fortigate import MockFortigate


class Test(MockFortigate):
    """unittest objects/policy.py"""

    def setUp(self):
        super().setUp()
        self.obj = Policy(fgt=self.fgt)

    def test_valid__create(self):
        """Policy.create()"""
        for name, req_status in [
            (NAME1, 200),  # present on Fortigate, no need create
            (NAME2, 500),  # error
            (NAME3, 200),  # absent on Fortigate, need create
        ]:
            result = self.obj.create(data={"name": name})
            self.assertEqual(result.status_code, req_status, msg=f"{name=}")

    def test_valid__delete(self):
        """Policy.delete()"""
        for id_, req_status in [
            ("1", 200),
            (1, 200),
            (2, 500),
        ]:
            result = self.obj.delete(policyid=id_)
            self.assertEqual(result.status_code, req_status, msg=f"{id_=}")

    def test_valid__delete_name(self):
        """Policy.delete()"""
        for name, req_status in [
            (NAME1, [200]),
            (NAME2, []),
        ]:
            result = self.obj.delete_name(name=name)
            statuses = [o.status_code for o in result]
            self.assertEqual(statuses, req_status, msg=f"{name=}")

    def test_valid__get(self):
        """Policy.get()"""
        for kwargs, req_names in [
            ({"id": 1}, [NAME1]),
            ({"id": 2}, []),
            ({"name": NAME1}, [NAME1]),
            ({"name": NAME2}, []),
        ]:
            result = self.obj.get(**kwargs)
            names = [d["name"] for d in result]
            self.assertEqual(names, req_names, msg=f"{kwargs=}")

    def test_valid__update(self):
        """Policy.update()"""
        for data, req_status in [
            ({"name": NAME1, "policyid": 1}, 200),
            ({"name": NAME2, "policyid": 2}, 500),
        ]:
            result = self.obj.update(data=data)
            self.assertEqual(result.status_code, req_status, msg=f"{data=}")

    def test_valid__move(self):
        """Policy.move()"""
        for id_, position, neighbor, req_status in [
            (1, "before", 2, 200),
            (2, "before", 1, 500),
        ]:
            result = self.obj.move(policyid=id_, position=position, neighbor=neighbor)
            self.assertEqual(result.status_code, req_status, msg=f"{id_=} {position=} {neighbor=}")


if __name__ == "__main__":
    unittest.main()
