"""Cmdb/vpn.ipsec/phase1 connector."""

from fortigate_api.connector import Connector


class Phase1ViC(Connector):
    """Cmdb/vpn.ipsec/phase1 connector."""

    uid = "name"
    _path = "api/v2/cmdb/vpn.ipsec/phase1"
