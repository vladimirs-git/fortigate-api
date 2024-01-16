"""Cmdb/vpn.ssl.web/host-check-software connector."""

from fortigate_api.connector import Connector


class HostCheckSoftwareVswC(Connector):
    """Cmdb/vpn.ssl.web/host-check-software connector."""

    uid = "name"
    _path = "api/v2/cmdb/vpn.ssl.web/host-check-software"
