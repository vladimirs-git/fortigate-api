"""Cmdb/vpn/pptp connector."""

from fortigate_api.connector import Connector


class PptpVC(Connector):
    """Cmdb/vpn/pptp connector."""

    uid = ""
    _path = "api/v2/cmdb/vpn/pptp"
