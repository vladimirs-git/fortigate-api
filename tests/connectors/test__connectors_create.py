"""Test connector create."""

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
        api.virtual_ip,
        api.zone,
    ]
    return items


@pytest.mark.parametrize("data, expected", [
    ({"name": "NAME1"}, 200),  # already exist
    ({"name": "NAME2"}, 200),  # not exist
    ({"name": "A/B"}, 200),  # already exist
    ({"typo": "NAME1"}, KeyError),
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
