"""unittest dict_.__init__.py"""

import unittest

from fortigate_api import dict_


class Test(unittest.TestCase):
    """unittest dict_.__init__.py"""

    def test_valid__check_mandatory(self):
        """check_mandatory()"""
        for keys, kwargs in [
            ([], {}),
            ([], dict(a=1)),
            (["a"], dict(a=1)),
            (["a", "b"], dict(a=1, b=2, c=3)),
        ]:
            dict_.check_mandatory(keys=keys, **kwargs)

    def test_invalid__check_mandatory(self):
        """check_mandatory()"""
        for keys, kwargs, error in [
            (["a"], {}, KeyError),
            (["a"], dict(b=2), KeyError),
            (["a", "b"], dict(a=1, c=3), KeyError),
        ]:
            with self.assertRaises(error, msg=f"{kwargs=}"):
                dict_.check_mandatory(keys=keys, **kwargs)

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
            dict_.check_only_one(keys=keys, **kwargs)

    def test_invalid__check_only_one(self):
        """check_only_one()"""
        for keys, kwargs, error in [
            (["a", "b"], dict(a=1, b=2), KeyError),
        ]:
            with self.assertRaises(error, msg=f"{kwargs=}"):
                dict_.check_only_one(keys=keys, **kwargs)

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
            dict_.check_one_of(keys=keys, **kwargs)

    def test_invalid__check_one_of(self):
        """check_one_of()"""
        for keys, kwargs, error in [
            (["a"], {}, KeyError),
            (["a", "b"], dict(c=3), KeyError),
        ]:
            with self.assertRaises(error, msg=f"{kwargs=}"):
                dict_.check_one_of(keys=keys, **kwargs)

    def test_valid__get_quoted(self):
        """get_quoted()"""
        key = "name"
        for kwargs, req in [
            (dict(name=1), "1"),
            (dict(name="10.0.0.0_8"), "10.0.0.0_8"),
            (dict(name="10.0.0.0/8"), "10.0.0.0%2F8"),
        ]:
            result = dict_.get_quoted(key=key, **kwargs)
            self.assertEqual(result, req, msg=f"{kwargs=}")

    def test_invalid__get_quoted(self):
        """get_quoted()"""
        key = "name"
        for kwargs, error in [
            (dict(a=1), KeyError),
            ({}, KeyError),
        ]:
            with self.assertRaises(error, msg=f"{kwargs=}"):
                dict_.get_quoted(key=key, **kwargs)

    def test_valid__pop_int(self):
        """pop_int()"""
        key = "id"
        for data, req in [
            ({}, 0),
            (dict(a="a"), 0),
            (dict(id=1), 1),
            (dict(id="1"), 1),
        ]:
            result = dict_.pop_int(key=key, data=data)
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
                dict_.pop_int(key=key, data=data)

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
            result = dict_.pop_lstr(key=key, data=data)
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
                dict_.pop_lstr(key=key, data=data)

    def test_valid__pop_str(self):
        """pop_str()"""
        key = "name"
        for data, req in [
            ({}, ""),
            (dict(a="a"), ""),
            (dict(name="a"), "a"),
            (dict(name=1), "1"),
        ]:
            result = dict_.pop_str(key=key, data=data)
            self.assertEqual(result, req, msg=f"{data=}")
            result_ = data.get(key)
            self.assertIsNone(result_, msg=f"{data=}")


if __name__ == "__main__":
    unittest.main()
