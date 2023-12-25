"""unittest address.py"""

import unittest

import pytest
from pytest_mock import MockerFixture
from requests import Session

from fortigate_api import FortigateAPI
from fortigate_api.address import Address
from tests import helper__tst as tst


@pytest.fixture
def obj():
    """Init Fortigate"""
    api = FortigateAPI(host="host")
    api.rest._session = Session()
    return api.address


@pytest.mark.parametrize("data, expected", [
    ({"name": "ADDR1"}, 200),  # already exist
    ({"name": "ADDR2"}, 200),  # not exist
    ({"name": "A/B"}, 200),  # already exist
    ({"typo": "ADDR1"}, KeyError),
])
def test__create(obj: Address, mocker: MockerFixture, data, expected):
    """Address.create()"""
    mocker.patch("requests.Session.get",
                 side_effect=lambda *args, **kw: tst.session_get(mocker, *args, **kw))
    mocker.patch("requests.Session.post",
                 side_effect=lambda *args, **kw: tst.session_post(mocker, *args, **kw))

    if isinstance(expected, int):
        response = obj.create(data)
        actual = response.status_code
        assert actual == expected
    else:
        with pytest.raises(expected):
            obj.create(data)


@pytest.mark.parametrize("kwargs, expected", [
    ({"uid": "ADDR1"}, 200),
    ({"uid": "ADDR2"}, 404),
    ({"filter": "name==ADDR1"}, 200),
    ({"filter": "name==ADDR2"}, 200),
    ({"filter": "name==ADDR3"}, 200),
    ({"uid": ""}, ValueError),
    ({"uid": "ADDR1", "filter": "name==ADDR1"}, KeyError),
])
def test__delete(obj: Address, mocker: MockerFixture, kwargs, expected):
    """Address.delete()"""
    mocker.patch("requests.Session.get",
                 side_effect=lambda *args, **kw: tst.session_get(mocker, *args, **kw))
    mocker.patch("requests.Session.delete",
                 side_effect=lambda *args, **kw: tst.session_delete(mocker, *args, **kw))

    if isinstance(expected, int):
        response = obj.delete(**kwargs)
        actual = response.status_code
        assert actual == expected
    else:
        with pytest.raises(expected):
            obj.delete(**kwargs)


@pytest.mark.parametrize("kwargs, expected", [
    (dict(uid="ADDR1"), ["ADDR1"]),
    (dict(uid="ADDR1", filter=f"name==ADDR1"), ["ADDR1"]),
    (dict(uid="ADDR2"), []),
    (dict(uid="A/B"), ["A/B"]),
    (dict(filter="name==ADDR2"), []),
    (dict(filter=f"name==ADDR1"), ["ADDR1"]),
    (dict(id="ADDR1"), KeyError),
])
def test__get(obj: Address, mocker: MockerFixture, kwargs, expected):
    """Address.get()"""
    mocker.patch("requests.Session.get",
                 side_effect=lambda *args, **kw: tst.session_get(mocker, *args, **kw))

    if isinstance(expected, list):
        items = obj.get(**kwargs)
        actual = [d["name"] for d in items]
        assert actual == expected
    else:
        with pytest.raises(expected):
            obj.get(**kwargs)


@pytest.mark.parametrize("kwargs, expected", [
    ({"uid": "ADDR1", "data": {"name": "ADDR1"}}, 200),
    ({"uid": "ADDR3", "data": {"name": "ADDR3"}}, 404),
    ({"data": {"name": "ADDR1"}}, 200),
    ({"data": {"name": "ADDR3"}}, 404),
])
def test__update(obj: Address, mocker: MockerFixture, kwargs, expected):
    """Address.update()"""
    mocker.patch("requests.Session.get",
                 side_effect=lambda *args, **kw: tst.session_get(mocker, *args, **kw))
    mocker.patch("requests.Session.put",
                 side_effect=lambda *args, **kw: tst.session_put(mocker, *args, **kw))

    response = obj.update(**kwargs)

    actual = response.status_code
    assert actual == expected


@pytest.mark.parametrize("uid, expected", [
    ("ADDR1", True),
    ("ADDR3", False),
])
def test__is_exist(obj: Address, mocker: MockerFixture, uid, expected):
    """Address.is_exist()"""
    mocker.patch("requests.Session.get",
                 side_effect=lambda *args, **kw: tst.session_get(mocker, *args, **kw))

    actual = obj.is_exist(uid=uid)

    assert actual == expected


if __name__ == "__main__":
    unittest.main()
