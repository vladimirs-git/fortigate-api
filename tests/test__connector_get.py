"""Test connector get."""

import pytest
from pytest_mock import MockerFixture

from tests import helpers__tst as tst
from tests.helpers__tst import connectors_name, connectors_id


@pytest.mark.parametrize("kwargs, expected", [
    (dict(name="NAME1"), ["NAME1"]),  # object exists
    (dict(name="A/B"), ["A/B"]),  # object exists
    (dict(name="NAME9"), []),  # object does not exist
    (dict(name="NAME1", filter="name==NAME1"), ["NAME1"]),  # object has been found
    (dict(filter="name==NAME1"), ["NAME1"]),  # object has been found
    (dict(filter="name==NAME9"), []),  # object has not been found
    (dict(typo="NAME1"), []),  # invalid param
])
def test__get__name(connectors_name: list, mocker: MockerFixture, kwargs, expected):
    """Connector get()"""
    mocker.patch(target="requests.Session.get",
                 side_effect=lambda *args, **kw: tst.session_get(mocker, *args, **kw))

    for connector in connectors_name:
        items = connector.get(**kwargs)
        actual = [d["name"] for d in items]
        assert actual == expected


@pytest.mark.parametrize("kwargs, expected", [
    (dict(id=1), ["NAME1"]),  # object exists
    (dict(name="NAME9"), []),  # object does not exist
    (dict(typo="NAME1"), []),  # invalid param
])
def test__get__id(connectors_id: list, mocker: MockerFixture, kwargs, expected):
    """Connector get()"""
    mocker.patch(target="requests.Session.get",
                 side_effect=lambda *args, **kw: tst.session_get(mocker, *args, **kw))

    for connector in connectors_id:
        items = connector.get(**kwargs)
        actual = [d["name"] for d in items]
        assert actual == expected
