"""Cmdb/firewall/addrgrp connector."""

from fortigate_api.connector import Connector


class AddrgrpFC(Connector):
    """Cmdb/firewall/addrgrp connector."""

    uid = "name"
    _path = "api/v2/cmdb/firewall/addrgrp"
    _path_ui = "ng/firewall/address"
