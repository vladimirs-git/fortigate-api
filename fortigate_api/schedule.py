"""Schedule Object."""

from fortigate_api.base import Base


class Schedule(Base):
    """Schedule Object."""

    def __init__(self, rest):
        """Schedule Object.

        ::
            :param rest: Fortigate REST API connector
            :type rest: Fortigate
        """
        super().__init__(rest=rest, url_obj="api/v2/cmdb/firewall.schedule/onetime/")
