"""Service Object."""

from fortigate_api.base import Base


class Service(Base):
    """Service Object."""

    def __init__(self, fgt):
        """Service Object.

        ::
            :param fgt: Fortigate connector
            :type fgt: Fortigate
        """
        super().__init__(fgt=fgt, url_obj="api/v2/cmdb/firewall.service/custom/")
