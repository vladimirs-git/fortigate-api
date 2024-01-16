"""Cmdb/wireless-controller/snmp connector."""

from fortigate_api.connector import Connector


class SnmpWcC(Connector):
    """Cmdb/wireless-controller/snmp connector."""

    uid = ""
    _path = "api/v2/cmdb/wireless-controller/snmp"
