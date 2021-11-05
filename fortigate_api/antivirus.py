"""Antivirus Object"""

from __future__ import annotations

from requests import Response

from fortigate_api import helper
from fortigate_api.action import Action
from fortigate_api.typing_ import DAny, LDAny


class Antivirus(Action):
    """Antivirus Object"""

    def create(self, data: DAny, **kwargs) -> Response:
        """Create antivirus-object on Fortigate
        :param data: data of object
        :return: session response"""
        return self._create(url="api/v2/cmdb/antivirus/profile/", data=data)

    def delete(self, name: str) -> Response:
        """Delete antivirus-object from Fortigate
        :param name: name of object
        :return: session response"""
        name = helper.quote_(name)
        url = f"api/v2/cmdb/antivirus/profile/{name}"
        return self._delete(url=url)

    def get(self, **kwargs) -> LDAny:
        """Get antivirus-objects, all or filtered by params: name, filter, filters"""
        return self._get(url="api/v2/cmdb/antivirus/profile/", **kwargs)

    def update(self, data: DAny) -> Response:
        """Update antivirus-object on Fortigate
        :param data: data of object
        :return: session response"""
        return self._update(url="api/v2/cmdb/antivirus/profile/", data=data)
