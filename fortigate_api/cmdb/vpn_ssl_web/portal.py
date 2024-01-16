"""Cmdb/vpn.ssl.web/portal connector."""

from fortigate_api.connector import Connector


class PortalVswC(Connector):
    """Cmdb/vpn.ssl.web/portal connector."""

    uid = "name"
    _path = "api/v2/cmdb/vpn.ssl.web/portal"
