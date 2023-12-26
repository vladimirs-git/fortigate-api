"""Test connector delete."""

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
        api.address,
        api.address_group,
        api.antivirus,
        api.application,
        api.external_resource,
        api.interface,
        api.internet_service,
        api.ip_pool,
        api.schedule,
        api.service,
        api.service_category,
        api.service_group,
        api.virtual_ip,
        api.zone,
    ]
    return items


@pytest.mark.parametrize("kwargs, expected", [
    ({"uid": "NAME1"}, 200),
    ({"uid": "NAME9"}, 404),
    ({"filter": "name==NAME1"}, 200),
    ({"filter": "name==NAME9"}, 200),  # not exist
    ({"uid": ""}, ValueError),
    ({"uid": "NAME1", "filter": "name==NAME1"}, KeyError),
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
