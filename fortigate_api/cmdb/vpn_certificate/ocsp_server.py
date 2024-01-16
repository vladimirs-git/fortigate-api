"""Cmdb/vpn.certificate/ocsp-server connector."""

from fortigate_api.connector import Connector


class OcspServerVcC(Connector):
    """Cmdb/vpn.certificate/ocsp-server connector."""

    uid = "name"
    _path = "api/v2/cmdb/vpn.certificate/ocsp-server"
