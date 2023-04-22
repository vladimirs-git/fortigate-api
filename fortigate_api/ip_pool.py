"""IP Pool Object."""

from fortigate_api.base import Base


class IpPool(Base):
    """IP Pool Object."""

    def __init__(self, fgt):
        """IP Pool Object.

        ::
            :param fgt: Fortigate connector
            :type fgt: Fortigate
        """
        super().__init__(fgt=fgt, url_obj="api/v2/cmdb/firewall/ippool/")
