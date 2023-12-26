"""Test connector get."""

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


@pytest.mark.parametrize("kwargs, expected", [
    (dict(uid="NAME1"), ["NAME1"]),
    (dict(uid="NAME1", filter="name==NAME1"), ["NAME1"]),
    (dict(uid="NAME9"), []),
    (dict(uid="A/B"), ["A/B"]),
    (dict(filter="name==NAME9"), []),
    (dict(filter="name==NAME1"), ["NAME1"]),
    (dict(id="NAME1"), KeyError),
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
