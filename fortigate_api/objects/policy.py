"""Policy Object"""

from typing import List
from urllib.parse import urlencode, parse_qsl

from requests import Response

from fortigate_api import helper as h
from fortigate_api.base.object_id import ObjectID
from fortigate_api.types_ import LDAny, StrInt, DAny


class Policy(ObjectID):
    """Policy Object"""

    def __init__(self, fgt):
        super().__init__(url_obj="api/v2/cmdb/firewall/policy/", fgt=fgt)

    def delete_name(self, name: str) -> List[Response]:
        """Deletes fortigate-objects with the same name from Fortigate
        :param name: name of the fortigate-objects
        :return: Session response. *<Response [200]>* Object successfully deleted,
            *<Response [404]>* Object absent in the Fortigate
        """
        results: LDAny = self.get(name=name)
        ids = [str(d["policyid"]) for d in results]
        return self._delete_by_ids(ids)

    # noinspection PyShadowingBuiltins
    def move(self, id: StrInt, position: str, neighbor: StrInt) -> Response:
        """Move policy to before/after other neighbor-policy
        :param id: Identifier of policy being moved
        :param position: "before" or "after" neighbor
        :param neighbor: Policy will be moved near to this neighbor-policy
        :return: Session response. *<Response [200]>* Policy successfully moved,
            *<Response [500]>* Policy has not been moved
        """
        id_ = h.int_(key="id", **{"id": id})
        params = {"action": "move",
                  position: h.int_(key="neighbor", **{"neighbor": neighbor}),
                  "username": self.fgt.username,
                  "secretkey": self.fgt.password}
        query = urlencode(dict(parse_qsl(urlencode(params))))
        url = f"{self.url}/{self.url_obj}{id_}?{query}"
        return self.fgt.put(url=url, data={})

    def update(self, data: DAny) -> Response:
        """Updates fortigate-object in the Fortigate
        :param data: Data of the fortigate-object
        :return: Session response. *<Response [200]>* Object successfully updated,
            *<Response [404]>* Object has not been updated
        """
        id_ = str(data["policyid"])
        return self._update(id=id_, data=data)
