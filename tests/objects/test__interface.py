"""unittest interface.py"""

import unittest

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
        api.interface,
    ]
    return items


@pytest.mark.parametrize("kwargs, expected", [
    ({"uid": "INTF1"}, 200),
    ({"uid": "INTF9"}, 404),
    ({"filter": "name==INTF1"}, 200),
    ({"filter": "name==INTF3"}, 200),
    ({"filter": "name==INTF9"}, 200),
    ({"uid": ""}, ValueError),
    ({"uid": "INTF1", "filter": "name==INTF1"}, KeyError),
])
def test__delete(connectors: list, mocker: MockerFixture, kwargs, expected):
    """Interface.delete()"""
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
    (dict(uid="INTF1"), ["INTF1"]),  # root
    (dict(uid="INTF3"), []),  # vdom3
    (dict(uid="INTF9"), []),  # absent
    (dict(filter=f"name==INTF1"), ["INTF1"]),
    (dict(filter=f"name==INTF3"), []),
    (dict(filter=f"name==INTF9"), []),
    (dict(all=True), ["INTF1", "INTF3"]),
    (dict(all=True, uid="INTF1"), ["INTF1"]),
    (dict(all=True, uid="INTF3"), ["INTF3"]),
    (dict(all=True, uid="INTF9"), []),
    (dict(all=True, filter=f"name==INTF1"), ["INTF1"]),
    (dict(all=True, filter=f"name==INTF3"), ["INTF3"]),
    (dict(all=True, filter=f"name==INTF9"), []),
    (dict(name="INTF1"), KeyError),
])
def test__get(connectors: list, mocker: MockerFixture, kwargs, expected):
    """Interface.get()"""
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
    ({"uid": "INTF1", "data": {"name": "INTF1"}}, 200),
    ({"uid": "INTF3", "data": {"name": "INTF3"}}, 200),
    ({"uid": "INTF9", "data": {"name": "INTF9"}}, 404),
    ({"data": {"name": "INTF1"}}, 200),
    ({"data": {"name": "INTF3"}}, 200),
    ({"data": {"name": "INTF9"}}, 404),
])
def test__update(connectors: list, mocker: MockerFixture, kwargs, expected):
    """Interface.update()"""
    mocker.patch("requests.Session.get",
                 side_effect=lambda *args, **kw: tst.session_get(mocker, *args, **kw))
    mocker.patch("requests.Session.put",
                 side_effect=lambda *args, **kw: tst.session_put(mocker, *args, **kw))

    for connector in connectors:
        response = connector.update(**kwargs)
        actual = response.status_code
        assert actual == expected


@pytest.mark.parametrize("uid, expected", [
    ("INTF1", True),
    ("INTF9", False),
])
def test__is_exist(connectors: list, mocker: MockerFixture, uid, expected):
    """Interface.is_exist()"""
    mocker.patch("requests.Session.get",
                 side_effect=lambda *args, **kw: tst.session_get(mocker, *args, **kw))

    for connector in connectors:
        actual = connector.is_exist(uid=uid)
        assert actual == expected, connector


if __name__ == "__main__":
    unittest.main()
