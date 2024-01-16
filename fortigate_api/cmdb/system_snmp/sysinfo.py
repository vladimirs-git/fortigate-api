"""Cmdb/system.snmp/sysinfo connector."""

from fortigate_api.connector import Connector


class SysinfoSsC(Connector):
    """Cmdb/system.snmp/sysinfo connector."""

    uid = ""
    _path = "api/v2/cmdb/system.snmp/sysinfo"
