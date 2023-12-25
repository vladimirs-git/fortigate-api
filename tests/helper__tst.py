"""Helper for unittests."""
from __future__ import annotations

import json
import re
import unittest
from unittest.mock import patch

from requests import Response
from requests.cookies import RequestsCookieJar

from fortigate_api.fortigate import Fortigate

NAME3 = "NAME3"  # used for post <Response 200>
NAME1, NAME2, NAME4, SLASH, SLASH_ = "NAME1", "NAME2", "NAME4", "A/B", "A%2FB"
ADDR1, ADDR2, ADDR3, ADDR4, ADDR5 = "ADDR1", "ADDR2", "ADDR3", "ADDR4", "ADDR5"
ADDGR1 = "ADDGR1"
POL1, POL3 = "POL1", "POL3"
EQ = "%3D%3D"
GET = {"http_method": "GET", "revision": "1"}
D_ADDR1 = {"name": ADDR1, "type": "ipmask", "subnet": "1.1.1.0 255.255.255.252"}
D_ADDR2 = {"name": ADDR2, "type": "ipmask", "subnet": "2.2.2.0 255.255.255.252"}
D_ADDR3 = {"name": ADDR3, "type": "ipmask", "subnet": "3.3.3.0 255.255.255.252"}
D_ADDR4 = {"name": ADDR4, "type": "ipmask", "subnet": "4.4.4.0 255.255.255.252"}
D_ADDR5 = {"name": ADDR5, "type": "ipmask", "subnet": "5.5.5.0 255.255.255.252"}
D_ADDGR1 = {"name": ADDGR1, "type": "default", "member": [{"name": ADDR5}]}
D_INTF1 = {"name": NAME1, "vdom": "root"}
D_INTF3 = {"name": NAME3, "vdom": "vdom3"}
D_NAME1 = {"name": NAME1}
D_POL1 = {
    "name": POL1,
    "policyid": "1",
    "srcaddr": [{"name": ADDR1}],
    "dstaddr": [{"name": ADDR2}],
}
D_POL3 = {
    "name": POL3,
    "policyid": "3",
    "srcaddr": [{"name": ADDR3}],
    "dstaddr": [{"name": ADDGR1}],
}
D_SLASH = {"name": SLASH}
D_SNMP1 = {"name": NAME1, "id": "1"}
D_SNMP3 = {"name": NAME3, "id": "3"}
D_ZONE = {"name": NAME1, "interface": [{"interface-name": NAME1}]}


class MockFortigate(unittest.TestCase):  # TODO delete
    """Mock Fortigate."""

    def setUp(self):
        """Set Up."""
        patch.object(Fortigate, "login", return_value=MockSession()).start()
        patch.object(Fortigate, "_get_session", return_value=MockSession()).start()
        self.rest = Fortigate(host="domain.com", username="", password="")


class MockSession:  # TODO delete
    """Mock Session."""

    def __init__(self):
        """Mock Session."""
        self._headers = {}

    @property
    def headers(self):
        """Mock headers."""
        return self._headers

    @headers.setter
    def headers(self, data):
        self._headers = data

    @property
    def cookies(self):
        """Mock cookies."""
        cookie = RequestsCookieJar()
        cookie.name = "ccsrftoken"
        cookie.value = ".secret."
        return [cookie]

    # noinspection PyUnusedLocal
    @staticmethod
    def delete(url: str, **kwargs) -> Response:
        """Mock Session delete."""
        _ = kwargs  # noqa
        return MockResponse.delete(url=url)

    # noinspection PyUnusedLocal
    @staticmethod
    def get(url: str, **kwargs) -> Response:
        """Mock Session get."""
        _ = kwargs  # noqa
        return MockResponse.get(url=url)

    # noinspection PyUnusedLocal
    @staticmethod
    def post(url: str, **kwargs) -> Response:
        """Mock Session post."""
        return MockResponse().post(url=url, **kwargs)

    # noinspection PyUnusedLocal
    @staticmethod
    def put(url: str, **kwargs) -> Response:
        """Mock Session put."""
        return MockResponse().put(url=url, **kwargs)


