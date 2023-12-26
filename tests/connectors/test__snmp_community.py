"""unittest snmp_community.py"""

import pytest
from pytest_mock import MockerFixture
from requests import Session

from fortigate_api import FortigateAPI
from tests import helpers__tst as tst


@pytest.fixture
def connectors():
    """Init Connector objects."""
    api = FortigateAPI(host="host")
    api.rest._session = Session()
    items = [
        api.snmp_community,
    ]
    return items


@pytest.mark.parametrize("kwargs, expected", [
    ({"uid": "NAME1"}, 200),
    ({"uid": "NAME9"}, 404),
    ({"uid": ""}, ValueError),
])
def test__delete(connectors: list, mocker: MockerFixture, kwargs, expected):
    """SnmpCommunity.delete()"""
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
    ({"uid": "NAME1", "data": {"name": "NAME1"}}, 200),
    ({"uid": "NAME3", "data": {"name": "NAME3"}}, 404),
    ({"data": {"id": "NAME1"}}, 200),
    ({"data": {"id": "NAME3"}}, 404),
])
def test__update(connectors: list, mocker: MockerFixture, kwargs, expected):
    """SnmpCommunity.update()"""
    mocker.patch("requests.Session.get",
                 side_effect=lambda *args, **kw: tst.session_get(mocker, *args, **kw))
    mocker.patch("requests.Session.put",
                 side_effect=lambda *args, **kw: tst.session_put(mocker, *args, **kw))

    for connector in connectors:
        response = connector.update(**kwargs)
        actual = response.status_code
        assert actual == expected
