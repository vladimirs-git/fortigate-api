"""Service Category Object."""

from fortigate_api.base import Base


class ServiceCategory(Base):
    """Service Category Object."""

    def __init__(self, fgt):
        """Service Category Object.

        ::
            :param fgt: Fortigate connector
            :type fgt: Fortigate
        """
        super().__init__(fgt=fgt, url_obj="api/v2/cmdb/firewall.service/category/")
