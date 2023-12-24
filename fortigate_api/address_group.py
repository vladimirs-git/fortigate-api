"""Address Group Object."""

from fortigate_api.base import Base


class AddressGroup(Base):
    """Address Group Object.

    - Web UI: https://hostname/api/v2/cmdb/firewall/addrgrp/
    - API: https://hostname/ng/firewall/address
    """

    def __init__(self, rest):
        """Address Group Object.

        ::
            :param rest: Fortigate REST API connector
            :type rest: Fortigate
        """
        super().__init__(rest=rest, url_obj="api/v2/cmdb/firewall/addrgrp/")
