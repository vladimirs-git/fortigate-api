"""Object Base"""

from abc import abstractmethod

from requests import Response  # type: ignore

from fortigate_api import helper as h
from fortigate_api.types_ import DAny, LDAny, IStrs


class ObjectBase:
    """Object Base"""

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
        """Object Base
        :param fgt: Fortigate connector
        """
        self.fgt = fgt
        self.url = fgt.url

    @abstractmethod
    def create(self, data: DAny) -> Response:
        """Creates new object in the Fortigate"""

    @abstractmethod
    def delete(self, name: str) -> Response:
        """Deletes object with name from Fortigate"""

    @abstractmethod
    def get(self, **kwargs) -> LDAny:
        """Gets objects, all or filtered by params"""

    @abstractmethod
    def update(self, data: DAny) -> Response:
        """Updates object in the Fortigate"""

    def _create(self, url: str, data: DAny) -> Response:
        """Creates new object in the Fortigate
        :param url: REST API URL to the object
        :param data: Data of the object
        :return: Session response
        """
        url = f"{self.url}/{url}"
        name = h.quote_(data["name"])
        exist = self.fgt.exist(url=f"{url}{name}")
        if exist.ok:
            return exist
        return self.fgt.post(url=url, data=data)

    def _delete(self, url: str) -> Response:
        """Deletes object from Fortigate
        :param url: REST API URL to the object
        :return: Session response
        """
        url = f"{self.url}/{url}"
        return self.fgt.delete(url=url)

    def _get(self, url: str, **kwargs) -> LDAny:
        """Gets objects data from Fortigate
        :param url: REST API URL to the object
        :param kwargs: url params: name, id, filter
        :return: data of the objects"""
        url = self._quote_url(url)
        url = f"{self.url}/{url}"
        url = self._url_params(url=url, **kwargs)
        return self.fgt.get(url)

    def _update(self, url: str, data: DAny) -> Response:
        """Updates existing object in the Fortigate
        :param url: REST API URL to the object
        :param data: Data of the object
        :return: Session response
        """
        name = h.quote_(data["name"])
        url = f"{self.url}/{url}{name}"
        exist = self.fgt.exist(url=url)
        if not exist.ok:
            return exist
        return self.fgt.put(url=url, data=data)

    def _is_exist(self, url: str, **kwargs) -> bool:
        """Checks does an object exists in the Fortigate
        :param url: REST API URL to the object
        :param name: Name of the object
        :param id: The ID of the object
        :return: True - object exist, False - object does not exist
        """
        url = f"{self.url}/{url}"
        url = self._url_params(url=url, **kwargs)
        response = self.fgt.exist(url=url)
        return response.ok

    # =========================== helpers ============================

    @staticmethod
    def _name_to_filter(kwargs: DAny) -> None:
        """replace "name" argument to "filter" """
        if name := kwargs.get("name") or "":
            del kwargs["name"]
            kwargs["filter"] = f"name=={name}"

    def _quote_url(self, url: str) -> str:
        """quote end of url"""
        for known in self._known_urls:
            if url.startswith(known):
                end = url.replace(known, "", 1)
                return known + h.quote_(end)
        return url

    @staticmethod
    def _url_params(url: str, **kwargs) -> str:
        """Add name, id, filter params to url
        :param url: REST API URL to the object
        :param kwargs: params: id, name, filter
        :return: url with params
        """
        params = kwargs
        if not params:
            return url
        if len(params) != 1:
            raise ValueError(f"expected only one of {params=}")
        expected = ["id", "name", "filter"]
        if invalid_params := set(params).difference(set(expected)):
            raise ValueError(f"{invalid_params=}, {expected=}")
        if params.get("id") or 0:
            id_ = h.int_(key="id", **params)
            return f"{url}{id_}"
        if name := params.get("name") or "":
            return f"{url}{h.quote_(name)}"
        filters: IStrs = params.get("filter") or []
        if not isinstance(filters, (str, list, set, tuple)):
            raise ValueError(f"{filters=} {str} expected")
        if isinstance(filters, str):
            filters = [filters]
        if invalid_filter := [s for s in filters if not isinstance(s, str)]:
            raise ValueError(f"{invalid_filter=} {str} expected")
        url_ = h.add_params_to_url(url=url, params=dict(filter=filters))
        return url_
