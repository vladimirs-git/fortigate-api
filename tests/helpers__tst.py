"""Helper for tests."""
from __future__ import annotations

import json
from http.cookiejar import Cookie
from typing import Any
from urllib.parse import urlparse

import pytest
from pytest_mock import MockerFixture
from requests import Response, Session

from fortigate_api import helpers as h, FortiGateAPI

NAME1 = {
    "name": "NAME1",
    "vdom": "root",  # interface
}
NAME3 = {
    "name": "NAME3",
    "vdom": "vdom3",  # interface
}
POL1 = {
    "policyid": 1,
    "name": "POL1",
}
POL3 = {
    "policyid": 3,
    "name": "POL3",
}
SLASH = {
    "name": "A/B",
    "vdom": "root",  # interface
}

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
    "firewall/ippool",
    "firewall/vip",
    "system/external-resource",
    "system/interface",
    "system/vdom",
    "system/zone",
]
UID_ID = [
    "firewall/internet-service",
    "firewall/policy",
    "system.snmp/community",
]


@pytest.fixture
def connectors_name():
    """Init Connector with uid key="name"."""
    api = FortiGateAPI(host="host")
    api.fortigate._session = Session()
    items = [
        api.cmdb.antivirus.profile,
        api.cmdb.application.list,
        api.cmdb.firewall.address,
        api.cmdb.firewall.addrgrp,
        api.cmdb.firewall.ippool,
        api.cmdb.firewall.vip,
        api.cmdb.firewall_schedule.onetime,
        api.cmdb.firewall_service.category,
        api.cmdb.firewall_service.custom,
        api.cmdb.firewall_service.group,
        api.cmdb.system.external_resource,
        api.cmdb.system.interface,
        api.cmdb.system.vdom,
        api.cmdb.system.zone,
    ]
    return items


@pytest.fixture
def connectors_id():
    """Init Connector with uid key="id"."""
    api = FortiGateAPI(host="host")
    api.fortigate._session = Session()
    items = [
        # api.cmdb.firewall.internet_service,
        api.cmdb.system_snmp.community,
    ]
    return items


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
    """Mock Session.delete()"""
    _ = args, kwargs
    app_model = h.url_to_app_model(url)
    if app_model in UID_NAME:
        resp = connector_delete(url)
    elif app_model == "firewall/policy":
        resp = firewall_policy_delete(url)
    elif app_model in UID_ID:
        resp = firewall_policy_delete(url)
    # invalid url
    else:
        resp = create_response("delete", url, 400)
    return mock_response(mocker, resp)


def session_get(mocker: MockerFixture, url, *args, **kwargs) -> Response:
    """Mock Session.get()"""
    _ = args, kwargs
    app_model = h.url_to_app_model(url)
    if app_model in UID_NAME:
        resp = connector_get_name(url)
    elif app_model == "firewall/policy":
        resp = firewall_policy_get(url)
    elif app_model == "firewall.ipmacbinding/setting":
        resp = firewall_ipmacbinding_setting_get(url)
    elif app_model in UID_ID:
        resp = connector_get_id(url)
    # invalid url
    else:
        resp = create_response("get", url, 400)
    return mock_response(mocker, resp)


def session_post(mocker: MockerFixture, url, *args, **kwargs) -> Response:
    """Mock Session.post(), create"""
    _ = args, kwargs
    app_model = h.url_to_app_model(url)
    if app_model in UID_NAME:
        resp = connector_post(url, data=kwargs)
    elif app_model == "firewall/policy":
        resp = firewall_policy_post(url, data=kwargs)
    elif app_model in UID_ID:
        resp = connector_post(url, data=kwargs)
    # invalid url
    else:
        resp = create_response("post", url, 400)
    return mock_response(mocker, resp)


