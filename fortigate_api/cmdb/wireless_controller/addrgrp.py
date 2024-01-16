"""Cmdb/wireless-controller/addrgrp connector."""

from fortigate_api.connector import Connector


class AddrgrpWcC(Connector):
    """Cmdb/wireless-controller/addrgrp connector."""

    uid = "id"
    _path = "api/v2/cmdb/wireless-controller/addrgrp"
