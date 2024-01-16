"""Cmdb/ips/settings connector."""

from fortigate_api.connector import Connector


class SettingsIC(Connector):
    """Cmdb/ips/settings connector."""

    uid = ""
    _path = "api/v2/cmdb/ips/settings"
