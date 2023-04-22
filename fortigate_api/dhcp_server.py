"""DHCP Server Object."""

from requests import Response

from fortigate_api.base import Base
from fortigate_api.types_ import DAny, StrInt


class DhcpServer(Base):
    """DHCP Server Object."""

    def __init__(self, fgt):
        """DHCP Server Object.

        ::
            :param fgt: Fortigate connector
            :type fgt: Fortigate
        """
        super().__init__(fgt=fgt, url_obj="api/v2/cmdb/system.dhcp/server/", uid_key="id")

    def create(self, data: DAny) -> Response:
        """Create dhcp-server-object in the Fortigate.

        Note, in Fortigate is possible to create multiple DHCP servers with the same settings,
        you need control duplicates
        ::
            :param data: Data of the fortigate-object
            :type data: dict

            :return: Session response
                *<Response [200]>* Object successfully created or already exists
            :rtype: Response
        """
        return self.fgt.post(url=self.url_, data=data)

    def update(self, data: DAny, uid: StrInt = "") -> Response:
        """Update dhcp-server-object, where `uid` is data["id"].

        ::
            :param data: Data of the dhcp-server-object
            :type data: dict

            :param uid: ID of the dhcp-server-object,
                taken from the `uid` parameter or from data["id"]
            :type uid: str or int

            :return: Session response
                *<Response [200]>* Object successfully updated
                *<Response [404]>* Object has not been updated
            :rtype: Response
        """
        if not uid:
            uid = data.get("id") or ""
            if not uid:
                raise ValueError(f"absent {uid=} and data[\"id\"]")
        return self._update(uid=uid, data=data)
