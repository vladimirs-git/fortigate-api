"""Test connector delete."""

import pytest
from pytest_mock import MockerFixture

from tests import helpers__tst as tst
from tests.helpers__tst import connectors_name, connectors_id


@pytest.mark.parametrize("kwargs, expected", [
    ({"uid": "NAME1"}, 200),  # object exists
    ({"uid": "NAME9"}, 404),  # object does not exist
    ({"filter": "name==NAME1"}, 200),  # object has been found
    ({"filter": "name==NAME9"}, 404),  # object has not been found
    ({"uid": ""}, ValueError),  # invalid uid
    ({"uid": "NAME1", "filter": "name==NAME1"}, ValueError),  # invalid uid
])
def test__delete__name(connectors_name: list, mocker: MockerFixture, kwargs, expected):
    """Connector delete()"""
    mocker.patch(target="requests.Session.get",
                 side_effect=lambda *args, **kw: tst.session_get(mocker, *args, **kw))
    mocker.patch(target="requests.Session.delete",
                 side_effect=lambda *args, **kw: tst.session_delete(mocker, *args, **kw))

    for connector in connectors_name:
        if isinstance(expected, int):
            response = connector.delete(**kwargs)
            actual = response.status_code
            assert actual == expected


@pytest.mark.parametrize("kwargs, expected", [
    ({"uid": 1}, 200),  # object exists
    ({"uid": "1"}, 200),  # object exists
    ({"uid": 9}, 404),  # object does not exist
    ({"uid": 0}, ValueError),  # invalid uid
])
def test__delete__id(connectors_id: list, mocker: MockerFixture, kwargs, expected):
    """Connector delete()"""
    mocker.patch(target="requests.Session.get",
                 side_effect=lambda *args, **kw: tst.session_get(mocker, *args, **kw))
    mocker.patch(target="requests.Session.delete",
                 side_effect=lambda *args, **kw: tst.session_delete(mocker, *args, **kw))

    for connector in connectors_id:
        if isinstance(expected, int):
            response = connector.delete(**kwargs)
            actual = response.status_code
            assert actual == expected
        else:
            with pytest.raises(expected):
                connector.delete(**kwargs)
