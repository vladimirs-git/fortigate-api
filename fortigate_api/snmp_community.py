"""SNMP Community Object."""

from requests import Response

from fortigate_api.base import Base
from fortigate_api.types_ import DAny, StrInt


class SnmpCommunity(Base):
    """SNMP Community Object.

    - Web UI: https://hostname/ng/system/snmp
    - API: https://hostname/api/v2/cmdb/system.snmp/community
    - Data: :ref:`SnmpCommunity.yml`
    """

    def __init__(self, rest):
        """Init SNMP Community Object.

        :param rest: :ref:`Fortigate` REST API connector.
        :type rest: Fortigate
        """
        super().__init__(rest=rest, url_obj="api/v2/cmdb/system.snmp/community/", uid_key="id")

    def update(self, data: DAny, uid: StrInt = "") -> Response:
        """Update snmp-community-object, where `uid` is `data["id"]`.

        :param data: Data of the snmp-community-object.
        :type data: dict

        :param uid: ID of the snmp-community-object,
            taken from the `uid` parameter or from `data["id"]`.
        :type uid: str or int

        :return: Session response.

            - <Response [200]> Object successfully updated,
            - <Response [404]> Object has not been updated.
        :rtype: requests.Response
        """
        if not uid:
            uid = data.get("id") or ""
            if not uid:
                raise ValueError(f"absent {uid=} and data[\"id\"]")
        return self._update(uid=uid, data=data)
