"""Test address.py"""

import pytest
from pytest_mock import MockerFixture
from requests import Session

from fortigate_api import FortigateAPI
from tests import helper__tst as tst


@pytest.fixture
def connectors():
    """Init Connector objects."""
    api = FortigateAPI(host="host")
    api.rest._session = Session()
    items = [
        api.address,
    ]
    return items


@pytest.mark.parametrize("data, expected", [
    ({"name": "ADDR1"}, 200),  # already exist
    ({"name": "ADDR2"}, 200),  # not exist
    ({"name": "A/B"}, 200),  # already exist
    ({"typo": "ADDR1"}, KeyError),
])
def test__create(connectors: list, mocker: MockerFixture, data, expected):
    """Address.create()"""
    mocker.patch("requests.Session.get",
                 side_effect=lambda *args, **kw: tst.session_get(mocker, *args, **kw))
    mocker.patch("requests.Session.post",
                 side_effect=lambda *args, **kw: tst.session_post(mocker, *args, **kw))

    for connector in connectors:
        if isinstance(expected, int):
            response = connector.create(data)
            actual = response.status_code
            assert actual == expected
        else:
            with pytest.raises(expected):
                connector.create(data)


@pytest.mark.parametrize("kwargs, expected", [
    ({"uid": "ADDR1"}, 200),
    ({"uid": "ADDR9"}, 404),
    ({"filter": "name==ADDR1"}, 200),
    ({"filter": "name==ADDR9"}, 200),
    ({"uid": ""}, ValueError),
    ({"uid": "ADDR1", "filter": "name==ADDR1"}, KeyError),
])
def test__delete(connectors: list, mocker: MockerFixture, kwargs, expected):
    """Address.delete()"""
    mocker.patch("requests.Session.get",
                 side_effect=lambda *args, **kw: tst.session_get(mocker, *args, **kw))
    mocker.patch("requests.Session.delete",
                 side_effect=lambda *args, **kw: tst.session_delete(mocker, *args, **kw))

    for connector in connectors:
        if isinstance(expected, int):
            response = connector.delete(**kwargs)
            actual = response.status_code
            assert actual == expected
        else:
            with pytest.raises(expected):
                connector.delete(**kwargs)


@pytest.mark.parametrize("kwargs, expected", [
    (dict(uid="ADDR1"), ["ADDR1"]),
    (dict(uid="ADDR1", filter=f"name==ADDR1"), ["ADDR1"]),
    (dict(uid="ADDR2"), []),
    (dict(uid="A/B"), ["A/B"]),
    (dict(filter="name==ADDR2"), []),
    (dict(filter=f"name==ADDR1"), ["ADDR1"]),
    (dict(id="ADDR1"), KeyError),
])
def test__get(connectors: list, mocker: MockerFixture, kwargs, expected):
    """Address.get()"""
    mocker.patch("requests.Session.get",
                 side_effect=lambda *args, **kw: tst.session_get(mocker, *args, **kw))

    for connector in connectors:
        if isinstance(expected, list):
            items = connector.get(**kwargs)
            actual = [d["name"] for d in items]
            assert actual == expected
        else:
            with pytest.raises(expected):
                connector.get(**kwargs)


@pytest.mark.parametrize("kwargs, expected", [
    ({"uid": "ADDR1", "data": {"name": "ADDR1"}}, 200),
    ({"uid": "ADDR3", "data": {"name": "ADDR3"}}, 404),
    ({"data": {"name": "ADDR1"}}, 200),
    ({"data": {"name": "ADDR3"}}, 404),
])
def test__update(connectors: list, mocker: MockerFixture, kwargs, expected):
    """Address.update()"""
    mocker.patch("requests.Session.get",
                 side_effect=lambda *args, **kw: tst.session_get(mocker, *args, **kw))
    mocker.patch("requests.Session.put",
                 side_effect=lambda *args, **kw: tst.session_put(mocker, *args, **kw))

    for connector in connectors:
        response = connector.update(**kwargs)
        actual = response.status_code
        assert actual == expected


@pytest.mark.parametrize("uid, expected", [
    ("ADDR1", True),
    ("ADDR9", False),
])
def test__is_exist(connectors: list, mocker: MockerFixture, uid, expected):
    """Address.is_exist()"""
    mocker.patch("requests.Session.get",
                 side_effect=lambda *args, **kw: tst.session_get(mocker, *args, **kw))

    for connector in connectors:
        actual = connector.is_exist(uid=uid)
        assert actual == expected, connector
