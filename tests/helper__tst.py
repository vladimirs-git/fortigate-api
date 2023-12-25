"""Helper for unittests."""
from __future__ import annotations

import json
from http.cookiejar import Cookie
from typing import Any
from urllib.parse import urlparse

from pytest_mock import MockerFixture
from requests import Response, Session

from fortigate_api import helpers as h

ADDR1 = {"name": "ADDR1", "type": "ipmask", "subnet": "10.0.0.0 255.255.255.252"}
ADDR3 = {"name": "ADDR3", "type": "ipmask", "subnet": "10.0.0.4 255.255.255.252"}
ADGR1 = {"name": "ADGR1", "member": [{"name": "ADDR1"}]}
ADGR3 = {"name": "ADGR3", "member": [{"name": "ADDR3"}]}
INTF1 = {"name": "INTF1", "vdom": "root"}
INTF3 = {"name": "INTF3", "vdom": "vdom3"}
NAME1 = {"name": "NAME1"}
NAME3 = {"name": "NAME3"}


URL_BASE = "/api/v2/cmdb/firewall/"
UID_NAME = [
    "antivirus/profile",
    "application/list",
    "firewall.schedule/onetime",
    "firewall.service/category",
    "firewall.service/custom",
    "firewall.service/group",
    "firewall/address",
    "firewall/addrgrp",
    "firewall/internet-service",
    "firewall/ippool",
    "firewall/vip",
    "system/external-resource",
    "system/zone",
    "system/interface",
    "system.snmp/community",
]



def create_cookie(name: str, value: str) -> Cookie:
    """Return Cookie object."""
    return Cookie(
        version=0,
        name=name,
        value=value,
        port=None,
        port_specified=False,
        domain="host.local",
        domain_specified=False,
        domain_initial_dot=False,
        path="/",
        path_specified=True,
        secure=True,
        expires=None,
        discard=True,
        comment=None,
        comment_url=None,
        rest={},
    )


def crate_response(status_code: int) -> Response:
    """Return Response object with status_code=200."""
    response = Response()
    response.status_code = status_code
    return response


def create_session_w_cookie(name: str, value: str) -> Session:
    """Return Session object with cookies."""
    cookie = create_cookie(name, value)
    session = Session()
    session.cookies = [cookie]  # type: ignore
    return session


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


# ============================= session ==============================

def session_delete(mocker: MockerFixture, url, *args, **kwargs) -> Response:
    """Mock Session.delete(), delete"""
    _ = args, kwargs
    app_model = h.url_to_app_model(url)
    if app_model in UID_NAME:
        resp = address_delete(url)
    elif app_model == "firewall/policy":
        resp = policy_delete(url)
    else:
        resp = create_response("delete", url, 400)
    return mock_response(mocker, resp)


def session_get(mocker: MockerFixture, url, *args, **kwargs) -> Response:
    """Mock Session.get(), get"""
    _ = args, kwargs
    app_model = h.url_to_app_model(url)
    if app_model in UID_NAME:
        resp = address_get(url)
    elif app_model == "firewall/policy":
        resp = policy_get(url)
    else:
        resp = create_response("get", url, 400)
    return mock_response(mocker, resp)


def session_post(mocker: MockerFixture, url, *args, **kwargs) -> Response:
    """Mock Session.post(), create"""
    _ = args, kwargs
    app_model = h.url_to_app_model(url)
    if app_model in UID_NAME:
        resp = address_post(url, data=kwargs)
    elif app_model == "firewall/policy":
        resp = policy_post(url, data=kwargs)
    else:
        resp = create_response("post", url, 400)
    return mock_response(mocker, resp)


def session_put(mocker: MockerFixture, url, *args, **kwargs) -> Response:
    """Mock Session.put(), update"""
    _ = args, kwargs
    app_model = h.url_to_app_model(url)
    if app_model in UID_NAME:
        resp = address_put(url)
    elif app_model == "firewall/policy":
        resp = policy_put(url)
    else:
        resp = create_response("put", url, 400)
    return mock_response(mocker, resp)


# ============================= address ==============================


def address_delete(url: str) -> Response:
    """Delete."""
    uid = h.url_to_uid(url)
    query = urlparse(url).query
    key = (uid, query)
    status_code = {
        # address
        ("ADDR1", ""): 200,
        ("ADDR1", "filter=name%3D%3DADDR1"): 200,
        ("ADDR9", ""): 404,
        ("", "filter=name%3D%3DADDR1"): 200,
        ("", "filter=name%3D%3DADDR9"): 404,
        # address_group
        ("ADGR1", ""): 200,
        ("ADGR1", "filter=name%3D%3DADGR1"): 200,
        ("ADGR9", ""): 404,
        ("", "filter=name%3D%3DADGR1"): 200,
        ("", "filter=name%3D%3DADGR9"): 404,
        # interface
        ("INTF1", ""): 200,
        ("INTF1", "filter=name%3D%3DINTF1"): 200,
        ("INTF9", ""): 404,
        ("", "filter=name%3D%3DINTF1"): 200,
        ("", "filter=name%3D%3DINTF9"): 404,
        # name
        ("A%2FB", ""): 200,
        ("NAME1", ""): 200,
        ("NAME1", "filter=name%3D%3DNAME1"): 200,
        ("NAME9", ""): 404,
        ("", "filter=name%3D%3DNAME1"): 200,
        ("", "filter=name%3D%3DNAME9"): 404,
    }.get(key)
    return create_response("delete", url, status_code)


