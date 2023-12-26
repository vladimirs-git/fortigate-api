"""Virtual IP Object."""

from fortigate_api.base import Base


class VirtualIp(Base):
    """Virtual IP Object.

    - Web UI: https://hostname/ng/firewall/virtual-ip
    - API: https://hostname/api/v2/cmdb/firewall/vip
    - Data: :ref:`VirtualIp.yml`
    """

    def __init__(self, rest):
        """Init Virtual IP Object.

        :param rest: :ref:`Fortigate` REST API connector.
        :type rest: Fortigate
        """
        super().__init__(rest=rest, url_obj="api/v2/cmdb/firewall/vip/")
