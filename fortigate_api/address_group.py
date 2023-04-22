"""Address Group Object."""

from fortigate_api.base import Base


class AddressGroup(Base):
    """Address Group Object."""

    def __init__(self, fgt):
        """Address Group Object.

        ::
            :param fgt: Fortigate connector
            :type fgt: Fortigate
        """
        super().__init__(fgt=fgt, url_obj="api/v2/cmdb/firewall/addrgrp/")
