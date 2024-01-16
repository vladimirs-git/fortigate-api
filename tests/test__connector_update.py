"""Test connector update."""

import pytest
from pytest_mock import MockerFixture

from tests import helpers__tst as tst
from tests.helpers__tst import connectors_name, connectors_id


@pytest.mark.parametrize("data, expected", [
    ({"name": "NAME1"}, 200),  # object exists
    ({"name": "NAME9"}, 404),  # object does not exist
])
def test__update__name(connectors_name: list, mocker: MockerFixture, data, expected):
    """Connector update()"""
    mocker.patch(target="requests.Session.put",
                 side_effect=lambda *args, **kw: tst.session_put(mocker, *args, **kw))

    for connector in connectors_name:
        response = connector.update(data=data)
        actual = response.status_code
        assert actual == expected


@pytest.mark.parametrize("data, expected", [
    ({"id": 1}, 200),  # object exists
    ({"id": 9}, 404),  # object does not exist
])
def test__update__id(connectors_id: list, mocker: MockerFixture, data, expected):
    """Connector update()"""
    mocker.patch(target="requests.Session.put",
                 side_effect=lambda *args, **kw: tst.session_put(mocker, *args, **kw))

    for connector in connectors_id:
        response = connector.update(data=data)
        actual = response.status_code
        assert actual == expected
