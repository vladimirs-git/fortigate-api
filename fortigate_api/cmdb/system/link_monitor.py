"""Cmdb/system/link-monitor connector."""

from fortigate_api.connector import Connector


class LinkMonitorSC(Connector):
    """Cmdb/system/link-monitor connector."""

    uid = "name"
    _path = "api/v2/cmdb/system/link-monitor"
