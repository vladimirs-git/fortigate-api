"""Cmdb/firewall.schedule/group connector."""

from fortigate_api.connector import Connector


class GroupFsC(Connector):
    """Cmdb/firewall.schedule/group connector."""

    uid = "name"
    _path = "api/v2/cmdb/firewall.schedule/group"
