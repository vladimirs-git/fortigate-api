"""unittest virtual_ip.py"""

import unittest

from fortigate_api.objects.virtual_ip import VirtualIP
from tests.helper__tst import NAME1, NAME2, NAME3, MockFortigate


class Test(MockFortigate):
    """unittest virtual_ip.py"""

    def setUp(self):
        """setUp"""
        super().setUp()
        self.obj = VirtualIP(fgt=self.fgt)

    def test_valid__create(self):
        """VirtualIp.create()"""
        for name, req_status in [
            (NAME1, 200),  # present in the Fortigate, no need create
            (NAME2, 500),  # error
            (NAME3, 200),  # absent in the Fortigate, need create
        ]:
            result = self.obj.create(data={"name": name})
            self.assertEqual(result.status_code, req_status, msg=f"{name=}")

    def test_valid__delete(self):
        """VirtualIp.delete()"""
        for name, req_status in [
            (NAME1, 200),
            (NAME2, 500),
        ]:
            result = self.obj.delete(name=name)
            self.assertEqual(result.status_code, req_status, msg=f"{name=}")

    def test_valid__get(self):
        """VirtualIp.get()"""
        for name, req_names in [
            (NAME1, [NAME1]),
            (NAME2, []),
        ]:
            result = self.obj.get(name=name)
            names = [d["name"] for d in result]
            self.assertEqual(names, req_names, msg=f"{name=}")

    def test_valid__update(self):
        """VirtualIp.update()"""
        for name, req_status in [
            (NAME1, 200),
            (NAME2, 500),
        ]:
            result = self.obj.update(data={"name": name})
            self.assertEqual(result.status_code, req_status, msg=f"{name=}")


if __name__ == "__main__":
    unittest.main()
