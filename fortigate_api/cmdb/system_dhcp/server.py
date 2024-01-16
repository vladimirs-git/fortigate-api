"""Cmdb/system.dhcp/server connector."""

from fortigate_api.connector import Connector


class ServerSdC(Connector):
    """Cmdb/system.dhcp/server connector."""

    uid = "id"
    _path = "api/v2/cmdb/system.dhcp/server"
    _path_ui = "ng/interface/edit/{name}"
