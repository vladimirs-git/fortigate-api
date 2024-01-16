"""Test helpers.py"""
from typing import Any

import pytest
from requests import Response

from fortigate_api import helpers as h


# ========================= scope app model ==========================

@pytest.mark.parametrize("scope, expected", [
    ("", IndexError),
    ("cmdb", ("cmdb", "cmdb_s", "CmdbS")),
    ("ab", ("ab", "ab_s", "AbS")),
])
def test__scope_names(scope, expected: Any):
    """helpers.scope_names()"""
    if isinstance(expected, tuple):
        actual = h.scope_names(scope=scope)
        assert actual == expected
    else:
        with pytest.raises(expected):
            h.scope_names(scope=scope)


@pytest.mark.parametrize("scope, app, expected", [
    ("", "", IndexError),
    ("cmdb", "firewall", ("firewall", "firewall_c", "FirewallC")),
    ("aa", "bb", ("bb", "bb_a", "BbA")),
    ("aa", "bb-bb", ("bb_bb", "bb_bb_a", "BbBbA")),
    ("aa", "bb.bb", ("bb_bb", "bb_bb_a", "BbBbA")),
])
def test__app_names(scope, app, expected: Any):
    """helpers.app_names()"""
    if isinstance(expected, tuple):
        actual = h.app_names(scope=scope, app=app)
        assert actual == expected
    else:
        with pytest.raises(expected):
            h.app_names(scope=scope, app=app)


@pytest.mark.parametrize("scope, app, model, expected", [
    ("", "", "", IndexError),
    ("cmdb", "firewall", "address", ("address", "AddressFC")),
    ("aa", "bb", "cc", ("cc", "CcBA")),
    ("aa", "bb", "cc-cc", ("cc_cc", "CcCcBA")),
    ("aa", "bb", "cc.cc", ("cc_cc", "CcCcBA")),
    ("aa", "bb", "global", ("global_", "GlobalBA")),  # model reserved_keywords
    ("aa", "bb", "1cc", ("_1cc", "_1ccBA")),  # model startswith digit
])
def test__model_names(scope, app, model, expected: Any):
    """helpers.model_names()"""
    if isinstance(expected, tuple):
        actual = h.model_names(scope=scope, app=app, model=model)
        assert actual == expected
    else:
        with pytest.raises(expected):
            h.model_names(scope=scope, app=app, model=model)


@pytest.mark.parametrize("part, expected", [
    ("", IndexError),
    ("a_b", "a_b"),
    ("a-b", "a_b"),
    ("a.b", "a_b"),
    ("1a", "_1a"),
])
def test__part_to_attr(part, expected: Any):
    """helpers.part_to_attr()"""
    if isinstance(expected, str):
        actual = h.part_to_attr(part=part)
        assert actual == expected
    else:
        with pytest.raises(expected):
            h.part_to_attr(part=part)


@pytest.mark.parametrize("attr, expected", [
    ("", ""),
    ("a_b", "a.b"),
    ("a.b", "a.b"),
    ("a-b", "a-b"),
])
def test__attr_to_app(attr, expected: Any):
    """helpers.attr_to_app()"""
    actual = h.attr_to_app(attr=attr)
    assert actual == expected


@pytest.mark.parametrize("attr, expected", [
    ("", ""),
    ("a_b", "a-b"),
    ("a.b", "a.b"),
    ("a-b", "a-b"),
])
def test__attr_to_model(attr, expected: Any):
    """helpers.attr_to_model()"""
    actual = h.attr_to_model(attr=attr)
    assert actual == expected


@pytest.mark.parametrize("path, expected", [
    ("", ValueError),
    ("address", ValueError),
    ("/cmdb/firewall/address", ("cmdb", "firewall", "address")),
    ("/cmdb/firewall.ssh/local-ca", ("cmdb", "firewall_ssh", "local_ca")),
    ("firewall/address", ("", "firewall", "address")),
    ("firewall.ssh/local-ca", ("", "firewall_ssh", "local_ca")),
])
def test__path_to_attrs(path, expected: Any):
    """helpers.path_to_attrs()"""
    if isinstance(expected, tuple):
        actual = h.path_to_attrs(path=path)
        assert actual == expected
    else:
        with pytest.raises(expected):
            h.path_to_attrs(path=path)


@pytest.mark.parametrize("path, expected", [
    ("", ValueError),
    ("address", ValueError),
    ("/cmdb/firewall/address", ("cmdb", "firewall", "address")),
    ("/cmdb/firewall.ssh/local-ca", ("cmdb", "firewall.ssh", "local-ca")),
    ("firewall/address", ("", "firewall", "address")),
    ("firewall.ssh/local-ca", ("", "firewall.ssh", "local-ca")),
])
def test__path_to_parts(path, expected: Any):
    """helpers.path_to_parts()"""
    if isinstance(expected, tuple):
        actual = h.path_to_parts(path=path)
        assert actual == expected
    else:
        with pytest.raises(expected):
            h.path_to_parts(path=path)


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


