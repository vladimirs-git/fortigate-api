"""unittest object.py"""

import unittest

from fortigate_api.objects.object import Object
from tests.helper__tst import NAME1, NAME2, NAME3, SLASH, MockFortigate

URL_ADDR = "api/v2/cmdb/firewall/address/"
URL_NAME1 = "api/v2/cmdb/firewall/address/NAME1"
URL_NAME2 = "api/v2/cmdb/firewall/address/NAME2"


class Test(MockFortigate):
    """unittest object.py"""

    def setUp(self):
        """setUp"""
        super().setUp()
        self.obj = Object(fgt=self.fgt)

    def test_valid__create(self):
        """Object.create()"""
        url1 = "api/v2/cmdb/firewall/address/"
        for name, url, req_status in [
            (NAME1, url1, 200),  # present in the Fortigate, no need create
            (NAME2, url1, 500),  # error
            (NAME3, url1, 200),  # absent in the Fortigate, need create
            (SLASH, url1, 200),  # name with slash, present in the Fortigate, no need create
        ]:
            result = self.obj.create(data={"name": name}, url=url)
            self.assertEqual(result.status_code, req_status, msg=f"{name=} {url=}")

    def test_valid__delete(self):
        """Object.delete()"""
        for url, req_status in [
            (URL_NAME1, 200),
            (URL_NAME2, 500),
        ]:
            result = self.obj.delete(url=url)
            self.assertEqual(result.status_code, req_status, msg=f"{url=}")

    def test_valid__get(self):
        """Object.get()"""
        for url, req in [
            (URL_NAME1, [NAME1]),
            (URL_NAME2, []),
        ]:
            result = self.obj.get(url=url)
            names = [d["name"] for d in result]
            self.assertEqual(names, req, msg=f"{url=}")

    def test_valid__is_exist(self):
        """Object.is_exist()"""
        for url, req in [
            (URL_NAME1, True),
            (URL_NAME2, False),
        ]:
            result = self.obj.is_exist(url=url)
            self.assertEqual(result, req, msg=f"{url=}")

    def test_valid__update(self):
        """Object.update()"""
        for url, data, req_status in [
            (URL_ADDR, {"name": NAME1}, 200),
            (URL_ADDR, {"name": NAME2}, 500),
        ]:
            result = self.obj.update(url=url, data=data)
            self.assertEqual(result.status_code, req_status, msg=f"{url=}")


if __name__ == "__main__":
    unittest.main()
