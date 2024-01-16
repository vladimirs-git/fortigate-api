"""Cmdb/firewall/ldb-monitor connector."""

from fortigate_api.connector import Connector


class LdbMonitorFC(Connector):
    """Cmdb/firewall/ldb-monitor connector."""

    uid = "name"
    _path = "api/v2/cmdb/firewall/ldb-monitor"
