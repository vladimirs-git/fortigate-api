"""Cmdb/firewall/proxy-addrgrp connector."""

from fortigate_api.connector import Connector


class ProxyAddrgrpFC(Connector):
    """Cmdb/firewall/proxy-addrgrp connector."""

    uid = "name"
    _path = "api/v2/cmdb/firewall/proxy-addrgrp"
