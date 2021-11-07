"""unittest fortigate_api.py"""

from __future__ import annotations

import unittest

from fortigate_api import helper


class Test(unittest.TestCase):
    """unittest fortigate_api.py"""

    def test_valid__int(self):
        """int_()"""
        for key, kwargs, req_int in [
            ("port", {"port": ""}, 0),
            ("port", {"port": 0}, 0),
            ("port", {"port": None}, 0),
            ("port", {"port": 1}, 1),
            ("port", {"port": "1"}, 1),
        ]:
            result = helper.int_(key=key, **kwargs)
            self.assertEqual(result, req_int, msg=f"{key=} {kwargs=}")

    def test_invalid__int(self):
        """int_()"""
        for key, kwargs in [
            ("port", {"port": "text"}),
            ("port", {"port": {"port": "1"}}),
        ]:
            with self.assertRaises(ValueError, msg=f"{key=} {kwargs=}"):
                helper.int_(key=key, **kwargs)

    def test_valid__str(self):
        """str_()"""
        for key, kwargs, req_str in [
            ("vdom", {"vdom": ""}, ""),
            ("vdom", {"vdom": 0}, ""),
            ("vdom", {"vdom": None}, ""),
            ("vdom", {"vdom": "1"}, "1"),
        ]:
            result = helper.str_(key=key, **kwargs)
            self.assertEqual(result, req_str, msg=f"{key=} {kwargs=}")

    def test_invalid__str(self):
        """str_()"""
        for key, kwargs in [
            ("vdom", {"vdom": 1}),
            ("vdom", {"vdom": {"vdom": "name"}}),
        ]:
            with self.assertRaises(ValueError, msg=f"{key=} {kwargs=}"):
                helper.str_(key=key, **kwargs)

    def test_valid__quote(self):
        """quote_()"""
        for string, req_string in [
            ("", ""),
            ("10.0.0.0_8", "10.0.0.0_8"),
            ("10.0.0.0/8", "10.0.0.0%2F8"),
        ]:
            result = helper.quote_(string=string)
            self.assertEqual(result, req_string, msg=f"{string=}")

    def test_valid__name_to_filter(self):
        """name_to_filter()"""
        name = "NAME"
        for kwargs, req_kwargs in [
            ({}, {}),
            ({"id": 1}, {"id": 1}),
            ({"name": name}, {"filter": f"name=={name}"}),
        ]:
            helper.name_to_filter(kwargs=kwargs)
            self.assertEqual(kwargs, req_kwargs, msg=f"{kwargs=}")


if __name__ == "__main__":
    unittest.main()
