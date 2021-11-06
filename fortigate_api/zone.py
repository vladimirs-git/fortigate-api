"""Zone Object"""

from __future__ import annotations

from requests import Response  # type: ignore

from fortigate_api import helper
from fortigate_api.action import Action
from fortigate_api.interface import Interface
from fortigate_api.typing_ import DAny, LDAny, LStr


class Zone(Action):
    """Zone Object"""

    def create(self, data: DAny, **kwargs) -> Response:
        """Create zone-object on Fortigate
        :param data: data of object
        :return: session response"""
        return self._create(url="api/v2/cmdb/system/zone/", data=data)

    def delete(self, name: str) -> Response:
        """Delete zone-object from Fortigate
        :param name: name of object
        :return: session response"""
        name = helper.quote_(name)
        url = f"api/v2/cmdb/system/zone/{name}"
        return self._delete(url=url)

    def get(self, **kwargs) -> LDAny:
        """Get zone-objects in vdom, all or filtered by params: name, filter, filters"""
        interface_o = Interface(fgt=self.fgt)
        interfaces: LStr = [d["name"] for d in interface_o.get()]
        zones_all: LDAny = self._get(url="api/v2/cmdb/system/zone/", **kwargs)
        zones: LDAny = list()
        for zone in zones_all:
            for intf_d in zone["interface"]:
                if intf_d["interface-name"] in interfaces:
                    zones.append(zone)
                    break
        return zones

    def get_all(self) -> LDAny:
        """Get zone-objects, all"""
        return self._get(url="api/v2/cmdb/system/zone/")

    def update(self, data: DAny) -> Response:
        """Update zone-object on Fortigate
        :param data: data of object
        :return: session response"""
        return self._update(url="api/v2/cmdb/system/zone/", data=data)
