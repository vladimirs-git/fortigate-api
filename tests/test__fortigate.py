"""Test fortigate.py"""

import pytest
from pytest_mock import MockerFixture
from requests import Session

from fortigate_api.fortigate import FortiGate
from tests import helpers__tst as tst


@pytest.fixture
def api():
    """Init FortiGate"""
    api_o = FortiGate(host="host")
    api_o._session = Session()
    return api_o


# =========================== methods ============================

@pytest.mark.parametrize("url, expected", [
    ("https://host/api/v2/cmdb/firewall/policy/1", 200),
    ("https://host/api/v2/cmdb/firewall/policy/2", 404),
    ("https://host/api/v2/cmdb/firewall/typo/1", 400),
])
def test__delete(api: FortiGate, mocker: MockerFixture, url, expected):
    """FortiGate.delete()"""
    mocker.patch(target="requests.Session.delete",
                 side_effect=lambda *args, **kw: tst.session_delete(mocker, *args, **kw))
    response = api.delete(url=url)
    actual = response.status_code
    assert actual == expected


@pytest.mark.parametrize("url, expected", [
    ("https://host/api/v2/cmdb/firewall.ipmacbinding/setting", {"bindthroughfw": "disable"}),
    ("https://host/api/v2/cmdb/firewall/policy/1", [{"name": "POL1", "policyid": 1}]),
])
def test__get(api: FortiGate, mocker: MockerFixture, url, expected):
    """FortiGate.get()"""
    mocker.patch(target="requests.Session.get",
                 side_effect=lambda *args, **kw: tst.session_get(mocker, *args, **kw))
    response = api.get(url=url)
    data = response.json()
    assert data["http_method"] == "GET"
    results = data["results"]
    assert results == expected


@pytest.mark.parametrize("url, expected", [
    ("https://host/api/v2/cmdb/firewall.ipmacbinding/setting", {"bindthroughfw": "disable"}),
])
def test__get_result(api: FortiGate, mocker: MockerFixture, url, expected):
    """FortiGate.get_result()"""
    mocker.patch(target="requests.Session.get",
                 side_effect=lambda *args, **kw: tst.session_get(mocker, *args, **kw))
    actual = api.get_result(url=url)
    assert actual == expected


@pytest.mark.parametrize("url, expected", [
    ("https://host/api/v2/cmdb/firewall/policy/1", [1]),
    ("https://host/api/v2/cmdb/firewall/policy/2", []),
    ("https://host/api/v2/cmdb/firewall/typo/1", []),
])
def test__get_results(api: FortiGate, mocker: MockerFixture, url, expected):
    """FortiGate.get_results()"""
    mocker.patch(target="requests.Session.get",
                 side_effect=lambda *args, **kw: tst.session_get(mocker, *args, **kw))
    result = api.get_results(url=url)
    actual = [d["policyid"] for d in result]
    assert actual == expected


@pytest.mark.parametrize("url, data, expected", [
    ("https://host/api/v2/cmdb/firewall/policy/1", {"name": "POL1"}, 500),
    ("https://host/api/v2/cmdb/firewall/policy/2", {"name": "POL2"}, 200),
    ("https://host/api/v2/cmdb/firewall/typo/2", {"name": "POL2"}, 400),
])
def test__post(api: FortiGate, mocker: MockerFixture, url, data, expected):
    """FortiGate.post()"""
    mocker.patch(target="requests.Session.post",
                 side_effect=lambda *args, **kw: tst.session_post(mocker, *args, **kw))
    response = api.post(url=url, data=data)
    actual = response.status_code
    assert actual == expected


@pytest.mark.parametrize("url, expected", [
    ("https://host/api/v2/cmdb/firewall/policy/1", 200),
    ("https://host/api/v2/cmdb/firewall/policy/2", 404),
    ("https://host/api/v2/cmdb/firewall/typo/1", 400),
])
def test__put(api: FortiGate, mocker: MockerFixture, url, expected):
    """FortiGate.put()"""
    mocker.patch(target="requests.Session.put",
                 side_effect=lambda *args, **kw: tst.session_put(mocker, *args, **kw))
    response = api.put(url=url, data={"name": "POL1"})
    actual = response.status_code
    assert actual == expected


@pytest.mark.parametrize("url, expected", [
    ("https://host/api/v2/cmdb/firewall/policy/1", 200),
    ("https://host/api/v2/cmdb/firewall/policy/3", 404),
    ("https://host/api/v2/cmdb/firewall/typo/1", 400),
])
def test__exist(api: FortiGate, mocker: MockerFixture, url, expected):
    """FortiGate.exist()"""
    mocker.patch(target="requests.Session.get",
                 side_effect=lambda *args, **kw: tst.session_get(mocker, *args, **kw))
    response = api.exist(url=url)
    actual = response.status_code
    assert actual == expected
