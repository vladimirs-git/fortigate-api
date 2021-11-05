"""SNMP Community Object"""

from __future__ import annotations

from typing import List

from requests import Response

from fortigate_api import helper
from fortigate_api.action import Action
from fortigate_api.typing_ import DAny, LDAny


class SnmpCommunity(Action):
    """SNMP Community Object"""

    def create(self, data: DAny, **kwargs) -> Response:
        """Create snmp-community-object on Fortigate
        :param data: data of object
        :return: session response"""
        return self._create(url="api/v2/cmdb/system.snmp/community/", data=data)

    # noinspection PyShadowingBuiltins
    def delete(self, id: int) -> Response:  # pylint: disable=redefined-builtin
        """Delete snmp-community-object from Fortigate
        :param id: id of snmp-community-object
        :return: session response"""
        id_ = helper.int_(key="id", **{"id": id})
        url = f"api/v2/cmdb/system.snmp/community/{id_}"
        return self._delete(url=url)

    def delete_name(self, name: str) -> List[Response]:
        """Delete snmp-community-objects from Fortigate, is possible multiple objects with same name
        :param name: name of snmp-community-objects
        :return: session responses"""
        communities = self.get(name=name)
        ids = [d["id"] for d in communities]
        responses: List[Response] = list()
        for id_ in ids:
            url = f"api/v2/cmdb/system.snmp/community/{id_}"
            responses.append(self._delete(url=url))
        return responses

    def get(self, **kwargs) -> LDAny:
        """Get snmp-community-objects, all or filtered by params: id, name, filter, filters"""
        helper.name_to_filter(kwargs=kwargs)
        return self._get(url="api/v2/cmdb/system.snmp/community/", **kwargs)

    def update(self, data: DAny) -> Response:
        """Update snmp-community-object on Fortigate
        :param data: data of object
        :return: session response"""
        id_ = str(data["id"])
        url = f"{self.url}/api/v2/cmdb/system.snmp/community/{id_}"
        exist = self.fgt.exist(url)
        if not exist.ok:
            return exist
        return self.fgt.put(url=url, data=data)
