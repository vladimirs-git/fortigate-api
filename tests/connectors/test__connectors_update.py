"""Test connector update."""

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
        api.vdoms,
        api.virtual_ip,
        api.zone,
    ]
    return items


@pytest.mark.parametrize("kwargs, expected", [
    ({"uid": "NAME1", "data": {"name": "NAME1"}}, 200),
    ({"uid": "NAME3", "data": {"name": "NAME3"}}, 404),
    ({"data": {"name": "NAME1"}}, 200),
    ({"data": {"name": "NAME3"}}, 404),
])
def test__update(connectors: list, mocker: MockerFixture, kwargs, expected):
    """Address.update()"""
    mocker.patch("requests.Session.put",
                 side_effect=lambda *args, **kw: tst.session_put(mocker, *args, **kw))

    for connector in connectors:
        response = connector.update(**kwargs)
        actual = response.status_code
        assert actual == expected
