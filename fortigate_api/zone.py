"""Zone Object."""

from fortigate_api.base import Base


class Zone(Base):
    """Zone Object."""

    def __init__(self, fgt):
        """Zone Object.

        ::
            :param fgt: Fortigate connector
            :type fgt: Fortigate
        """
        super().__init__(fgt=fgt, url_obj="api/v2/cmdb/system/zone/")
