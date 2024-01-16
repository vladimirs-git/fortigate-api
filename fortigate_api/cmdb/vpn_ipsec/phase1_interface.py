"""Cmdb/vpn.ipsec/phase1-interface connector."""

from fortigate_api.connector import Connector


class Phase1InterfaceViC(Connector):
    """Cmdb/vpn.ipsec/phase1-interface connector."""

    uid = "name"
    _path = "api/v2/cmdb/vpn.ipsec/phase1-interface"
