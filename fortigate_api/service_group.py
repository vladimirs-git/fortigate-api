"""Service Group Object."""

from fortigate_api.base import Base


class ServiceGroup(Base):
    """Service Group Object."""

    def __init__(self, fgt):
        """Service Group Object.

        ::
            :param fgt: Fortigate connector
            :type fgt: Fortigate
        """
        super().__init__(fgt=fgt, url_obj="api/v2/cmdb/firewall.service/group/")
