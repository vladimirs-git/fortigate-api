"""Interface Object"""

from __future__ import annotations

from requests import Response  # type: ignore

from fortigate_api import helper
from fortigate_api.action import Action
from fortigate_api.types_ import DAny, LDAny


class Interface(Action):
    """Interface Object"""

    def create(self, data: DAny, **kwargs) -> Response:
        """Create interface-object on Fortigate
        :param data: data of object
        :return: session response"""
        return self._create(url="api/v2/cmdb/system/interface/", data=data)

    def delete(self, name: str) -> Response:
        """Delete interface-object from Fortigate
        :param name: name of object
        :return: session response"""
        name = helper.quote_(name)
        url = f"api/v2/cmdb/system/interface/{name}"
        return self._delete(url=url)

    def get(self, **kwargs) -> LDAny:
        """Get interface-objects in vdom, all or filtered by params: name, filter, filters"""
        interfaces: LDAny = self._get(url="api/v2/cmdb/system/interface/", **kwargs)
        interfaces = [d for d in interfaces if d["vdom"] == self.fgt.vdom]
        return interfaces

    def get_all(self) -> LDAny:
        """Get interface-objects, all"""
        return self._get(url="api/v2/cmdb/system/interface/")

    def update(self, data: DAny) -> Response:
        """Update interface-object on Fortigate
        :param data: data of object
        :return: session response"""
        return self._update(url="api/v2/cmdb/system/interface/", data=data)
