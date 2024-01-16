"""Cmdb/vpn.ipsec/phase2-interface connector."""

from fortigate_api.connector import Connector


class Phase2InterfaceViC(Connector):
    """Cmdb/vpn.ipsec/phase2-interface connector."""

    uid = "name"
    _path = "api/v2/cmdb/vpn.ipsec/phase2-interface"
