"""Cmdb/system/ha-monitor connector."""

from fortigate_api.connector import Connector


class HaMonitorSC(Connector):
    """Cmdb/system/ha-monitor connector."""

    uid = ""
    _path = "api/v2/cmdb/system/ha-monitor"
