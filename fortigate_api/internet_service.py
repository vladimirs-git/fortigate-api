"""Internet Service Object."""

from fortigate_api.base import Base


class InternetService(Base):
    """Internet Service Object."""

    def __init__(self, rest):
        """Internet Service Object.

        ::
            :param rest: Fortigate REST API connector
            :type rest: Fortigate
        """
        super().__init__(rest=rest, url_obj="api/v2/cmdb/firewall/internet-service/")
