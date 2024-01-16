"""Cmdb/firewall/vipgrp64 connector."""

from fortigate_api.connector import Connector


class Vipgrp64FC(Connector):
    """Cmdb/firewall/vipgrp64 connector."""

    uid = "name"
    _path = "api/v2/cmdb/firewall/vipgrp64"
