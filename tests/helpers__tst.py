"""Helper for tests."""
from __future__ import annotations

import json
from http.cookiejar import Cookie
from typing import Any
from urllib.parse import urlparse

from pytest_mock import MockerFixture
from requests import Response, Session

from fortigate_api import helpers as h

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
    """Mock Session.delete()"""
    _ = args, kwargs
    app_model = h.url_to_app_model(url)
    if app_model in UID_NAME:
        resp = connector_delete(url)
    elif app_model == "firewall/policy":
        resp = policy_delete(url)
    else:
        resp = create_response("delete", url, 400)
    return mock_response(mocker, resp)


def session_get(mocker: MockerFixture, url, *args, **kwargs) -> Response:
    """Mock Session.get()"""
    _ = args, kwargs
    app_model = h.url_to_app_model(url)
    if app_model in UID_NAME:
        resp = connector_get(url)
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
        resp = connector_post(url, data=kwargs)
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
        resp = connector_put(url)
    elif app_model == "firewall/policy":
        resp = policy_put(url)
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
        ("NAME1", "filter=name%3D%3DNAME1"): 200,
        ("NAME9", ""): 404,  # not exist
        ("", "filter=name%3D%3DNAME1"): 200,
    }.get(key, 0)
    return create_response("delete", url, status_code)


def connector_get(url: str) -> Response:
    """Get"""
    uid = h.url_to_uid(url)
    query = urlparse(url).query
    key = (uid, query)
    items = {
        ("", ""): [NAME1, NAME3],
        ("A%2FB", ""): [SLASH],
        ("NAME1", ""): [NAME1],
        ("NAME1", "filter=name%3D%3DNAME1"): [NAME1],
        ("", "filter=name%3D%3DNAME1"): [NAME1],
    }.get(key)
    if items is not None:
        return create_response("get", url, 200, items)
    return create_response("get", url, 404, [])


def connector_post(url: str, data: dict) -> Response:
    """Create"""
    data = json.loads(data["data"])
    uid = data["name"]
    status_code = {
        "NAME1": 500,  # exist
        "NAME2": 200,  # not exist
    }[uid]
    return create_response("post", url, status_code)


def connector_put(url: str) -> Response:
    """Update"""
    uid = h.url_to_uid(url)
    status_code = {
        "NAME1": 200,  # exist
        "NAME3": 404,  # not exist
    }[uid]
    return create_response("get", url, status_code)


# ============================== policy ==============================

def policy_delete(url: str) -> Response:
    """Delete"""
    uid = h.url_to_uid(url)
    status_code = {
        "1": 200,  # exist
        "2": 404,  # not exist
    }[uid]
    return create_response("delete", url, status_code)


def policy_get(url: str) -> Response:
    """Get"""
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
        return create_response("get", url, 200, items)
    return create_response("get", url, 404)


def policy_post(url: str, data: dict) -> Response:
    """Create"""
    data = json.loads(data["data"])
    name = data["name"]
    status_code = {
        "POL1": 500,  # exist
        "POL2": 200,  # not exist
    }[name]
    return create_response("post", url, status_code)


def policy_put(url: str) -> Response:
    """Update"""
    uid = h.url_to_uid(url)
    status_code = {
        "1": 200,  # exist
        "2": 404,  # not exist
        "4": 500,  # not moved, only for policy.move()
    }[uid]
    return create_response("put", url, status_code)
