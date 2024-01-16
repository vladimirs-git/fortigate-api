"""Test extended_filters.py"""
import json
from typing import Any

import pytest
from pytest_mock import MockerFixture
from requests import Session, Response

from fortigate_api import extended_filters, FortiGateAPI
from fortigate_api import helpers as h

ADDR1 = {"name": "ADDR1", "type": "ipmask", "subnet": "10.0.0.0 255.255.255.252"}
ADDR3 = {"name": "ADDR3", "type": "ipmask", "subnet": "10.0.0.4 255.255.255.252"}
ADGR1 = {"name": "ADGR1", "member": [{"name": "ADDR1"}]}
ADGR3 = {"name": "ADGR3", "member": [{"name": "ADDR3"}]}
POL1 = {"policyid": 1, "name": "POL1", "srcaddr": [{"name": "ADDR1"}], "dstaddr": []}
POL3 = {"policyid": 3, "name": "POL3", "srcaddr": [{"name": "ADDR3"}], "dstaddr": []}


def create_response(method: str, url: str, status_code: int, data: Any = None) -> Response:
    """Create response."""
    resp = Response()
    resp.url = url
    resp.status_code = status_code
    data_ = {"http_method": method.upper(), "revision": "1", "status": "success"}
    if status_code >= 400:
        data_.update({"status": "error"})
    if data is not None:
        data_["results"] = data
    text = json.dumps(data_)
    resp._content = text.encode("utf-8")
    return resp


def mock_response(mocker: MockerFixture, response: Response) -> Response:
    """Crate mock based on Response"""
    resp: Response = mocker.Mock(spec=Response)
    resp.url = response.url
    resp.status_code = response.status_code
    resp.ok = response.ok  # type: ignore
    resp.reason = ""
    resp.json.return_value = response.json()  # type: ignore
    return resp


def session_get(mocker: MockerFixture, url, *args, **kwargs) -> Response:
    """Mock Session.get()"""
    _ = args, kwargs
    app_model = h.url_to_app_model(url)
    if app_model == "firewall/address":
        resp = create_response("get", url, 200, [ADDR1, ADDR3])
    elif app_model == "firewall/addrgrp":
        resp = create_response("get", url, 200, [ADGR1, ADGR3])
    elif app_model == "firewall/policy":
        resp = create_response("get", url, 200, [POL1, POL3])
    else:
        resp = create_response("get", url, 400)
    return mock_response(mocker, resp)


@pytest.fixture
def connectors():
    """Init Connector objects."""
    api = FortiGateAPI(host="host")
    api.fortigate._session = Session()
    items = [
        api.cmdb.firewall.policy,
    ]
    return items


@pytest.mark.parametrize("efilter, error", [
    (["srcaddr==1.1.1.1/32"], None),
    (["srcaddr!=1.1.1.1/32"], None),
    (["srcaddr<=1.1.1.1/32"], None),
    (["srcaddr>=1.1.1.1/32"], None),
    (["dstaddr==1.1.1.1/32"], None),
    (["dstaddr!=1.1.1.1/32"], None),
    (["dstaddr<=1.1.1.1/32"], None),
    (["dstaddr>=1.1.1.1/32"], None),
    (["srcaddr==1.1.1.1/32", "dstaddr==2.2.2.2/32"], None),
    (["srcaddr!!1.1.1.1/32"], ValueError),
    (["typo==1.1.1.1/32"], ValueError),
    (["srcaddr==1.1.1.1/32", "srcaddr==2.2.2.2/32"], ValueError),
])
def test__check_efilter(efilter, error):
    """extended_filters._check_efilter()"""
    if error is None:
        extended_filters._check_efilter(efilter=efilter)
    else:
        with pytest.raises(error):
            extended_filters._check_efilter(efilter=efilter)


@pytest.mark.parametrize("kwargs, expected", [
    (dict(efilter="srcaddr==10.0.0.0/30"), ["POL1"]),
    (dict(efilter="srcaddr==10.0.0.0/29"), []),
    (dict(efilter="srcaddr!=10.0.0.0/30"), ["POL3"]),
    (dict(efilter="srcaddr!=10.0.0.0/29"), ["POL1", "POL3"]),
    (dict(efilter="srcaddr<=10.0.0.0/32"), []),  # get all subnets
    (dict(efilter="srcaddr<=10.0.0.0/31"), []),
    (dict(efilter="srcaddr<=10.0.0.0/30"), ["POL1"]),
    (dict(efilter="srcaddr<=10.0.0.0/29"), ["POL1", "POL3"]),
    (dict(efilter="srcaddr<=0.0.0.0/0"), ["POL1", "POL3"]),
    (dict(efilter="srcaddr>=10.0.0.0"), ["POL1"]),  # get all supernets
    (dict(efilter="srcaddr>=10.0.0.0/32"), ["POL1"]),
    (dict(efilter="srcaddr>=10.0.0.0/31"), ["POL1"]),
    (dict(efilter="srcaddr>=10.0.0.0/30"), ["POL1"]),
    (dict(efilter="srcaddr>=10.0.0.0/29"), []),
    (dict(efilter="srcaddr>=0.0.0.0/0"), []),
    (dict(efilter="srcaddr=!10.0.0.0/30"), ValueError),
    (dict(efilter="typo==10.0.0.0/30"), ValueError),
    (dict(efilter="srcaddr==typo"), ValueError),
    (dict(efilter="srcaddr==10.0.0.1000"), ValueError),
    (dict(efilter="srcaddr==10.0.0.1/33"), ValueError),
    (dict(efilter="srcaddr==fd12:3456:789a:1::/64"), ValueError),
])
def test__get(connectors: list, mocker: MockerFixture, kwargs, expected):
    """Policy.get()"""
    mocker.patch(target="requests.Session.get",
                 side_effect=lambda *args, **kw: session_get(mocker, *args, **kw))

    for connector in connectors:
        if isinstance(expected, list):
            items = connector.get(**kwargs)
            actual = [d["name"] for d in items]
            assert actual == expected
        else:
            with pytest.raises(expected):
                connector.get(**kwargs)
