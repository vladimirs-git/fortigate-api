"""unittest snmp_community.py"""

import unittest

from fortigate_api.objects.snmp_community import SnmpCommunity
from tests.helper__tst import NAME1, NAME2, NAME3, MockFortigate


class Test(MockFortigate):
    """unittest snmp_community.py"""

    def setUp(self):
        """setUp"""
        super().setUp()
        self.obj = SnmpCommunity(fgt=self.fgt)

    def test_valid__create(self):
        """SnmpCommunity.create()"""
        for name, req_status in [
            (NAME1, 200),  # present in the Fortigate, no need create
            (NAME2, 500),  # error
            (NAME3, 200),  # absent in the Fortigate, need create
        ]:
            result = self.obj.create(data={"name": name})
            self.assertEqual(result.status_code, req_status, msg=f"{name=}")

    def test_valid__delete(self):
        """SnmpCommunity.delete()"""
        for id_, req_status in [
            ("1", 200),
            (1, 200),
            (2, 500),
        ]:
            result = self.obj.delete(id=id_)
            self.assertEqual(result.status_code, req_status, msg=f"{id_=}")

    def test_valid__delete_name(self):
        """SnmpCommunity.delete()"""
        for name, req_status in [
            (NAME1, [200]),
            (NAME2, []),
        ]:
            result = self.obj.delete_name(name=name)
            statuses = [o.status_code for o in result]
            self.assertEqual(statuses, req_status, msg=f"{name=}")

    def test_valid__get(self):
        """SnmpCommunity.get()"""
        for kwargs, req_names in [
            ({"name": NAME1}, [NAME1]),
            ({"name": NAME2}, []),
            ({"id": 1}, [NAME1]),
            ({"id": 2}, []),
        ]:
            result = self.obj.get(**kwargs)
            names = [d["name"] for d in result]
            self.assertEqual(names, req_names, msg=f"{kwargs=}")

    def test_valid__update(self):
        """SnmpCommunity.update()"""
        for data, req_status in [
            ({"name": NAME1, "id": 1}, 200),
            ({"name": NAME2, "id": 2}, 500),
        ]:
            result = self.obj.update(data=data)
            self.assertEqual(result.status_code, req_status, msg=f"{data=}")


if __name__ == "__main__":
    unittest.main()
