"""Cmdb/vpn/ocvpn connector."""

from fortigate_api.connector import Connector


class OcvpnVC(Connector):
    """Cmdb/vpn/ocvpn connector."""

    uid = ""
    _path = "api/v2/cmdb/vpn/ocvpn"
