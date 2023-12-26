"""Schedule Object."""

from fortigate_api.base import Base


class Schedule(Base):
    """Schedule Object.

    - Web UI: https://hostname/ng/firewall/schedule
    - API: https://hostname/api/v2/cmdb/firewall.schedule/onetime
    - Data: :ref:`Schedule.yml`
    """

    def __init__(self, rest):
        """Init Schedule Object.

        :param rest: :ref:`Fortigate` REST API connector.
        :type rest: Fortigate
        """
        super().__init__(rest=rest, url_obj="api/v2/cmdb/firewall.schedule/onetime/")
