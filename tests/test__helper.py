"""unittest helper.py"""

import unittest

from fortigate_api import helpers as h


class Test(unittest.TestCase):
    """unittest helper.py"""

    # ============================= dict =============================

    def test_valid__check_mandatory(self):
        """check_mandatory()"""
        for keys, kwargs in [
            ([], {}),
            ([], dict(a=1)),
            (["a"], dict(a=1)),
            (["a", "b"], dict(a=1, b=2, c=3)),
        ]:
            h.check_mandatory(keys=keys, **kwargs)

    def test_invalid__check_mandatory(self):
        """check_mandatory()"""
        for keys, kwargs, error in [
            (["a"], {}, KeyError),
            (["a"], dict(b=2), KeyError),
            (["a", "b"], dict(a=1, c=3), KeyError),
        ]:
            with self.assertRaises(error, msg=f"{kwargs=}"):
                h.check_mandatory(keys=keys, **kwargs)

    def test_valid__check_only_one(self):
        """check_only_one()"""
        for keys, kwargs in [
            ([], {}),
            ([], dict(a=1)),
            (["a"], {}),
            (["a"], dict(a=1)),
            (["a"], dict(a=1, b=2)),
            (["a", "b"], dict(a=1, c=3)),
            (["a", "b"], dict(b=2, c=3)),
        ]:
            h.check_only_one(keys=keys, **kwargs)

    def test_invalid__check_only_one(self):
        """check_only_one()"""
        for keys, kwargs, error in [
            (["a", "b"], dict(a=1, b=2), KeyError),
        ]:
            with self.assertRaises(error, msg=f"{kwargs=}"):
                h.check_only_one(keys=keys, **kwargs)

    def test_valid__check_one_of(self):
        """check_one_of()"""
        for keys, kwargs in [
            ([], {}),
            ([], dict(a=1)),
            (["a"], dict(a=1)),
            (["a"], dict(a=1, b=2)),
            (["a", "b"], dict(a=1, c=3)),
            (["a", "b"], dict(b=2, c=3)),
        ]:
            h.check_one_of(keys=keys, **kwargs)

    def test_invalid__check_one_of(self):
        """check_one_of()"""
        for keys, kwargs, error in [
            (["a"], {}, KeyError),
            (["a", "b"], dict(c=3), KeyError),
        ]:
            with self.assertRaises(error, msg=f"{kwargs=}"):
                h.check_one_of(keys=keys, **kwargs)

    def test_valid__get_quoted(self):
        """get_quoted()"""
        key = "name"
        for kwargs, req in [
            (dict(name=1), "1"),
            (dict(name="10.0.0.0_8"), "10.0.0.0_8"),
            (dict(name="10.0.0.0/8"), "10.0.0.0%2F8"),
        ]:
            result = h.get_quoted(key=key, **kwargs)
            self.assertEqual(result, req, msg=f"{kwargs=}")

    def test_invalid__get_quoted(self):
        """get_quoted()"""
        key = "name"
        for kwargs, error in [
            (dict(a=1), KeyError),
            ({}, KeyError),
        ]:
            with self.assertRaises(error, msg=f"{kwargs=}"):
                h.get_quoted(key=key, **kwargs)

    def test_valid__pop_int(self):
        """pop_int()"""
        key = "id"
        for data, req in [
            ({}, 0),
            (dict(a="a"), 0),
            (dict(id=1), 1),
            (dict(id="1"), 1),
        ]:
            result = h.pop_int(key=key, data=data)
            self.assertEqual(result, req, msg=f"{data=}")
            result_ = data.get(key)
            self.assertIsNone(result_, msg=f"{data=}")

    def test_invalid__pop_int(self):
        """pop_int()"""
        key = "id"
        for data, error in [
            (dict(id="a"), TypeError),
            (dict(id=[1]), TypeError),
        ]:
            with self.assertRaises(error, msg=f"{data=}"):
                h.pop_int(key=key, data=data)

    def test_valid__pop_lstr(self):
        """pop_lstr()"""
        key = "filter"
        for data, req in [
            ({}, []),
            (dict(a="a"), []),
            (dict(filter=[]), []),
            (dict(filter="a"), ["a"]),
            (dict(filter=["a"]), ["a"]),
            (dict(filter=["b", "a"]), ["b", "a"]),
        ]:
            result = h.pop_lstr(key=key, data=data)
            self.assertEqual(result, req, msg=f"{data=}")
            result_ = data.get(key)
            self.assertIsNone(result_, msg=f"{data=}")

    def test_invalid__pop_lstr(self):
        """pop_lstr()"""
        key = "filter"
        for data, error in [
            (dict(filter=1), TypeError),
            (dict(filter=[1]), TypeError),
        ]:
            with self.assertRaises(error, msg=f"{data=}"):
                h.pop_lstr(key=key, data=data)

    def test_valid__pop_str(self):
        """pop_str()"""
        key = "name"
        for data, req in [
            ({}, ""),
            (dict(a="a"), ""),
            (dict(name="a"), "a"),
            (dict(name=1), "1"),
        ]:
            result = h.pop_str(key=key, data=data)
            self.assertEqual(result, req, msg=f"{data=}")
            result_ = data.get(key)
            self.assertIsNone(result_, msg=f"{data=}")

    # ============================= str ==============================

    def test_valid__findall1(self):
        """helpers.findall1()"""
        for pattern, string, expected in [
            ("", "abcde", ""),  # empty string
            ("typo", "abcde", ""),  # no match
            ("(typo)", "abcde", ""),  # no match
            ("(b)", "abcde", "b"),  # valid
            ("(b)(c)", "abcde", "b"),  # multiple match
        ]:
            actual = h.findall1(pattern=pattern, string=string)
            self.assertEqual(expected, actual, msg=f"{pattern=}")

    def test_invalid__findall1(self):
        """helpers.findall1()"""
        for pattern, string, error in [
            (["(b)"], "abcde", TypeError),
        ]:
            with self.assertRaises(error, msg=f"{pattern=}"):
                # noinspection PyTypeChecker
                h.findall1(pattern=pattern, string=string)

    def test_valid__findall2(self):
        """helpers.findall2()"""
        for pattern, string, expected in [
            ("", "abcde", ("", "")),
            ("typo", "abcde", ("", "")),
            ("(b)", "abcde", ("", "")),
            ("(b)(typo)", "abcde", ("", "")),
            ("(typo)(c)", "abcde", ("", "")),
            ("(b)(c)", "abcde", ("b", "c")),
            ("(b)(c)(d)", "abcde", ("b", "c")),
        ]:
            actual = h.findall2(pattern=pattern, string=string)
            self.assertEqual(expected, actual, msg=f"{pattern=}")

    def test_valid__findall3(self):
        """helpers.findall3()"""
        for pattern, string, expected in [
            ("", "abcde", ("", "", "")),
            ("typo", "abcde", ("", "", "")),
            ("(b)", "abcde", ("", "", "")),
            ("(b)(c)", "abcde", ("", "", "")),
            ("(typo)(c)(d)", "abcde", ("", "", "")),
            ("(b)(typo)(d)", "abcde", ("", "", "")),
            ("(b)(c)(typo)", "abcde", ("", "", "")),
            ("(b)(c)(d)", "abcde", ("b", "c", "d")),
            ("(b)(c)(d)(e)", "abcde", ("b", "c", "d")),
        ]:
            actual = h.findall3(pattern=pattern, string=string)
            self.assertEqual(expected, actual, msg=f"{pattern=}")

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
            result = h.make_url(url=url, **params)
            self.assertEqual(result, req, msg=f"{url=} {params=}")

    def test_valid__quote_(self):
        """quote_()"""
        for string, req in [
            ("", ""),
            (1, "1"),
            ("10.0.0.0_8", "10.0.0.0_8"),
            ("10.0.0.0/8", "10.0.0.0%2F8"),
        ]:
            result = h.quote(string=string)
            self.assertEqual(result, req, msg=f"{string=}")


if __name__ == "__main__":
    unittest.main()
