"""Cmdb/firewall.service/custom connector."""

from fortigate_api.connector import Connector


class CustomFsC(Connector):
    """Cmdb/firewall.service/custom connector."""

    uid = "name"
    _path = "api/v2/cmdb/firewall.service/custom"
    _path_ui = "ng/firewall/service"
