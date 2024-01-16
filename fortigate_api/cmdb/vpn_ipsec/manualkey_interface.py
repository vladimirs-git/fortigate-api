"""Cmdb/vpn.ipsec/manualkey-interface connector."""

from fortigate_api.connector import Connector


class ManualkeyInterfaceViC(Connector):
    """Cmdb/vpn.ipsec/manualkey-interface connector."""

    uid = "name"
    _path = "api/v2/cmdb/vpn.ipsec/manualkey-interface"
