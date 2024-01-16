"""Cmdb/system/settings connector."""

from fortigate_api.connector import Connector


class SettingsSC(Connector):
    """Cmdb/system/settings connector."""

    uid = ""
    _path = "api/v2/cmdb/system/settings"
