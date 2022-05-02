"""IpPool Object"""

from __future__ import annotations

from requests import Response  # type: ignore

from fortigate_api import helper
from fortigate_api.action import Action
from fortigate_api.types_ import DAny, LDAny


class IpPool(Action):
    """IpPool Object"""

    def create(self, data: DAny, **kwargs) -> Response:
        """Create ippool-object on Fortigate
        :param data: data of object
        :return: session response"""
        return self._create(url="api/v2/cmdb/firewall/ippool/", data=data)

    def delete(self, name: str) -> Response:
        """Delete ippool-object from Fortigate
        :param name: name of object
        :return: session response"""
        name = helper.quote_(name)
        url = f"api/v2/cmdb/firewall/ippool/{name}"
        return self._delete(url=url)

    def get(self, **kwargs) -> LDAny:
        """Get ippool-objects, all or filtered by params: name, filter, filters"""
        return self._get(url="api/v2/cmdb/firewall/ippool/", **kwargs)

    def update(self, data: DAny) -> Response:
        """Update ippool-object on Fortigate
        :param data: data of object
        :return: session response"""
        return self._update(url="api/v2/cmdb/firewall/ippool/", data=data)
