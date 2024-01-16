"""Cmdb/vpn.ssl.web/realm connector."""

from fortigate_api.connector import Connector


class RealmVswC(Connector):
    """Cmdb/vpn.ssl.web/realm connector."""

    uid = "url-path"
    _path = "api/v2/cmdb/vpn.ssl.web/realm"
