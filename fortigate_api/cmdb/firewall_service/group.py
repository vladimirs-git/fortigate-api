"""Cmdb/firewall.service/group connector."""

from fortigate_api.connector import Connector


class GroupFsC(Connector):
    """Cmdb/firewall.service/group connector."""

    uid = "name"
    _path = "api/v2/cmdb/firewall.service/group"
    _path_ui = "ng/firewall/service"
