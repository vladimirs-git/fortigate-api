"""unittest firewall/object_base.py"""

import unittest

from fortigate_api.base.object_base import ObjectBase
from tests.helper__tst import NAME1, NAME2, NAME3, SLASH, SLASH_, MockFortigate


class Test(MockFortigate):
    """unittest firewall/object_base.py"""

    def setUp(self):
        """setUp"""
        super().setUp()
        self.obj = ObjectBase(fgt=self.fgt)

    def test_valid__create(self):
        """ObjectBase._create()"""
        for name, req_status in [
            (NAME1, 200),
            (NAME2, 500),
            (NAME3, 200),
        ]:
            url = "api/v2/cmdb/firewall/address/"
            result = self.obj._create(url=url, data={"name": name})
            self.assertEqual(result.status_code, req_status, msg=f"{name=}")

    def test_valid__delete(self):
        """ObjectBase._delete()"""
        for name, req_status in [
            (NAME1, 200),
            (NAME2, 500),
        ]:
            url = f"api/v2/cmdb/firewall/address/{name}"
            result = self.obj._delete(url=url)
            self.assertEqual(result.status_code, req_status, msg=f"{name=}")

    def test_valid__get(self):
        """ObjectBase.get()"""
        for name, req_names in [
            (NAME1, [NAME1]),
            (SLASH, [SLASH_]),
            (NAME2, []),
        ]:
            url = f"api/v2/cmdb/firewall/address/{name}"
            result = self.obj._get(url=url)
            names = [d["name"] for d in result]
            self.assertEqual(names, req_names, msg=f"{name=}")

    def test_valid__update(self):
        """ObjectBase.update()"""
        for name, req_status in [
            (NAME1, 200),
            (NAME2, 500),
        ]:
            url = "api/v2/cmdb/firewall/address/"
            result = self.obj._update(url=url, data={"name": name})
            self.assertEqual(result.status_code, req_status, msg=f"{name=}")

    # =========================== helpers ============================

    def test_valid__name_to_filter(self):
        """ObjectBase._name_to_filter()"""
        name = "NAME"
        for kwargs, req_kwargs in [
            ({}, {}),
            ({"id": 1}, {"id": 1}),
            ({"name": name}, {"filter": f"name=={name}"}),
        ]:
            self.obj._name_to_filter(kwargs=kwargs)
            self.assertEqual(kwargs, req_kwargs, msg=f"{kwargs=}")

    def test_valid__url_params(self):
        """ObjectBase._url_params()"""
        url = self.obj.url
        filter1 = f"name=={NAME1}"
        req1 = f"{url}?filter=name%3D%3D{NAME1}"
        filter2 = f"name=={NAME2}"
        req2 = f"{url}?filter=name%3D%3D{NAME1}&filter=name%3D%3D{NAME2}"
        for kwargs, req_url in [
            ({}, url),
            (dict(id=""), url),
            (dict(id=0), url),
            (dict(id=1), f"{url}1"),
            (dict(id="1"), f"{url}1"),
            (dict(name=""), url),
            (dict(name="1"), f"{url}1"),
            (dict(name=NAME1), f"{url}{NAME1}"),
            (dict(filter=""), url),
            (dict(filter=[]), url),
            (dict(filter=filter1), req1),
            (dict(filter=[filter1]), req1),
            (dict(filter=[filter1, filter2]), req2),
        ]:
            result = self.obj._url_params(url=url, **kwargs)
            self.assertEqual(result, req_url, msg=f"{kwargs=}")

    def test_invalid__url_params(self):
        """ObjectBase._url_params()"""
        url = self.obj.url
        for kwargs in [
            dict(id=NAME1),
            dict(filters=[f"name=={NAME1}"]),
            dict(typo=""),
            # combo
            dict(id=0, name=""),
            dict(id=1, name=NAME2),
            dict(id=1, typo=""),
        ]:
            with self.assertRaises(ValueError, msg=f"{kwargs=}"):
                self.obj._url_params(url=url, **kwargs)

    def test_valid__quote_url(self):
        """Action._quote_url()"""
        url_base = "api/v2/cmdb/firewall/address/"
        for url, req_url in [
            ("", ""),
            (url_base, url_base),
            (f"{url_base}{NAME1}", f"{url_base}{NAME1}"),
            (f"{url_base}{SLASH}", f"{url_base}{SLASH_}"),
            (SLASH, SLASH),
        ]:
            result = self.obj._quote_url(url=url)
            self.assertEqual(result, req_url, msg=f"{url=}")


if __name__ == "__main__":
    unittest.main()
