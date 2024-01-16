"""Cmdb/vpn.certificate/remote connector."""

from fortigate_api.connector import Connector


class RemoteVcC(Connector):
    """Cmdb/vpn.certificate/remote connector."""

    uid = "name"
    _path = "api/v2/cmdb/vpn.certificate/remote"
