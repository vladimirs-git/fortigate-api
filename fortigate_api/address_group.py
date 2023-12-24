"""Address Group Object."""

from fortigate_api.base import Base


class AddressGroup(Base):
    """Address Group Object.

    - Web UI: https://hostname/ng/firewall/address
    - API: https://hostname/api/v2/cmdb/firewall/addrgrp
    - Data: :ref:`AddressGroup.yml`
    """

    def __init__(self, rest):
        """Init Address Group Object.

        :param rest: :ref:`Fortigate` REST API connector.
        :type rest: Fortigate
        """
        super().__init__(rest=rest, url_obj="api/v2/cmdb/firewall/addrgrp/")
