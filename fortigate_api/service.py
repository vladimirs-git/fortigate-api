"""Service Object"""

from __future__ import annotations

from requests import Response

from fortigate_api import helper
from fortigate_api.action import Action
from fortigate_api.typing_ import DAny, LDAny


class Service(Action):
    """Service Object"""

    def create(self, data: DAny, **kwargs) -> Response:
        """Create service-object on Fortigate
        :param data: data of object
        :return: session response"""
        return self._create(url="api/v2/cmdb/firewall.service/custom/", data=data)

    def delete(self, name: str) -> Response:
        """Delete service-object from Fortigate
        :param name: name of object
        :return: session response"""
        name = helper.quote_(name)
        url = f"api/v2/cmdb/firewall.service/custom/{name}"
        return self._delete(url=url)

    def get(self, **kwargs) -> LDAny:
        """Get service-objects, all or filtered by params: name, filter, filters"""
        return self._get(url="api/v2/cmdb/firewall.service/custom/", **kwargs)

    def update(self, data: DAny) -> Response:
        """Update service-object on Fortigate
        :param data: data of object
        :return: session response"""
        return self._update(url="api/v2/cmdb/firewall.service/custom/", data=data)
