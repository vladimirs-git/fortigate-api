"""unittest str_.__init__.py"""

import unittest

from fortigate_api import str_


class Test(unittest.TestCase):
    """unittest str_.__init__.py"""

    def test_valid__make_url(self):
        """make_url()"""
        for url, params, req in [
            ("https://domain.com", {}, "https://domain.com"),
            ("https://domain.com", dict(b="b"), "https://domain.com?b=b"),
            ("https://domain.com/path", dict(b="b"), "https://domain.com/path?b=b"),
            ("https://domain.com/path/", dict(b="b"), "https://domain.com/path/?b=b"),
            ("https://domain.com?a=a", dict(b="b"), "https://domain.com?a=a&b=b"),
            ("https://domain.com?a=a", dict(b=["b", "B"]), "https://domain.com?a=a&b=b&b=B"),
        ]:
            result = str_.make_url(url=url, **params)
            self.assertEqual(result, req, msg=f"{url=} {params=}")

    def test_valid__quote_(self):
        """quote_()"""
        for string, req in [
            ("", ""),
            (1, "1"),
            ("10.0.0.0_8", "10.0.0.0_8"),
            ("10.0.0.0/8", "10.0.0.0%2F8"),
        ]:
            result = str_.quote(string=string)
            self.assertEqual(result, req, msg=f"{string=}")


if __name__ == "__main__":
    unittest.main()
