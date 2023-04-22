"""Virtual IP Object."""

from fortigate_api.base import Base


class VirtualIP(Base):
    """Virtual IP Object."""

    def __init__(self, fgt):
        """Virtual IP Object.

        ::
            :param fgt: Fortigate connector
            :type fgt: Fortigate
        """
        super().__init__(fgt=fgt, url_obj="api/v2/cmdb/firewall/vip/")
