"""Address Object"""

from __future__ import annotations

from requests import Response

from fortigate_api import helper
from fortigate_api.action import Action
from fortigate_api.typing_ import DAny, LDAny


class Address(Action):
    """Address Object"""

    def create(self, data: DAny, **kwargs) -> Response:
        """Create address-object on Fortigate
        :param data: data of object
        :return: session response"""
        return self._create(url="api/v2/cmdb/firewall/address/", data=data)

    def delete(self, name: str) -> Response:
        """Delete address-object from Fortigate
        :param name: name of object
        :return: session response"""
        url = f"api/v2/cmdb/firewall/address/{helper.quote_(name)}"
        return self._delete(url=url)

    def get(self, **kwargs) -> LDAny:
        """Get address-objects, all or filtered by params: name, filter, filters"""
        return self._get(url="api/v2/cmdb/firewall/address/", **kwargs)

    def update(self, data: DAny) -> Response:
        """Update address-object on Fortigate
        :param data: data of object
        :return: session response"""
        return self._update(url="api/v2/cmdb/firewall/address/", data=data)
