"""Cmdb/wanopt/settings connector."""

from fortigate_api.connector import Connector


class SettingsWC(Connector):
    """Cmdb/wanopt/settings connector."""

    uid = ""
    _path = "api/v2/cmdb/wanopt/settings"
