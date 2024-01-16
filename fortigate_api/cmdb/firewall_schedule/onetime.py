"""Cmdb/firewall.schedule/onetime connector."""

from fortigate_api.connector import Connector


class OnetimeFsC(Connector):
    """Cmdb/firewall.schedule/onetime connector."""

    uid = "name"
    _path = "api/v2/cmdb/firewall.schedule/onetime"
    _path_ui = "ng/firewall/schedule"
