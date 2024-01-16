"""Test connector create."""

import pytest
from pytest_mock import MockerFixture

from tests import helpers__tst as tst
from tests.helpers__tst import connectors_name, connectors_id


@pytest.mark.parametrize("data, expected", [
    ({"name": "NAME1"}, 500),  # object exists
    ({"name": "A/B"}, 500),  # object exists
    ({"name": "NAME9"}, 200),  # object does not exist
    ({"typo": "NAME1"}, KeyError),  # invalid uid
])
def test__create(connectors_name: list, connectors_id: list, mocker: MockerFixture, data, expected):
    """Connector create()"""
    mocker.patch(target="requests.Session.post",
                 side_effect=lambda *args, **kw: tst.session_post(mocker, *args, **kw))

    connectors = [*connectors_name, *connectors_id]
    for connector in connectors:
        if isinstance(expected, int):
            response = connector.create(data)
            actual = response.status_code
            assert actual == expected
        else:
            with pytest.raises(expected):
                connector.create(data)
