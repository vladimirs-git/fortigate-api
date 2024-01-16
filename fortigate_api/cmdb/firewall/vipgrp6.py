"""Cmdb/firewall/vipgrp6 connector."""

from fortigate_api.connector import Connector


class Vipgrp6FC(Connector):
    """Cmdb/firewall/vipgrp6 connector."""

    uid = "name"
    _path = "api/v2/cmdb/firewall/vipgrp6"
