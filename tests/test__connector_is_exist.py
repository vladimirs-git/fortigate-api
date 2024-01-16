"""Test connector is_exist."""

import pytest
from pytest_mock import MockerFixture

from tests import helpers__tst as tst
from tests.helpers__tst import connectors_name, connectors_id


@pytest.mark.parametrize("uid, expected", [
    ("NAME1", True),  # object exists
    ("NAME9", False),  # object does not exist
])
def test__is_exist__name(connectors_name: list, mocker: MockerFixture, uid, expected):
    """Connector is_exist()"""
    mocker.patch(target="requests.Session.get",
                 side_effect=lambda *args, **kw: tst.session_get(mocker, *args, **kw))

    for connector in connectors_name:
        actual = connector.is_exist(uid=uid)
        assert actual == expected, connector


@pytest.mark.parametrize("uid, expected", [
    (1, True),  # object exists
    (9, False),  # object does not exist
])
def test__is_exist__id(connectors_id: list, mocker: MockerFixture, uid, expected):
    """Connector is_exist()"""
    mocker.patch(target="requests.Session.get",
                 side_effect=lambda *args, **kw: tst.session_get(mocker, *args, **kw))

    for connector in connectors_id:
        actual = connector.is_exist(uid=uid)
        assert actual == expected, connector
