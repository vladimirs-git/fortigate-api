"""Cmdb/system.snmp/user connector."""

from fortigate_api.connector import Connector


class UserSsC(Connector):
    """Cmdb/system.snmp/user connector."""

    uid = "name"
    _path = "api/v2/cmdb/system.snmp/user"
