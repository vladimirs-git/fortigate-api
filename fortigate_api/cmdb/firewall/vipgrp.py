"""Cmdb/firewall/vipgrp connector."""

from fortigate_api.connector import Connector


class VipgrpFC(Connector):
    """Cmdb/firewall/vipgrp connector."""

    uid = "name"
    _path = "api/v2/cmdb/firewall/vipgrp"
