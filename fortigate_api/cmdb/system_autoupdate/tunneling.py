"""Cmdb/system.autoupdate/tunneling connector."""

from fortigate_api.connector import Connector


class TunnelingSaC(Connector):
    """Cmdb/system.autoupdate/tunneling connector."""

    uid = ""
    _path = "api/v2/cmdb/system.autoupdate/tunneling"
