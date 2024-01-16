"""Cmdb/firewall/vipgrp46 connector."""

from fortigate_api.connector import Connector


class Vipgrp46FC(Connector):
    """Cmdb/firewall/vipgrp46 connector."""

    uid = "name"
    _path = "api/v2/cmdb/firewall/vipgrp46"
