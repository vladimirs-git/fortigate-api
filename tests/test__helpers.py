"""Test helpers.py"""

import pytest

from fortigate_api import helpers as h


# =============================== dict ===============================

@pytest.mark.parametrize("keys, kwargs, error", [
    ([], {}, None),
    ([], {"a": 1}, None),
    (["a"], {"a": 1}, None),
    (["a", "b"], {"a": 1, "b": 2, "c": 3}, None),
    (["a"], {}, KeyError),
    (["a"], {"b": 2}, KeyError),
    (["a", "b"], {"a": 1, "c": 3}, KeyError),
])
def test__check_mandatory(keys, kwargs, error):
    """helpers.check_mandatory()"""
    if error is None:
        h.check_mandatory(keys=keys, **kwargs)
    else:
        with pytest.raises(error):
            h.check_mandatory(keys=keys, **kwargs)


@pytest.mark.parametrize("keys, kwargs, error", [
    ([], {}, None),
    ([], {"a": 1}, None),
    (["a"], {}, None),
    (["a"], {"a": 1}, None),
    (["a"], {"a": 1, "b": 2}, None),
    (["a", "b"], {"a": 1, "c": 3}, None),
    (["a", "b"], {"b": 2, "c": 3}, None),
    (["a", "b"], {"a": 1, "b": 2}, KeyError),
])
def test__check_only_one(keys, kwargs, error):
    """helpers.check_only_one()"""
    if error is None:
        h.check_only_one(keys=keys, **kwargs)
    else:
        with pytest.raises(error):
            h.check_only_one(keys=keys, **kwargs)


@pytest.mark.parametrize("keys, kwargs, error", [
    ([], {}, None),
    ([], {"a": 1}, None),
    (["a"], {}, KeyError),
    (["a"], {"a": 1}, None),
    (["a"], {"a": 1, "b": 2}, None),
    (["a", "b"], {"a": 1, "c": 3}, None),
    (["a", "b"], {"b": 2, "c": 3}, None),
    (["a", "b"], {"c": 3}, KeyError),
])
def test__check_one_of(keys, kwargs, error):
    """helpers.check_one_of()"""
    if error is None:
        h.check_one_of(keys=keys, **kwargs)
    else:
        with pytest.raises(error):
            h.check_one_of(keys=keys, **kwargs)


@pytest.mark.parametrize("kwargs, expected", [
    ({"name": 1}, "1"),
    ({"name": "10.0.0.0_8"}, "10.0.0.0_8"),
    ({"name": "10.0.0.0/8"}, "10.0.0.0%2F8"),
    ({"typo": 1}, KeyError),
    ({}, KeyError),
])
def test__get_quoted(kwargs, expected):
    """helpers.get_quoted()"""
    key = "name"
    if isinstance(expected, str):
        actual = h.get_quoted(key=key, **kwargs)
        assert actual == expected
    else:
        with pytest.raises(expected):
            h.get_quoted(key=key, **kwargs)


@pytest.mark.parametrize("data, expected", [
    ({}, 0),
    ({"typo": "a"}, 0),
    ({"id": -1}, TypeError),
    ({"id": 0}, 0),
    ({"id": 1}, 1),
    ({"id": "1"}, 1),
    ({"id": "a"}, TypeError),
    ({"id": [1]}, TypeError),
])
def test__pop_int(data, expected):
    """helpers.pop_int()"""
    key = "id"
    if isinstance(expected, int):
        actual = h.pop_int(key=key, data=data)
        assert actual == expected
        none = data.get(key)
        assert none is None
    else:
        with pytest.raises(expected):
            h.pop_int(key=key, data=data)


@pytest.mark.parametrize("data, expected", [
    ({}, []),
    ({"typo": "a"}, []),
    ({"filter": []}, []),
    ({"filter": "a"}, ["a"]),
    ({"filter": ["a", "b"]}, ["a", "b"]),
    ({"filter": ["b", "a"]}, ["b", "a"]),
    ({"filter": 1}, TypeError),
    ({"filter": [1]}, TypeError),
])
def test__pop_lstr(data, expected):
    """helpers.pop_lstr()"""
    key = "filter"
    if isinstance(expected, list):
        actual = h.pop_lstr(key=key, data=data)
        assert actual == expected
        none = data.get(key)
        assert none is None
    else:
        with pytest.raises(expected):
            h.pop_lstr(key=key, data=data)


@pytest.mark.parametrize("data, expected", [
    ({}, ""),
    ({"typo": "a"}, ""),
    ({"name": "a"}, "a"),
    ({"name": 1}, "1"),
])
def test__pop_str(data, expected):
    """helpers.pop_str()"""
    key = "name"
    actual = h.pop_str(key=key, data=data)
    assert actual == expected
    none = data.get(key)
    assert none is None


@pytest.mark.parametrize("data, expected", [
    ({}, ""),
    ({"name": "a/1"}, "a%2F1"),
])
def test__pop_quoted(data, expected):
    """helpers.pop_quoted()"""
    key = "name"
    actual = h.pop_quoted(key=key, data=data)
    assert actual == expected
    none = data.get(key)
    assert none is None


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


@pytest.mark.parametrize("url, params, expected", [
    ("https://domain.com", {}, "https://domain.com"),
    ("https://domain.com", {"b": "b"}, "https://domain.com?b=b"),
    ("https://domain.com/path", {"b": "b"}, "https://domain.com/path?b=b"),
    ("https://domain.com/path/", {"b": "b"}, "https://domain.com/path/?b=b"),
    ("https://domain.com?a=a", {"b": "b"}, "https://domain.com?a=a&b=b"),
    ("https://domain.com?a=a", {"b": ["b", "B"]}, "https://domain.com?a=a&b=b&b=B"),
])
def test_valid__make_url(url, params, expected):
    """helpers.make_url()"""
    actual = h.make_url(url=url, **params)
    assert actual == expected


@pytest.mark.parametrize("string, expected", [
    ("", ""),
    (1, "1"),
    ("10.0.0.0_8", "10.0.0.0_8"),
    ("10.0.0.0/8", "10.0.0.0%2F8"),
])
def test_valid__quote(string, expected):
    """helpers.quote()"""
    actual = h.quote(string=string)
    assert actual == expected
