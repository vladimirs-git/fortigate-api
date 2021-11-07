"""unittest firewall/action.py"""

from __future__ import annotations

import unittest

from fortigate_api.action import Action
from tests.helper__tst import NAME1, NAME2, NAME3, SLASH, SLASH_
from tests.mock_fortigate import MockFortigate


class Test(MockFortigate):
    """unittest firewall/action.py"""

    def setUp(self):
        super().setUp()
        self.action = Action(fgt=self.fgt)

    def test_valid__create(self):
        """Base._create()"""
        for name, req_status in [
            (NAME1, 200),
            (NAME2, 500),
            (NAME3, 200),
        ]:
            url = "api/v2/cmdb/firewall/address/"
            result = self.action._create(url=url, data={"name": name})
            self.assertEqual(result.status_code, req_status, msg=f"{name=}")

    def test_valid__delete(self):
        """Base._delete()"""
        for name, req_status in [
            (NAME1, 200),
            (NAME2, 500),
        ]:
            url = f"api/v2/cmdb/firewall/address/{name}"
            result = self.action._delete(url=url)
            self.assertEqual(result.status_code, req_status, msg=f"{name=}")

    def test_valid__get(self):
        """Base.get()"""
        for name, req_names in [
            (NAME1, [NAME1]),
            (SLASH, [SLASH_]),
            (NAME2, []),
        ]:
            url = f"api/v2/cmdb/firewall/address/{name}"
            result = self.action._get(url=url)
            names = [d["name"] for d in result]
            self.assertEqual(names, req_names, msg=f"{name=}")

    def test_valid__update(self):
        """Base.update()"""
        for name, req_status in [
            (NAME1, 200),
            (NAME2, 500),
        ]:
            url = "api/v2/cmdb/firewall/address/"
            result = self.action._update(url=url, data={"name": name})
            self.assertEqual(result.status_code, req_status, msg=f"{name=}")

    # =========================== helpers ============================

    def test_valid__url_params(self):
        """Base._url_params()"""
        url = self.action.url
        filter1, filter1_req = f"name=={NAME1}", f"{url}?filter=name%3D%3D{NAME1}"
        filter2 = f"name=={NAME2}"
        filter2_req = f"{url}?filter=name%3D%3D{NAME1}&filter=name%3D%3D{NAME2}"
        for kwargs, req_url in [
            (dict(), f"{url}"),
            (dict(id=1), f"{url}1"),
            (dict(id="1"), f"{url}1"),
            (dict(name="1"), f"{url}1"),
            (dict(name=NAME1), f"{url}{NAME1}"),
            (dict(filter=filter1), filter1_req),
            (dict(filters=[filter1]), filter1_req),
            (dict(filters=[filter1, filter2]), filter2_req),
        ]:
            result = self.action._url_params(url=url, **kwargs)
            self.assertEqual(result, req_url, msg=f"{kwargs=}")

    def test_valid__quote_url(self):
        """Base._quote_url()"""
        url_base = "api/v2/cmdb/firewall/address/"
        for url, req_url in [
            ("", ""),
            (url_base, url_base),
            (f"{url_base}{NAME1}", f"{url_base}{NAME1}"),
            (f"{url_base}{SLASH}", f"{url_base}{SLASH_}"),
            (SLASH, SLASH),
        ]:
            result = self.action._quote_url(url=url)
            self.assertEqual(result, req_url, msg=f"{url=}")

    def test_invalid__url_params(self):
        """Base._url_params()"""
        url = self.action.url
        for kwargs in [
            dict(id=""),
            dict(id=0),
            dict(id=NAME1),
            dict(name=""),
            dict(filter=""),
            dict(filters=[]),
            dict(id=0, name=""),
            dict(id=1, name=NAME2),
            dict(typo=""),
            dict(id=1, typo=""),
        ]:
            with self.assertRaises(ValueError, msg=f"{kwargs=}"):
                self.action._url_params(url=url, **kwargs)


if __name__ == "__main__":
    unittest.main()
