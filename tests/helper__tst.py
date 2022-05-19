"""Helper for unittests"""
from __future__ import annotations

import json
import unittest
from unittest.mock import patch

from requests import Response  # type: ignore

from fortigate_api.base.object_base import ObjectBase
from fortigate_api.fortigate import Fortigate

NAME1, NAME2, NAME3, SLASH, SLASH_ = "NAME1", "NAME2", "NAME3", "A/B", "A%2FB"


class MockFortigate(unittest.TestCase):
    """mocked Fortigate"""

    def setUp(self):
        """setUp"""
        patch.object(Fortigate, "login", return_value=MockSession()).start()
        self.fgt = Fortigate(host="domain.com", username="", password="")


CONTENT_INTERFACE = b"""{"http_method": "GET", "revision": "1",
                         "results": [{"name": "NAME1", "vdom": "root"}]}"""
CONTENT_OBJECT = b"""{"http_method": "GET", "revision": "1",
                      "results": [{"name": "NAME1"}]}"""
CONTENT_POLICY1 = b"""{"http_method": "GET", "revision": "1",
                       "results": [{"name": "NAME1", "policyid": "1"}]}"""
CONTENT_POLICY3 = b"""{"http_method": "GET", "revision": "1",
                       "results": [{"name": "NAME3", "policyid": "3"}]}"""
CONTENT_SLASH = b"""{"http_method": "GET", "revision": "1",
                     "results": [{"name": "A%2FB"}]}"""
CONTENT_SNMP1 = b"""{"http_method": "GET", "revision": "1",
                     "results": [{"name": "NAME1", "id": "1"}]}"""
CONTENT_SNMP3 = b"""{"http_method": "GET", "revision": "1",
                     "results": [{"name": "NAME1", "id": "3"}]}"""
CONTENT_ZONE = b"""{"http_method": "GET", "revision": "1",
                    "results": [{"name": "NAME1", "interface": [{"interface-name": "NAME1"}]}]}"""


class MockSession:
    """mocked Session"""

    # noinspection PyUnusedLocal
    @staticmethod
    def delete(url: str, **kwargs) -> Response:
        """mocked Session.delete()"""
        return MockResponse.delete(url=url)

    # noinspection PyUnusedLocal
    @staticmethod
    def get(url: str, **kwargs) -> Response:
        """mocked Session.get()"""
        return MockResponse.get(url=url)

    # noinspection PyUnusedLocal
    @staticmethod
    def post(url: str, **kwargs) -> Response:
        """mocked Session.post()"""
        return MockResponse().post(url=url, **kwargs)

    # noinspection PyUnusedLocal
    @staticmethod
    def put(url: str, **kwargs) -> Response:
        """mocked Session.put()"""
        return MockResponse().put(url=url, **kwargs)