class MockResponse(Response):  # TODO delete
    """Mock Response."""

    exist_objects = {
        f"api/v2/cmdb/antivirus/profile/{NAME1}": [D_NAME1],
        f"api/v2/cmdb/application/list/{NAME1}": [D_NAME1],

        "api/v2/cmdb/firewall/address": [D_ADDR1, D_ADDR2, D_ADDR3, D_ADDR4, D_ADDR5],
        f"api/v2/cmdb/firewall/address/?filter=name{EQ}{ADDR1}": [D_ADDR1],
        f"api/v2/cmdb/firewall/address/{ADDR1}": [D_ADDR1],
        f"api/v2/cmdb/firewall/address/{ADDR1}?filter=name{EQ}{ADDR1}": [D_ADDR1],
        f"api/v2/cmdb/firewall/address/{SLASH_}": [D_SLASH],

        "api/v2/cmdb/firewall/addrgrp": [D_ADDGR1],
        f"api/v2/cmdb/firewall/addrgrp/?filter=name{EQ}{ADDGR1}": [D_ADDGR1],
        f"api/v2/cmdb/firewall/addrgrp/{ADDGR1}": [D_ADDGR1],
        f"api/v2/cmdb/firewall/addrgrp/{ADDGR1}?filter=name{EQ}{ADDGR1}": [D_ADDGR1],

        f"api/v2/cmdb/firewall/internet-service/{NAME1}": [D_NAME1],
        f"api/v2/cmdb/firewall/ippool/{NAME1}": [D_NAME1],
        f"api/v2/cmdb/firewall/vip/{NAME1}": [D_NAME1],

        "api/v2/cmdb/firewall/policy": [D_POL1, D_POL3],
        "api/v2/cmdb/firewall/policy/1": [D_POL1],
        "api/v2/cmdb/firewall/policy/3": [D_POL3],
        f"api/v2/cmdb/firewall/policy/1?filter=name{EQ}{POL1}": [D_POL1],
        f"api/v2/cmdb/firewall/policy/?filter=name{EQ}{POL1}": [D_POL1],
        f"api/v2/cmdb/firewall/policy/?filter=name{EQ}{POL3}": [D_POL3],
        f"api/v2/cmdb/firewall/policy/?filter=policyid{EQ}1": [D_POL1],
        f"api/v2/cmdb/firewall/policy/?filter=policyid{EQ}3": [D_POL3],
        f"api/v2/cmdb/firewall/policy/{POL1}": [D_POL1],  # dummy for unittest

        f"api/v2/cmdb/firewall.schedule/onetime/{NAME1}": [D_NAME1],
        f"api/v2/cmdb/firewall.service/category/{NAME1}": [D_NAME1],
        f"api/v2/cmdb/firewall.service/custom/{NAME1}": [D_NAME1],
        f"api/v2/cmdb/firewall.service/group/{NAME1}": [D_NAME1],

        "api/v2/cmdb/system.snmp/community": [D_SNMP1, D_SNMP3],
        "api/v2/cmdb/system.snmp/community/1": [D_SNMP1],
        "api/v2/cmdb/system.snmp/community/3": [D_SNMP3],
        f"api/v2/cmdb/system.snmp/community/1?filter=name{EQ}{NAME1}": [D_SNMP1],
        f"api/v2/cmdb/system.snmp/community/?filter=id{EQ}1": [D_SNMP1],
        f"api/v2/cmdb/system.snmp/community/?filter=id{EQ}3": [D_SNMP3],
        f"api/v2/cmdb/system.snmp/community/?filter=name{EQ}{NAME1}": [D_SNMP1],
        f"api/v2/cmdb/system.snmp/community/{NAME1}": [D_SNMP1],  # dummy for unittest
        # f"api/v2/cmdb/system.snmp/community/?filter=name{EQ}{NAME3}": [D_SNMP3],

        f"api/v2/cmdb/system/external-resource/{NAME1}": [D_NAME1],
        f"api/v2/cmdb/system/external-resource/?filter=name{EQ}{NAME1}": [D_NAME1],

        "api/v2/cmdb/system/interface": [D_INTF1, D_INTF3],
        f"api/v2/cmdb/system/interface/?filter=name{EQ}{NAME1}": [D_INTF1],
        f"api/v2/cmdb/system/interface/?filter=name{EQ}{NAME3}": [D_INTF3],
        f"api/v2/cmdb/system/interface/{NAME1}": [D_INTF1],
        f"api/v2/cmdb/system/interface/{NAME3}": [D_INTF3],

        f"api/v2/cmdb/system/zone/{NAME1}": [D_ZONE],
    }

    def __init__(self, url=""):
        """Mock Response."""
        super().__init__()
        self.url = url
        self.reason = "unittest"
        self.status_code = 500

    @classmethod
    def get(cls, url: str) -> MockResponse:
        """Mock Session get.

        ::
            :return: status_code=200 if object is configured in the Fortigate
        """
        resp = cls(url=url)
        url_ = cls._url(url=url)

        # login
        if url_ == "api/v2/cmdb/system/vdom":
            resp.status_code = 200
            return resp
        # logout
        if url_ == "logout":
            resp.status_code = 200
            return resp

        # data
        if url_ in cls.exist_objects:
            data = cls.exist_objects[url_]
            text = json.dumps({**GET, **{"results": data}})
            resp._content = text.encode("utf-8")
            resp.status_code = 200
        return resp

    # noinspection PyProtectedMember
    @classmethod
    def post(cls, url: str, **kwargs) -> MockResponse:
        """Mock Session post.

        ::
            :return: status_code==200 (created successfully) only for supported objects
                with names: NAME1, NAME3
        """
        resp = cls(url=url)
        data_s = kwargs.get("data")
        if not data_s:
            return resp

        # login
        if data_s == "username=username&secretkey=":
            resp.status_code = 200
            return resp

        # new data
        data_d = json.loads(data_s)
        name = data_d.get("name") or ""
        if name == NAME3:
            resp.status_code = 200
        return resp

    @classmethod
    def delete(cls, url: str) -> MockResponse:
        """Mock Session delete.

        ::
            :return: Object is configured in firewall, status_code==200
        """
        resp = cls(url=url)
        url_ = cls._url(url=url)
        if url_ in resp.exist_objects:
            resp.status_code = 200
        return resp

    @classmethod
    def put(cls, url: str, **kwargs) -> MockResponse:
        """Mock Session put.

        ::
            :return: Object is configured in firewall, status_code==200
        """
        resp = cls(url=url)
        url_ = cls._url(url=url)
        if (data_s := kwargs.get("data")) and data_s != "{}":
            data_d = json.loads(data_s)
            if data_d.get("name") in [NAME1, ADDR1, ADDGR1, POL1]:
                if url_ in resp.exist_objects:
                    resp.status_code = 200
        # move
        elif url_ == "api/v2/cmdb/firewall/policy/1?action=move&username=&secretkey=&before=2":
            resp.status_code = 200
        return resp

    @staticmethod
    def _url(url: str) -> str:
        """Remove https://{hostname}/ from REST API URL."""
        pattern = "/api/v2/cmdb/"
        if re.search(pattern, url):
            url_ = "api/v2/cmdb/" + url.split(pattern)[1]
        else:
            url_ = url.split("/host/")[1]
        return url_
