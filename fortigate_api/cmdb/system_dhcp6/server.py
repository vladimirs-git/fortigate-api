"""Cmdb/system.dhcp6/server connector."""

from fortigate_api.connector import Connector


class ServerSdC(Connector):
    """Cmdb/system.dhcp6/server connector."""

    uid = "id"
    _path = "api/v2/cmdb/system.dhcp6/server"
