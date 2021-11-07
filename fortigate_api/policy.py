"""Policy Object"""

from __future__ import annotations

from typing import List
from urllib.parse import urlencode, parse_qsl

from requests import Response  # type: ignore

from fortigate_api import helper
from fortigate_api.action import Action
from fortigate_api.typing_ import DAny, LDAny, StrInt


class Policy(Action):
    """Policy Object"""

    def create(self, data: DAny, **kwargs) -> Response:
        """Create policy-object on Fortigate
        :param data: data of object
        :return: session response"""
        return self._create(url="api/v2/cmdb/firewall/policy/", data=data)

    def delete(self, policyid: StrInt) -> Response:
        """Delete policy-object from Fortigate
        :param policyid: unique identifier of policy-object
        :return: session response"""
        id_ = helper.int_(key="id", **{"id": policyid})
        url = f"api/v2/cmdb/firewall/policy/{id_}"
        return self._delete(url=url)

    def delete_name(self, name: str) -> List[Response]:
        """Delete policy-objects from Fortigate, is possible multiple objects with the same name
        :param name: name of policy-objects
        :return: session responses"""
        policies = self.get(name=name)
        ids = [d["policyid"] for d in policies]
        responses: List[Response] = list()
        for id_ in ids:
            url = f"api/v2/cmdb/firewall/policy/{id_}"
            responses.append(self._delete(url=url))
        return responses

    def get(self, **kwargs) -> LDAny:
        """Get policy-objects, all or filtered by params: policyid, name, filter, filters"""
        helper.name_to_filter(kwargs=kwargs)
        return self._get(url="api/v2/cmdb/firewall/policy/", **kwargs)

    def update(self, data: DAny) -> Response:
        """Update policy-object on Fortigate
        :param data: data of object
        :return: session response"""
        id_ = str(data["policyid"])
        url = f"{self.url}/api/v2/cmdb/firewall/policy/{id_}"
        exist = self.fgt.exist(url)
        if not exist.ok:
            return exist
        return self.fgt.put(url=url, data=data)

    def move(self, policyid: StrInt, position: str, neighbor: StrInt) -> Response:
        """Move policy to before/after other neighbor-policy
        :param policyid: unique identifier of policy being moved
        :param position: "before" or "after" neighbor
        :param neighbor: policy will be moved near to this neighbor-policy
        """
        id_ = helper.int_(key="id", **{"id": policyid})
        params = {"action": "move",
                  position: helper.int_(key="neighbor", **{"neighbor": neighbor}),
                  "username": self.fgt.username,
                  "secretkey": self.fgt.password}
        query = urlencode(dict(parse_qsl(urlencode(params))))
        url = f"{self.url}/api/v2/cmdb/firewall/policy/{id_}?{query}"
        return self.fgt.put(url=url, data={})
