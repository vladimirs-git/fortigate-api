"""Test connector create."""
from typing import Any

import pytest
from pytest_mock import MockerFixture

from tests import helpers__tst as tst
from tests.helpers__tst import connectors_name, connectors_id, connectors_wo_uid


@pytest.mark.parametrize("data, expected", [
    ({"name": "NAME1"}, 500),  # object exists
    ({"name": "A/B"}, 500),  # object exists
    ({"name": "NAME9"}, 200),  # object does not exist
    ({"typo": "NAME1"}, KeyError),  # invalid uid
])
def test__create(connectors_name: list, connectors_id: list, mocker: MockerFixture, data, expected):
    """Connector create() uid is str."""
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


@pytest.mark.parametrize("kwargs, expected", [
    ({"uid": "NAME1"}, 200),  # object exists
    ({"uid": "NAME9"}, 404),  # object does not exist
    ({"filter": "name==NAME1"}, 200),  # object has been found
    ({"filter": "name==NAME9"}, 404),  # object has not been found
    ({"uid": ""}, ValueError),  # invalid uid
    ({"uid": "NAME1", "filter": "name==NAME1"}, ValueError),  # invalid uid
])
def test__delete__name(connectors_name: list, mocker: MockerFixture, kwargs, expected):
    """Connector.delete() uid is str."""
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
    """Connector.delete() uid is int."""
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
    """Connector.get() uid is str."""
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
    """Connector.get() uid is int."""
    mocker.patch(target="requests.Session.get",
                 side_effect=lambda *args, **kw: tst.session_get(mocker, *args, **kw))

    for connector in connectors_id:
        items = connector.get(**kwargs)
        actual = [d["name"] for d in items]
        assert actual == expected


@pytest.mark.parametrize("kwargs, expected", [
    (dict(key="value"), ["value"]),  # object exists
    (dict(typo="value"), [None]),  # object does not exist
])
def test__get__wo_uid(connectors_wo_uid: list, mocker: MockerFixture, kwargs, expected):
    """Connector.get() without uid."""
    mocker.patch(target="requests.Session.get",
                 side_effect=lambda *args, **kw: tst.session_get(mocker, *args, **kw))

    for connector in connectors_wo_uid:
        items = connector.get(**kwargs)
        actual = [d.get("key") for d in items]
        assert actual == expected


@pytest.mark.parametrize("uid, expected", [
    ("NAME1", True),  # object exists
    ("NAME9", False),  # object does not exist
])
def test__is_exist__name(connectors_name: list, mocker: MockerFixture, uid, expected):
    """Connector.is_exist() uid is str."""
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
    """Connector.is_exist() uid is int."""
    mocker.patch(target="requests.Session.get",
                 side_effect=lambda *args, **kw: tst.session_get(mocker, *args, **kw))

    for connector in connectors_id:
        actual = connector.is_exist(uid=uid)
        assert actual == expected, connector


@pytest.mark.parametrize("data, expected", [
    (dict(name="NAME1"), 200),  # object exists
    (dict(name="NAME9"), 404),  # object does not exist
])
def test__update__name(connectors_name: list, mocker: MockerFixture, data, expected):
    """Connector.update() uid is str."""
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
    """Connector.update() uid is int."""
    mocker.patch(target="requests.Session.put",
                 side_effect=lambda *args, **kw: tst.session_put(mocker, *args, **kw))

    for connector in connectors_id:
        response = connector.update(data=data)
        actual = response.status_code
        assert actual == expected


@pytest.mark.parametrize("data, expected", [
    ({"key": "value"}, 200),  # object exists
    ({"typo": "value"}, 404),  # object does not exist
])
def test__update__wo_uid(connectors_wo_uid: list, mocker: MockerFixture, data, expected):
    """Connector.update() without uid."""
    mocker.patch(target="requests.Session.put",
                 side_effect=lambda *args, **kw: tst.session_put(mocker, *args, **kw))

    for connector in connectors_wo_uid:
        response = connector.update(data=data)
        actual = response.status_code
        assert actual == expected


@pytest.mark.parametrize("uid, data, expected", [
    ("", {}, ""),
    ("", {"name": "NAME"}, ""),
    ("policyid", {"policyid": 0}, "0"),
    ("policyid", {"policyid": 1}, "1"),
    ("name", {"name": "NAME"}, "NAME"),
    ("name", {"typo": "NAME"}, ValueError),
    ("name", {"name": "A/B"}, "A%2FB"),
])
def test__get_uid(connectors_name: list, uid, data, expected: Any):
    """Connector._get_uid()"""
    connector = connectors_name[0]
    connector.uid = uid
    if isinstance(expected, str):
        actual = connector._get_uid(data=data)
        assert actual == expected
    else:
        with pytest.raises(expected):
            connector._get_uid(data=data)
