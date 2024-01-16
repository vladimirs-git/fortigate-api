"""Cmdb/vpn.certificate/ca connector."""

from fortigate_api.connector import Connector


class CaVcC(Connector):
    """Cmdb/vpn.certificate/ca connector."""

    uid = "name"
    _path = "api/v2/cmdb/vpn.certificate/ca"
