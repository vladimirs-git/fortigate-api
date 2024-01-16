"""Cmdb/vpn.ipsec/manualkey connector."""

from fortigate_api.connector import Connector


class ManualkeyViC(Connector):
    """Cmdb/vpn.ipsec/manualkey connector."""

    uid = "name"
    _path = "api/v2/cmdb/vpn.ipsec/manualkey"
