"""unittest helpers.py"""
import unittest

import pytest

from fortigate_api import helpers as h


class Test(unittest.TestCase):
    """unittest helpers.py"""

    # ============================= dict =============================

    def test_valid__check_mandatory(self):
        """helpers.check_mandatory()"""
        for keys, kwargs in [
            ([], {}),
            ([], dict(a=1)),
            (["a"], dict(a=1)),
            (["a", "b"], dict(a=1, b=2, c=3)),
        ]:
            h.check_mandatory(keys=keys, **kwargs)

    def test_invalid__check_mandatory(self):
        """helpers.check_mandatory()"""
        for keys, kwargs, error in [
            (["a"], {}, KeyError),
            (["a"], dict(b=2), KeyError),
            (["a", "b"], dict(a=1, c=3), KeyError),
        ]:
            with self.assertRaises(error, msg=f"{kwargs=}"):
                h.check_mandatory(keys=keys, **kwargs)

    def test_valid__check_only_one(self):
        """helpers.check_only_one()"""
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
        """helpers.check_only_one()"""
        for keys, kwargs, error in [
            (["a", "b"], dict(a=1, b=2), KeyError),
        ]:
            with self.assertRaises(error, msg=f"{kwargs=}"):
                h.check_only_one(keys=keys, **kwargs)

    def test_valid__check_one_of(self):
        """helpers.check_one_of()"""
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
        """helpers.check_one_of()"""
        for keys, kwargs, error in [
            (["a"], {}, KeyError),
            (["a", "b"], dict(c=3), KeyError),
        ]:
            with self.assertRaises(error, msg=f"{kwargs=}"):
                h.check_one_of(keys=keys, **kwargs)

    def test_valid__get_quoted(self):
        """helpers.get_quoted()"""
        key = "name"
        for kwargs, req in [
            (dict(name=1), "1"),
            (dict(name="10.0.0.0_8"), "10.0.0.0_8"),
            (dict(name="10.0.0.0/8"), "10.0.0.0%2F8"),
        ]:
            result = h.get_quoted(key=key, **kwargs)
            self.assertEqual(result, req, msg=f"{kwargs=}")

    def test_invalid__get_quoted(self):
        """helpers.get_quoted()"""
        key = "name"
        for kwargs, error in [
            (dict(a=1), KeyError),
            ({}, KeyError),
        ]:
            with self.assertRaises(error, msg=f"{kwargs=}"):
                h.get_quoted(key=key, **kwargs)

    def test_valid__pop_int(self):
        """helpers.pop_int()"""
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
        """helpers.pop_int()"""
        key = "id"
        for data, error in [
            (dict(id="a"), TypeError),
            (dict(id=[1]), TypeError),
        ]:
            with self.assertRaises(error, msg=f"{data=}"):
                h.pop_int(key=key, data=data)

    def test_valid__pop_lstr(self):
        """helpers.pop_lstr()"""
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
        """helpers.pop_lstr()"""
        key = "filter"
        for data, error in [
            (dict(filter=1), TypeError),
            (dict(filter=[1]), TypeError),
        ]:
            with self.assertRaises(error, msg=f"{data=}"):
                h.pop_lstr(key=key, data=data)

    def test_valid__pop_str(self):
        """helpers.pop_str()"""
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

    def test_valid__make_url(self):
        """helpers.make_url()"""
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
        """helpers.quote_()"""
        for string, req in [
            ("", ""),
            (1, "1"),
            ("10.0.0.0_8", "10.0.0.0_8"),
            ("10.0.0.0/8", "10.0.0.0%2F8"),
        ]:
            result = h.quote(string=string)
            self.assertEqual(result, req, msg=f"{string=}")


# ============================= str ==============================

@pytest.mark.parametrize("word, expected", [
    ("", ""),
    ("text", "Text"),
    ("text_text", "TextText"),
    ("text_text_text", "TextTextText"),
])
def test__attr_to_class(word, expected):
    """helpers.attr_to_class()"""
    actual = h.attr_to_class(word)
    assert actual == expected


@pytest.mark.parametrize("word, expected", [
    ("", ""),
    ("Text", "text"),
    ("TextText", "text_text"),
    ("TextTextText", "text_text_text"),
])
def test__class_to_attr(word, expected):
    """helpers.class_to_attr()"""
    actual = h.class_to_attr(word)
    assert actual == expected


if __name__ == "__main__":
    unittest.main()
