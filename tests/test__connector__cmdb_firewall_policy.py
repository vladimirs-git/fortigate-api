"""Test Policy connector"""

import pytest
from pytest_mock import MockerFixture
from requests import Session

from fortigate_api import FortiGateAPI
from tests import helpers__tst as tst


@pytest.fixture
def connectors():
    """Init Connector objects."""
    api = FortiGateAPI(host="host", username="test")
    api.fortigate._session = Session()
    items = [
        api.cmdb.firewall.policy,
    ]
    return items


@pytest.mark.parametrize("data, expected", [
    ({"name": "POL1"}, 500),  # object exists
    ({"name": "POL9"}, 200),  # object does not exist
    ({"typo": "POL1"}, KeyError),  # invalid key
])
def test__create(connectors: list, mocker: MockerFixture, data, expected):
    """Policy.create()"""
    mocker.patch(target="requests.Session.post",
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
    (dict(uid=1), 200),  # object exists
    (dict(uid="1"), 200),  # object exists
    (dict(uid=9), 404),  # object does not exist
    (dict(filter="policyid==1"), 200),  # object has been found
    (dict(filter="policyid==9"), 404),  # object has not been found
    (dict(filter="name==POL1"), 200),  # object has been found
    (dict(filter="name==POL9"), 404),  # object has not been found
    (dict(uid="", filter="policyid==1"), 200),  # invalid uid
    (dict(uid=0, filter="policyid==1"), 200),  # invalid uid
    (dict(uid=""), ValueError),  # invalid uid
    (dict(uid=0), ValueError),  # invalid uid
    (dict(uid=1, filter="policyid==1"), ValueError),  # invalid uid
    (dict(uid="0", filter="policyid==1"), ValueError),  # invalid uid
])
def test__delete(connectors: list, mocker: MockerFixture, kwargs, expected):
    """Policy.delete()"""
    mocker.patch(target="requests.Session.get",
                 side_effect=lambda *args, **kw: tst.session_get(mocker, *args, **kw))
    mocker.patch(target="requests.Session.delete",
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
    (dict(policyid=1), ["POL1"]),  # object exists
    (dict(policyid="POL9"), []),  # object does not exist
    (dict(policyid=1, filter="name==POL1"), ["POL1"]),  # object has been found
    (dict(filter="name==POL1"), ["POL1"]),  # object has been found
    (dict(filter="name==POL9"), []),  # object has not been found
    (dict(typo=1), []),  # invalid param
])
def test__get(connectors: list, mocker: MockerFixture, kwargs, expected):
    """Policy.get()"""
    mocker.patch(target="requests.Session.get",
                 side_effect=lambda *args, **kw: tst.session_get(mocker, *args, **kw))

    for connector in connectors:
        items = connector.get(**kwargs)
        actual = [d["name"] for d in items]
        assert actual == expected


@pytest.mark.parametrize("kwargs, expected", [
    ({"policyid": 1, "position": "before", "neighbor": 2}, 200),  # object exists
    ({"policyid": 4, "position": "before", "neighbor": 2}, 500),  # object does not exist
])
def test__move(connectors: list, mocker: MockerFixture, kwargs, expected):
    """Policy.move()"""
    mocker.patch(target="requests.Session.get",
                 side_effect=lambda *args, **kw: tst.session_get(mocker, *args, **kw))
    mocker.patch(target="requests.Session.put",
                 side_effect=lambda *args, **kw: tst.session_put(mocker, *args, **kw))

    for connector in connectors:
        response = connector.move(**kwargs)
        actual = response.status_code
        assert actual == expected


@pytest.mark.parametrize("data, expected", [
    ({"policyid": 1, "name": "POL1"}, 200),  # object exists
    ({"policyid": 9, "name": "POL9"}, 404),  # object does not exist
])
def test__update(connectors: list, mocker: MockerFixture, data, expected):
    """Policy.update()"""
    mocker.patch(target="requests.Session.put",
                 side_effect=lambda *args, **kw: tst.session_put(mocker, *args, **kw))

    for connector in connectors:
        response = connector.update(data=data)
        actual = response.status_code
        assert actual == expected


@pytest.mark.parametrize("policyid, expected", [
    (1, True),  # object exists
    (9, False),  # object does not exist
])
def test__is_exist(connectors: list, mocker: MockerFixture, policyid, expected):
    """Policy.is_exist()"""
    mocker.patch(target="requests.Session.get",
                 side_effect=lambda *args, **kw: tst.session_get(mocker, *args, **kw))

    for connector in connectors:
        actual = connector.is_exist(uid=policyid)
        assert actual == expected, connector
