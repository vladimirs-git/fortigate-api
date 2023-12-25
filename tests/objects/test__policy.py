"""unittest policy.py"""

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
        api.policy,
    ]
    return items


@pytest.mark.parametrize("data, expected", [
    ({"name": "POL1"}, 500),  # already exist
    ({"name": "POL2"}, 200),  # not exist
    ({"typo": "POL1"}, KeyError),
])
def test__create(connectors: list, mocker: MockerFixture, data, expected):
    """Policy.create()"""
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
    (dict(uid="1"), 200),
    (dict(uid=1), 200),
    (dict(uid=2), 404),
    (dict(filter="policyid==1"), 200),
    (dict(filter="policyid==2"), 200),
    (dict(filter=f"name==POL1"), 200),
    (dict(filter="name==POL2"), 200),
    (dict(uid="", filter="policyid==1"), 200),
    (dict(uid=0, filter="policyid==1"), 200),
    (dict(uid=""), ValueError),
    (dict(uid=0), ValueError),
    (dict(uid=1, filter="policyid==1"), KeyError),
    (dict(uid="0", filter="policyid==1"), KeyError),
])
def test__delete(connectors: list, mocker: MockerFixture, kwargs, expected):
    """Policy.delete()"""
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
    (dict(uid=1), ["POL1"]),
    (dict(uid=1, filter=f"name==POL1"), ["POL1"]),
    (dict(uid="POL2"), []),
    (dict(filter="name==POL2"), []),
    (dict(filter=f"name==POL1"), ["POL1"]),
    (dict(id=1), KeyError),
    # efilter
    (dict(efilter="srcaddr==10.0.0.0/30"), ["POL1"]),
    (dict(efilter="srcaddr==10.0.0.0/29"), []),
    (dict(efilter="srcaddr!=10.0.0.0/30"), ["POL3"]),
    (dict(efilter="srcaddr!=10.0.0.0/29"), ["POL1", "POL3"]),
    (dict(efilter="srcaddr<=10.0.0.0/32"), []),  # get all subnets
    (dict(efilter="srcaddr<=10.0.0.0/31"), []),
    (dict(efilter="srcaddr<=10.0.0.0/30"), ["POL1"]),
    (dict(efilter="srcaddr<=10.0.0.0/29"), ["POL1", "POL3"]),
    (dict(efilter="srcaddr<=0.0.0.0/0"), ["POL1", "POL3"]),
    (dict(efilter="srcaddr>=10.0.0.0"), ["POL1"]),  # get all supernets
    (dict(efilter="srcaddr>=10.0.0.0/32"), ["POL1"]),
    (dict(efilter="srcaddr>=10.0.0.0/31"), ["POL1"]),
    (dict(efilter="srcaddr>=10.0.0.0/30"), ["POL1"]),
    (dict(efilter="srcaddr>=10.0.0.0/29"), []),
    (dict(efilter="srcaddr>=0.0.0.0/0"), []),
    (dict(name="POL1"), KeyError),
    (dict(efilter="srcaddr=!10.0.0.0/30"), ValueError),
    (dict(efilter="typo==10.0.0.0/30"), ValueError),
    (dict(efilter="srcaddr==typo"), ValueError),
    (dict(efilter="srcaddr==10.0.0.1000"), ValueError),
    (dict(efilter="srcaddr==10.0.0.1/33"), ValueError),
    (dict(efilter="srcaddr==fd12:3456:789a:1::/64"), ValueError),
])
def test__get(connectors: list, mocker: MockerFixture, kwargs, expected):
    """Policy.get()"""
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
    ({"uid": 1, "position": "before", "neighbor": 2}, 200),
    ({"uid": 4, "position": "before", "neighbor": 2}, 500),
])
def test__move(connectors: list, mocker: MockerFixture, kwargs, expected):
    """Policy.move()"""
    mocker.patch("requests.Session.get",
                 side_effect=lambda *args, **kw: tst.session_get(mocker, *args, **kw))
    mocker.patch("requests.Session.put",
                 side_effect=lambda *args, **kw: tst.session_put(mocker, *args, **kw))

    for connector in connectors:
        response = connector.move(**kwargs)
        actual = response.status_code
        assert actual == expected


@pytest.mark.parametrize("kwargs, expected", [
    ({"uid": 1, "data": {"name": "POL1"}}, 200),
    ({"uid": 3, "data": {"name": "POL3"}}, 404),
    ({"data": {"policyid": 1, "name": "POL1"}}, 200),
    ({"data": {"policyid": 3, "name": "POL3"}}, 404),
])
def test__update(connectors: list, mocker: MockerFixture, kwargs, expected):
    """Policy.update()"""
    mocker.patch("requests.Session.get",
                 side_effect=lambda *args, **kw: tst.session_get(mocker, *args, **kw))
    mocker.patch("requests.Session.put",
                 side_effect=lambda *args, **kw: tst.session_put(mocker, *args, **kw))

    for connector in connectors:
        response = connector.update(**kwargs)
        actual = response.status_code
        assert actual == expected


@pytest.mark.parametrize("uid, expected", [
    (1, True),
    (9, False),
])
def test__is_exist(connectors: list, mocker: MockerFixture, uid, expected):
    """Policy.is_exist()"""
    mocker.patch("requests.Session.get",
                 side_effect=lambda *args, **kw: tst.session_get(mocker, *args, **kw))

    for connector in connectors:
        actual = connector.is_exist(uid=uid)
        assert actual == expected, connector


if __name__ == "__main__":
    unittest.main()
