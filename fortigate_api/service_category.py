"""Service Category Object."""

from fortigate_api.base import Base


class ServiceCategory(Base):
    """Service Category Object."""

    def __init__(self, rest):
        """Service Category Object.

        ::
            :param rest: Fortigate REST API connector
            :type rest: Fortigate
        """
        super().__init__(rest=rest, url_obj="api/v2/cmdb/firewall.service/category/")