class MockResponse(Response):
    """mocked Response"""

    exist_objects = [
        "api/v2/cmdb/firewall/policy/1",
        "api/v2/cmdb/firewall/policy/3",
        "api/v2/cmdb/system.snmp/community/1",
        "api/v2/cmdb/system.snmp/community/3",
        f"api/v2/cmdb/antivirus/profile/{NAME1}",
        f"api/v2/cmdb/application/list/{NAME1}",
        f"api/v2/cmdb/firewall.schedule/onetime/{NAME1}",
        f"api/v2/cmdb/firewall.schedule/onetime/{NAME1}",
        f"api/v2/cmdb/firewall.service/category/{NAME1}",
        f"api/v2/cmdb/firewall.service/custom/{NAME1}",
        f"api/v2/cmdb/firewall.service/group/{NAME1}",
        f"api/v2/cmdb/firewall/address/?filter=name%3D%3D{NAME1}",
        f"api/v2/cmdb/firewall/address/{NAME1}",
        f"api/v2/cmdb/firewall/addrgrp/{NAME1}",
        f"api/v2/cmdb/firewall/internet-service/{NAME1}",
        f"api/v2/cmdb/firewall/ippool/{NAME1}",
        f"api/v2/cmdb/firewall/policy/{NAME1}",
        f"api/v2/cmdb/firewall/vip/{NAME1}",
        f"api/v2/cmdb/system.snmp/community/{NAME1}",
        f"api/v2/cmdb/system/interface/{NAME1}",
        f"api/v2/cmdb/system/zone/{NAME1}",
    ]

    def __init__(self, url=""):
        super().__init__()
        self.url = url
        self.reason = "unittest"
        self.status_code = 500

    @classmethod
    def get(cls, url: str) -> MockResponse:
        """session.get(), return data, status_code=200 if object is configured in the Fortigate"""
        resp = cls(url=url)
        url_ = cls._url(url=url)
        if url_ in resp.exist_objects:
            resp.status_code = 200
            resp._content = CONTENT_OBJECT
            if url_ == f"api/v2/cmdb/system/interface/{NAME1}":
                resp._content = CONTENT_INTERFACE
            if url_ == f"api/v2/cmdb/system/zone/{NAME1}":
                resp._content = CONTENT_ZONE
        elif url_ == f"api/v2/cmdb/firewall/address/{SLASH_}":
            resp.status_code = 200
            resp._content = CONTENT_SLASH
        elif url_ == f"api/v2/cmdb/firewall/policy/?filter=name%3D%3D{NAME1}":
            resp.status_code = 200
            resp._content = CONTENT_POLICY1
        elif url_ == f"api/v2/cmdb/firewall/policy/?filter=name%3D%3D{NAME3}":
            resp.status_code = 200
            resp._content = CONTENT_POLICY3
        elif url_ == f"api/v2/cmdb/system.snmp/community/?filter=name%3D%3D{NAME1}":
            resp.status_code = 200
            resp._content = CONTENT_SNMP1
        elif url_ == f"api/v2/cmdb/system.snmp/community/?filter=name%3D%3D{NAME3}":
            resp.status_code = 200
            resp._content = CONTENT_SNMP3
        elif url_ in ObjectBase._known_urls:
            resp.status_code = 200
            resp._content = CONTENT_OBJECT
            if url_ == "api/v2/cmdb/system/interface/":
                resp._content = CONTENT_INTERFACE
        return resp

    # noinspection PyProtectedMember
    @classmethod
    def post(cls, url: str, **kwargs) -> MockResponse:
        """session.post() (create), return status_code==200 (created successfully) only for
        supported objects with names: NAME1, NAME3"""
        resp = cls(url=url)
        if data_s := kwargs.get("data"):
            data_d = json.loads(data_s)
            if data_d.get("name") in [NAME1, NAME3]:
                url_ = cls._url(url=url)
                if url_ in ObjectBase._known_urls:
                    resp.status_code = 200
        return resp

    @classmethod
    def delete(cls, url: str) -> MockResponse:
        """session.delete(), object is configured in firewall, status_code==200"""
        resp = cls(url=url)
        url_ = cls._url(url=url)
        if url_ in resp.exist_objects:
            resp.status_code = 200
        return resp

    @classmethod
    def put(cls, url: str, **kwargs) -> MockResponse:
        """session.put() (update), object is configured in firewall, status_code==200"""
        resp = cls(url=url)
        url_ = cls._url(url=url)
        if (data_s := kwargs.get("data")) and data_s != "{}":
            data_d = json.loads(data_s)
            if data_d.get("name") == NAME1:
                if url_ in resp.exist_objects:
                    resp.status_code = 200
        elif url_ == "api/v2/cmdb/firewall/policy/1?action=move&before=2":
            resp.status_code = 200
        return resp

    @staticmethod
    def _url(url: str) -> str:
        """remove https://{hostname}/ from REST API URL"""
        return "api/v2/cmdb/" + url.split("/api/v2/cmdb/")[1]
