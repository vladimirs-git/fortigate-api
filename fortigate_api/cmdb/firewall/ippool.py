"""Cmdb/firewall/ippool connector."""

from fortigate_api.connector import Connector


class IppoolFC(Connector):
    """Cmdb/firewall/ippool connector."""

    uid = "name"
    _path = "api/v2/cmdb/firewall/ippool"
    _path_ui = "ng/firewall/ip-pool"
