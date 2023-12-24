"""Internet Service Object."""

from fortigate_api.base import Base


class InternetService(Base):
    """Internet Service Object.

    - Web UI: https://hostname/ng/firewall/internet_service
    - API: https://hostname/api/v2/cmdb/firewall/internet-service
    - Data: :ref:`InternetService.yml`
    """

    def __init__(self, rest):
        """Init Internet Service Object.

        :param rest: :ref:`Fortigate` REST API connector.
        :type rest: Fortigate
        """
        super().__init__(rest=rest, url_obj="api/v2/cmdb/firewall/internet-service/")
