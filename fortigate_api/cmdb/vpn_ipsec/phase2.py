"""Cmdb/vpn.ipsec/phase2 connector."""

from fortigate_api.connector import Connector


class Phase2ViC(Connector):
    """Cmdb/vpn.ipsec/phase2 connector."""

    uid = "name"
    _path = "api/v2/cmdb/vpn.ipsec/phase2"