def session_put(mocker: MockerFixture, url, *args, **kwargs) -> Response:
    """Mock Session.put(), update"""
    _ = args, kwargs
    app_model = h.url_to_app_model(url)
    if app_model in UID_NAME:
        resp = connector_put(url)
    elif app_model == "firewall/policy":
        resp = firewall_policy_put(url)
    elif app_model in UID_ID:
        resp = firewall_policy_put(url)
    # invalid url
    else:
        resp = create_response("put", url, 400)
    return mock_response(mocker, resp)


# ============================ connector =============================

def connector_delete(url: str) -> Response:
    """Delete"""
    uid = h.url_to_uid(url)
    query = urlparse(url).query
    key = (uid, query)
    status_code = {
        ("A%2FB", ""): 200,
        ("NAME1", ""): 200,
    }.get(key, 404)
    return create_response("delete", url, status_code)


def connector_get_name(url: str) -> Response:
    """Get"""
    uid = h.url_to_uid(url)
    query = urlparse(url).query
    key = (uid, query)
    items = {
        ("", ""): [NAME1, NAME3],
        ("A%2FB", ""): [SLASH],
        ("NAME1", ""): [NAME1],
        ("NAME3", ""): [NAME3],  # interface
        ("NAME1", "filter=name%3D%3DNAME1"): [NAME1],
        ("", "filter=name%3D%3DNAME1"): [NAME1],
    }.get(key)
    status_code = 404 if items is None else 200
    return create_response("get", url, status_code, data=items)


def connector_get_id(url: str) -> Response:
    """Get"""
    uid = h.url_to_uid(url)
    query = urlparse(url).query
    key = (uid, query)
    items = {
        ("", ""): [NAME1, NAME3],
        ("1", ""): [NAME1],
    }.get(key)
    status_code = 404 if items is None else 200
    return create_response("get", url, status_code, data=items)


def connector_post(url: str, data: dict) -> Response:
    """Create"""
    data = json.loads(data["data"])
    uid = data["name"]
    status_code = {
        "NAME1": 500,  # exist
        "A/B": 500,
    }.get(uid, 200)
    return create_response("post", url, status_code)


def connector_put(url: str) -> Response:
    """Update"""
    uid = h.url_to_uid(url)
    status_code = {
        "NAME1": 200,  # exist
    }.get(uid, 404)
    return create_response("get", url, status_code)


# ======================= cmdb/firewall/policy =======================

def firewall_policy_delete(url: str) -> Response:
    """Delete"""
    uid = h.url_to_uid(url)
    status_code = {
        "1": 200,  # exist
    }.get(uid, 404)
    return create_response("delete", url, status_code)


def firewall_policy_get(url: str) -> Response:
    """Get"""
    uid = h.url_to_uid(url)
    query = urlparse(url).query
    key = (uid, query)
    items = {
        ("", ""): [POL1, POL3],
        ("", "filter=name%3D%3DPOL1"): [POL1],
        ("", "filter=policyid%3D%3D1"): [POL1],
        ("1", ""): [POL1],
        ("1", "filter=name%3D%3DPOL1"): [POL1],
        ("2", ""): [],
    }.get(key)
    status_code = 404 if items is None else 200
    return create_response("get", url, status_code, data=items)


def firewall_policy_post(url: str, data: dict) -> Response:
    """Create"""
    data = json.loads(data["data"])
    name = data["name"]
    status_code = {
        "POL1": 500,  # exist
    }.get(name, 200)
    return create_response("post", url, status_code)


def firewall_policy_put(url: str) -> Response:
    """Update"""
    uid = h.url_to_uid(url)
    status_code = {
        "1": 200,  # exist
        "4": 500,  # not moved, only for policy.move()
    }.get(uid, 404)
    return create_response("put", url, status_code)


# ======================= cmdb/firewall/policy =======================

def firewall_ipmacbinding_setting_get(url: str) -> Response:
    """Get"""
    uid = h.url_to_uid(url)
    query = urlparse(url).query
    key = (uid, query)
    items = {
        ("", ""): {"bindthroughfw": "disable"},
    }.get(key)
    status_code = 404 if items is None else 200
    return create_response("get", url, status_code, data=items)
