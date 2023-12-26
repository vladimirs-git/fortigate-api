"""DHCP Server Object."""

from requests import Response

from fortigate_api.base import Base
from fortigate_api.types_ import DAny, StrInt


class DhcpServer(Base):
    """DHCP Server Object.

    - Web UI: https://hostname/ng/interface/edit/{name}
    - API: https://hostname/api/v2/cmdb/system.dhcp/server
    - Data: :ref:`DhcpServer.yml`
    """

    def __init__(self, rest):
        """Init DHCP Server Object.

        :param rest: :ref:`Fortigate` REST API connector.
        :type rest: Fortigate
        """
        super().__init__(rest=rest, url_obj="api/v2/cmdb/system.dhcp/server/", uid_key="id")

    def create(self, data: DAny) -> Response:
        """Create dhcp-server-object in the Fortigate.

        Note, in Fortigate is possible to create multiple DHCP servers with the same settings,
        you need control duplicates.

        :param dict data: Data of the fortigate-object

        :return: Session response.

            - `<Response [200]>` Object successfully created or already exists,
            - `<Response [400]>` Invalid URL,
            - `<Response [500]>` Object already exist.
        :rtype: requests.Response
        """
        return self.rest.post(url=self.url_, data=data)

    def update(self, data: DAny, uid: StrInt = "") -> Response:
        """Update dhcp-server-object, where `uid` is `data["id"]`.

        :param dict data: Data of the dhcp-server-object.

        :param uid: ID of the dhcp-server-object,
            taken from the `uid` parameter or from `data["id"]`
        :type uid: str or int

        :return: Session response.

            - `<Response [200]>` Object successfully updated,
            - `<Response [400]>` Invalid URL,
            - `<Response [404]>` Object has not been updated.
        :rtype: requests.Response
        """
        if not uid:
            uid = data.get("id") or ""
            if not uid:
                raise ValueError(f"Absent {uid=} and data[\"id\"].")
        return self._update(uid=uid, data=data)
