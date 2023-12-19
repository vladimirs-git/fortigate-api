"""List Vdoms Object."""

from fortigate_api.base import Base


class Vdoms(Base):
    """Vdoms List Object."""

    def __init__(self, rest):
        """Vdoms List Object.

        ::
            :param rest: Fortigate REST API connector
            :type rest: Fortigate
        """
        super().__init__(rest=rest, url_obj="api/v2/cmdb/system/vdom")