"""Address Object."""

from fortigate_api.base import Base


class Address(Base):
    """Address Object."""

    def __init__(self, rest):
        """Init Address Object.

        :param rest: :ref:`Fortigate` REST API connector.
        :type rest: Fortigate
        """
        super().__init__(rest=rest, url_obj="api/v2/cmdb/firewall/address/")
