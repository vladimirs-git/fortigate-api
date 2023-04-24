"""unittest base.py"""

import unittest

from requests import Response

from fortigate_api.base import Base
from tests.helper__tst import NAME1, SLASH, SLASH_, MockFortigate


class Test(MockFortigate):
    """Base"""

    def setUp(self):
        """setUp"""
        super().setUp()
        self.obj = Base(rest=self.rest, url_obj="api/v2/cmdb/firewall/address/")

    # =========================== helpers ============================

    def test_valid__highest_response(self):
        """Base._highest_response()"""
        for status_codes, req in [
            ([], 200),
            ([200, 500, 400], 500),
        ]:
            responses = []
            for status_code in status_codes:
                response = Response()
                response.status_code = status_code
                responses.append(response)
            result_ = self.obj._highest_response(responses)
            result = result_.status_code
            self.assertEqual(result, req, msg=f"{status_codes=}")

    def test_valid__quote_url(self):
        """Base._quote_url()"""
        url_base = "api/v2/cmdb/firewall/address/"
        for url, req in [
            ("", ""),
            (url_base, url_base),
            (f"{url_base}{NAME1}", f"{url_base}{NAME1}"),
            (f"{url_base}{SLASH}", f"{url_base}{SLASH_}"),
            (SLASH, SLASH),
        ]:
            result = self.obj._quote_url(url=url)
            self.assertEqual(result, req, msg=f"{url=}")


if __name__ == "__main__":
    unittest.main()
