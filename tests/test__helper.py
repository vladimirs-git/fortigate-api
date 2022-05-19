"""unittest fortigate_api.py"""

import unittest

from fortigate_api import helper as h


class Test(unittest.TestCase):
    """unittest fortigate_api.py"""

    # =============================== int ================================

    def test_valid__int(self):
        """int_()"""
        for key, kwargs, req_int in [
            ("port", {"port": ""}, 0),
            ("port", {"port": 0}, 0),
            ("port", {"port": None}, 0),
            ("port", {"port": 1}, 1),
            ("port", {"port": "1"}, 1),
        ]:
            result = h.int_(key=key, **kwargs)
            self.assertEqual(result, req_int, msg=f"{key=} {kwargs=}")

    def test_invalid__int(self):
        """int_()"""
        for key, kwargs in [
            ("port", {"port": "text"}),
            ("port", {"port": {"port": "1"}}),
        ]:
            with self.assertRaises(ValueError, msg=f"{key=} {kwargs=}"):
                h.int_(key=key, **kwargs)

    # =============================== str ================================

    def test_valid__add_params_to_url(self):
        """add_params_to_url()"""
        for url, params, req in [
            ("https://domain.com", {}, "https://domain.com"),
            ("https://domain.com", dict(b="b"), "https://domain.com?b=b"),
            ("https://domain.com?a=a", dict(b="b"), "https://domain.com?a=a&b=b"),
            ("https://domain.com?a=a", dict(b=["b", "B"]), "https://domain.com?a=a&b=b&b=B"),
        ]:
            result = h.add_params_to_url(url=url, params=params)
            self.assertEqual(result, req, msg=f"{url=} {params=}")

    def test_valid__str_l(self):
        """str_()"""
        for key, kwargs, req_str in [
            ("vdom", {"vdom": ""}, ""),
            ("vdom", {"vdom": 0}, ""),
            ("vdom", {"vdom": None}, ""),
            ("vdom", {"vdom": "1"}, "1"),
        ]:
            result = h.str_(key=key, **kwargs)
            self.assertEqual(result, req_str, msg=f"{key=} {kwargs=}")

    def test_invalid__str_(self):
        """str_()"""
        for key, kwargs in [
            ("vdom", {"vdom": 1}),
            ("vdom", {"vdom": {"vdom": "name"}}),
        ]:
            with self.assertRaises(ValueError, msg=f"{key=} {kwargs=}"):
                h.str_(key=key, **kwargs)

    def test_valid__quote_(self):
        """quote_()"""
        for string, req_string in [
            ("", ""),
            ("10.0.0.0_8", "10.0.0.0_8"),
            ("10.0.0.0/8", "10.0.0.0%2F8"),
        ]:
            result = h.quote_(string=string)
            self.assertEqual(result, req_string, msg=f"{string=}")


if __name__ == "__main__":
    unittest.main()