def address_get(url: str) -> Response:
    """Get."""
    uid = h.url_to_uid(url)
    query = urlparse(url).query
    key = (uid, query)

    app_model = h.url_to_app_model(url)
    if app_model == "firewall/address":
        items = {
            ("", ""): [ADDR1, ADDR3],
            ("A%2FB", ""): [{"name": "A/B"}],
            ("ADDR1", ""): [ADDR1],
            ("ADDR1", "filter=name%3D%3DADDR1"): [ADDR1],
            ("", "filter=name%3D%3DADDR1"): [ADDR1],
            ("", "filter=name%3D%3DADDR9"): [],
        }.get(key)
    elif app_model == "firewall/addrgrp":
        items = {
            ("", ""): [ADGR1, ADGR3],
            ("A%2FB", ""): [{"name": "A/B"}],
            ("ADGR1", ""): [ADGR1],
            ("ADGR1", "filter=name%3D%3DADGR1"): [ADGR1],
            ("", "filter=name%3D%3DADGR1"): [ADGR1],
            ("", "filter=name%3D%3DADDR9"): [],
        }.get(key)
    elif app_model == "system/interface":
        items = {
            ("", ""): [INTF1, INTF3],  # all
            ("INTF1", ""): [INTF1],  # root
            ("INTF1", "filter=name%3D%3DINTF1"): [INTF1],
            ("INTF3", ""): [INTF3],  # vdom3
            ("", "filter=name%3D%3DINTF1"): [INTF1],
            ("", "filter=name%3D%3DINTF9"): [],
            ("", "filter=name%3D%3DINTF3"): [INTF3],
        }.get(key)
    else:
        items = {
            ("", ""): [NAME1, NAME3],
            ("A%2FB", ""): [{"name": "A/B"}],
            ("NAME1", ""): [NAME1],
            ("NAME1", "filter=name%3D%3DNAME1"): [NAME1],
            ("", "filter=name%3D%3DNAME1"): [NAME1],
            ("", "filter=name%3D%3DNAME9"): [],
        }.get(key)
    if items is not None:
        return create_response("get", url, 200, items)
    return create_response("get", url, 404, [])


def address_post(url: str, data: dict) -> Response:
    """Create."""
    data = json.loads(data["data"])
    uid = data["name"]
    status_code = {
        "ADDR1": 500,
        "ADDR2": 200,
        "ADGR1": 500,
        "ADGR2": 200,
        "NAME1": 500,
        "NAME2": 200,
    }[uid]
    return create_response("post", url, status_code)


def address_put(url: str) -> Response:
    """Update."""
    uid = h.url_to_uid(url)
    status_code = {
        "ADDR1": 200,
        "ADDR3": 404,
        "ADGR1": 200,
        "ADGR3": 404,
        "INTF1": 200,  # root
        "INTF3": 200,  # vdom3
        "INTF9": 404,
        "NAME1": 200,
        "NAME3": 404,
    }[uid]
    return create_response("get", url, status_code)


# ============================== policy ==============================
POL1 = {"policyid": 1, "name": "POL1", "srcaddr": [{"name": "ADDR1"}], "dstaddr": []}
POL3 = {"policyid": 3, "name": "POL3", "srcaddr": [{"name": "ADDR3"}], "dstaddr": []}


def policy_delete(url: str) -> Response:
    uid = h.url_to_uid(url)
    status_code = {"1": 200, "2": 404}[uid]
    return create_response("delete", url, status_code)


def policy_get(url: str) -> Response:
    uid = h.url_to_uid(url)
    query = urlparse(url).query
    key = (uid, query)
    items = {
        ("", ""): [POL1, POL3],
        ("", "filter=name%3D%3DPOL1"): [POL1],
        ("1", ""): [POL1],
        ("1", "filter=name%3D%3DPOL1"): [POL1],
        ("2", ""): [],
    }.get(key)
    if items is not None:
        resp = create_response("get", url, 200, items)
    else:
        resp = create_response("get", url, 404)
    return resp


def policy_put(url: str) -> Response:
    uid = h.url_to_uid(url)
    status_code = {
        "1": 200,  # exist
        "2": 404,  # not exist
        "4": 500,  # not moved, only for policy.move()
    }[uid]
    return create_response("put", url, status_code)


def policy_post(url: str, data: dict) -> Response:
    data = json.loads(data["data"])
    name = data["name"]
    status_code = {
        "POL1": 500,
        "POL2": 200,
    }[name]
    return create_response("post", url, status_code)
