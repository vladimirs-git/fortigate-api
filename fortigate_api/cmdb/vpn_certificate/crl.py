"""Cmdb/vpn.certificate/crl connector."""

from fortigate_api.connector import Connector


class CrlVcC(Connector):
    """Cmdb/vpn.certificate/crl connector."""

    uid = "name"
    _path = "api/v2/cmdb/vpn.certificate/crl"
