"""Test connector is_exist."""

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
        api.snmp_community,
        api.vdoms,
        api.virtual_ip,
        api.zone,
    ]
    return items


@pytest.mark.parametrize("uid, expected", [
    ("NAME1", True),
    ("NAME9", False),
])
def test__is_exist(connectors: list, mocker: MockerFixture, uid, expected):
    """Address.is_exist()"""
    mocker.patch("requests.Session.get",
                 side_effect=lambda *args, **kw: tst.session_get(mocker, *args, **kw))

    for connector in connectors:
        actual = connector.is_exist(uid=uid)
        assert actual == expected, connector
