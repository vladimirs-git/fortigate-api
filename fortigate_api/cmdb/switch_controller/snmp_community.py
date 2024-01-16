"""Cmdb/switch-controller/snmp-community connector."""

from fortigate_api.connector import Connector


class SnmpCommunityScC(Connector):
    """Cmdb/switch-controller/snmp-community connector."""

    uid = "id"
    _path = "api/v2/cmdb/switch-controller/snmp-community"
