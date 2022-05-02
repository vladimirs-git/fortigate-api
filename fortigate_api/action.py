"""Actions with Objects"""

from __future__ import annotations

from abc import abstractmethod
from urllib.parse import urlencode

from requests import Response  # type: ignore

from fortigate_api import helper
from fortigate_api.types_ import DAny, LDAny


class Action:
    """Actions with Objects"""

    _known_urls = (
        "api/v2/cmdb/antivirus/profile/",
        "api/v2/cmdb/application/list/",
        "api/v2/cmdb/firewall.schedule/onetime/",
        "api/v2/cmdb/firewall.service/category/",
        "api/v2/cmdb/firewall.service/custom/",
        "api/v2/cmdb/firewall.service/group/",
        "api/v2/cmdb/firewall/address/",
        "api/v2/cmdb/firewall/addrgrp/",
        "api/v2/cmdb/firewall/internet-service/",
        "api/v2/cmdb/firewall/ippool/",
        "api/v2/cmdb/firewall/policy/",
        "api/v2/cmdb/firewall/vip/",
        "api/v2/cmdb/system.snmp/community/",
        "api/v2/cmdb/system/interface/",
        "api/v2/cmdb/system/zone/",
    )

    def __init__(self, fgt):
        self.fgt = fgt  # firewall connector
        self.url = fgt.url

    @abstractmethod
    def create(self, data: DAny) -> Response:
        """Create new object on Fortigate"""

    @abstractmethod
    def delete(self, name: str) -> Response:
        """Delete object with name from Fortigate"""

    @abstractmethod
    def get(self, **kwargs) -> LDAny:
        """Get objects, all or filtered by params"""

    @abstractmethod
    def update(self, data: DAny) -> Response:
        """Update object on Fortigate"""

    def _create(self, url: str, data: DAny) -> Response:
        """Create new object on Fortigate
        :param url: REST API URL to object
        :param data: data of object
        :return: session response"""
        url = f"{self.url}/{url}"
        name = helper.quote_(data["name"])
        exist = self.fgt.exist(url=f"{url}{name}")
        if exist.ok:
            return exist
        return self.fgt.post(url=url, data=data)

    def _delete(self, url: str) -> Response:
        """Delete object from Fortigate
        :param url: REST API URL to object
        :return: session response"""
        url = f"{self.url}/{url}"
        return self.fgt.delete(url=url)

    def _get(self, url: str, **kwargs) -> LDAny:
        """Get objects data from Fortigate
        :param url: REST API URL to object
        :param kwargs: url params: name, id, filter, filters
        :return: data of objects"""
        url = self._quote_url(url)
        url = f"{self.url}/{url}"
        url = self._url_params(url=url, **kwargs)
        return self.fgt.get(url)

    def _update(self, url: str, data: DAny) -> Response:
        """Update existing object on Fortigate
        :param url: REST API URL to object
        :param data: data of object
        :return: session response"""
        name = helper.quote_(data["name"])
        url = f"{self.url}/{url}{name}"
        exist = self.fgt.exist(url=url)
        if not exist.ok:
            return exist
        return self.fgt.put(url=url, data=data)

    # =========================== helpers ============================

    def _quote_url(self, url: str) -> str:
        """quote end of url"""
        for known in self._known_urls:
            if url.startswith(known):
                end = url.replace(known, "", 1)
                return known + helper.quote_(end)
        return url

    @staticmethod
    def _url_params(url: str, **kwargs) -> str:
        """Add name, id, filter params to url
        :param url: REST API URL to object
        :param kwargs: params: id, name, filter, filters
        :return: url with params
        """
        params = kwargs
        if not params:
            return url
        if len(params) != 1:
            raise ValueError(f"expected only one of {params=}")
        expected = ["id", "name", "filter", "filters"]
        if invalid_params := set(params).difference(set(expected)):
            raise ValueError(f"{invalid_params=}, {expected=}")
        if params.get("id") or 0:
            id_ = helper.int_(key="id", **params)
            return f"{url}{id_}"
        if name := params.get("name", ""):
            return f"{url}{helper.quote_(name)}"
        if filter_ := params.get("filter", ""):
            param = urlencode([("filter", filter_)])
            return f"{url}?{param}"
        if filters := params.get("filters", list()):
            param = urlencode([("filter", s) for s in filters])
            return f"{url}?{param}"
        raise ValueError(f"absent value in params={list(params)}")
