"""Cmdb/vpn.ssl/settings connector."""

from fortigate_api.connector import Connector


class SettingsVsC(Connector):
    """Cmdb/vpn.ssl/settings connector."""

    uid = ""
    _path = "api/v2/cmdb/vpn.ssl/settings"
