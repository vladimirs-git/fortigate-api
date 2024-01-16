"""Cmdb/system.snmp/community connector."""

from fortigate_api.connector import Connector


class CommunitySsC(Connector):
    """Cmdb/system.snmp/community connector."""

    uid = "id"
    _path = "api/v2/cmdb/system.snmp/community"
    _path_ui = "ng/system/snmp"
