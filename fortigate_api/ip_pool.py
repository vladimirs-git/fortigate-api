"""IP Pool Object."""

from fortigate_api.base import Base


class IpPool(Base):
    """IP Pool Object."""

    def __init__(self, rest):
        """IP Pool Object.

        ::
            :param rest: Fortigate REST API connector
            :type rest: Fortigate
        """
        super().__init__(rest=rest, url_obj="api/v2/cmdb/firewall/ippool/")
