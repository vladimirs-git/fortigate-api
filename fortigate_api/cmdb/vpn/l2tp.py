"""Cmdb/vpn/l2tp connector."""

from fortigate_api.connector import Connector


class L2tpVC(Connector):
    """Cmdb/vpn/l2tp connector."""

    uid = ""
    _path = "api/v2/cmdb/vpn/l2tp"
