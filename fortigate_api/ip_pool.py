"""IP Pool Object."""

from fortigate_api.base import Base


class IpPool(Base):
    """IP Pool Object.

    - Web UI: https://hostname/ng/firewall/ip-pool
    - API: https://hostname/api/v2/cmdb/firewall/ippool
    - Data: :ref:`IpPool.yml`
    """

    def __init__(self, rest):
        """Init IP Pool Object.

        :param rest: :ref:`Fortigate` REST API connector.
        :type rest: Fortigate
        """
        super().__init__(rest=rest, url_obj="api/v2/cmdb/firewall/ippool/")
