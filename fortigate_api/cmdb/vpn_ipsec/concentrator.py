"""Cmdb/vpn.ipsec/concentrator connector."""

from fortigate_api.connector import Connector


class ConcentratorViC(Connector):
    """Cmdb/vpn.ipsec/concentrator connector."""

    uid = "name"
    _path = "api/v2/cmdb/vpn.ipsec/concentrator"
