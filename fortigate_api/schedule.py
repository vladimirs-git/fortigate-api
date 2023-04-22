"""Schedule Object."""

from fortigate_api.base import Base


class Schedule(Base):
    """Schedule Object."""

    def __init__(self, fgt):
        """Schedule Object.

        ::
            :param fgt: Fortigate connector
            :type fgt: Fortigate
        """
        super().__init__(fgt=fgt, url_obj="api/v2/cmdb/firewall.schedule/onetime/")
