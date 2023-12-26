"""Helper for efilters tests."""
from __future__ import annotations

from pytest_mock import MockerFixture
from requests import Response

from fortigate_api import helpers as h
from tests import helpers__tst as tst

ADDR1 = {"name": "ADDR1", "type": "ipmask", "subnet": "10.0.0.0 255.255.255.252"}
ADDR3 = {"name": "ADDR3", "type": "ipmask", "subnet": "10.0.0.4 255.255.255.252"}
ADGR1 = {"name": "ADGR1", "member": [{"name": "ADDR1"}]}
ADGR3 = {"name": "ADGR3", "member": [{"name": "ADDR3"}]}
POL1 = {"policyid": 1, "name": "POL1", "srcaddr": [{"name": "ADDR1"}], "dstaddr": []}
POL3 = {"policyid": 3, "name": "POL3", "srcaddr": [{"name": "ADDR3"}], "dstaddr": []}


def session_get(mocker: MockerFixture, url, *args, **kwargs) -> Response:
    """Mock Session.get()"""
    _ = args, kwargs
    app_model = h.url_to_app_model(url)
    if app_model == "firewall/address":
        resp = tst.create_response("get", url, 200, [ADDR1, ADDR3])
    elif app_model == "firewall/addrgrp":
        resp = tst.create_response("get", url, 200, [ADGR1, ADGR3])
    elif app_model == "firewall/policy":
        resp = tst.create_response("get", url, 200, [POL1, POL3])
    else:
        resp = tst.create_response("get", url, 400)
    return tst.mock_response(mocker, resp)
