"""Cmdb/dlp/settings connector."""

from fortigate_api.connector import Connector


class SettingsDC(Connector):
    """Cmdb/dlp/settings connector."""

    uid = ""
    _path = "api/v2/cmdb/dlp/settings"
