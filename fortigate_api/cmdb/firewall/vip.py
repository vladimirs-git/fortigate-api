"""Cmdb/firewall/vip connector."""

from fortigate_api.connector import Connector


class VipFC(Connector):
    """Cmdb/firewall/vip connector."""

    uid = "name"
    _path = "api/v2/cmdb/firewall/vip"
    _path_ui = "ng/firewall/virtual-ip"
