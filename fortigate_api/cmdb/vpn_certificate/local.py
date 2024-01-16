"""Cmdb/vpn.certificate/local connector."""

from fortigate_api.connector import Connector


class LocalVcC(Connector):
    """Cmdb/vpn.certificate/local connector."""

    uid = "name"
    _path = "api/v2/cmdb/vpn.certificate/local"