# noinspection PyShadowingBuiltins
@pytest.mark.parametrize("uid, filter, error", [
    ("", "", ValueError),
    ("", [], ValueError),
    ("", "a", None),
    ("", ["a"], None),
    ("a", "", None),
    ("a", [], None),
    ("a", "a", ValueError),
    ("a", ["a"], ValueError),
])
def test__check_uid_filter(uid, filter, error: Any):
    """helpers.check_uid_filter()"""
    if error is None:
        h.check_uid_filter(uid=uid, filter=filter)
    else:
        with pytest.raises(error):
            h.check_uid_filter(uid=uid, filter=filter)


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


# ============================= str ==============================


@pytest.mark.parametrize("url, params, expected", [
    ("https://domain.com", {}, "https://domain.com"),
    ("https://domain.com", {"b": "b"}, "https://domain.com?b=b"),
    ("https://domain.com/path", {"b": "b"}, "https://domain.com/path?b=b"),
    ("https://domain.com/path/", {"b": "b"}, "https://domain.com/path/?b=b"),
    ("https://domain.com?a=a", {"b": "b"}, "https://domain.com?a=a&b=b"),
    ("https://domain.com?a=a", {"b": ["b", "B"]}, "https://domain.com?a=a&b=b&b=B"),
])
def test__join_url_params(url, params, expected):
    """helpers.join_url_params()"""
    actual = h.join_url_params(url=url, **params)
    assert actual == expected


@pytest.mark.parametrize("string, expected", [
    ("", ""),
    (1, "1"),
    ("10.0.0.0_8", "10.0.0.0_8"),
    ("10.0.0.0/8", "10.0.0.0%2F8"),
])
def test__quote(string, expected):
    """helpers.quote()"""
    actual = h.quote(string=string)
    assert actual == expected


@pytest.mark.parametrize("url, expected", [
    ("", ""),
    ("https://domain.com/api/v2/cmdb", ""),
    ("https://domain.com/api/v2/cmdb/firewall", ""),
    ("https://domain.com/api/v2/cmdb/firewall/policy", "firewall/policy"),
    ("https://domain.com/api/v2/cmdb/firewall/policy/", "firewall/policy"),
    ("https://domain.com/api/v2/cmdb/firewall/policy/1", "firewall/policy"),
    ("https://domain.com/api/v2/cmdb/firewall/policy/1/2", "firewall/policy"),
    ("https://domain.com/api/v2/cmdb/firewall/policy?key=value", "firewall/policy"),
    ("https://domain.com/api/v2/cmdb/firewall/policy/1?key=value", "firewall/policy"),
])
def test__url_to_app_model(url, expected):
    """helpers.url_to_app_model()"""
    actual = h.url_to_app_model(url=url)
    assert actual == expected


@pytest.mark.parametrize("url, expected", [
    ("", ""),
    ("https://domain.com/api/v2/cmdb", ""),
    ("https://domain.com/api/v2/cmdb/firewall", ""),
    ("https://domain.com/api/v2/cmdb/firewall/policy", ""),
    ("https://domain.com/api/v2/cmdb/firewall/policy/", ""),
    ("https://domain.com/api/v2/cmdb/firewall/policy/1", "1"),
    ("https://domain.com/api/v2/cmdb/firewall/policy/1/2", "1"),
    ("https://domain.com/api/v2/cmdb/firewall/policy?key=value", ""),
    ("https://domain.com/api/v2/cmdb/firewall/policy/1?key=value", "1"),
])
def test__url_to_uid(url, expected):
    """helpers.url_to_uid()"""
    actual = h.url_to_uid(url=url)
    assert actual == expected


def test__rst_code():
    """helpers.rst_code()"""
    actual = h.rst_code(text="abc", code="text")
    expected = ".. code:: text\n\n    abc\n"
    assert actual == expected


# ============================= unsorted ==============================

@pytest.mark.parametrize("status_codes, expected", [
    ([], 404),
    ([200, 200], 200),
    ([200, 500, 400], 500),
    ([200, 400, 500], 500),
])
def test__highest_response(status_codes, expected):
    """helpers.highest_response()"""
    responses = []
    for status_code in status_codes:
        response = Response()
        response.status_code = status_code
        responses.append(response)
    response_: Response = h.highest_response(responses)
    actual = response_.status_code
    assert actual == expected
