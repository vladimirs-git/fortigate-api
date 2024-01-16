"""Cmdb/firewall/addrgrp6 connector."""

from fortigate_api.connector import Connector


class Addrgrp6FC(Connector):
    """Cmdb/firewall/addrgrp6 connector."""

    uid = "name"
    _path = "api/v2/cmdb/firewall/addrgrp6"
