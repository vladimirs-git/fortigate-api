"""Cmdb/log/setting connector."""

from fortigate_api.connector import Connector


class SettingLC(Connector):
    """Cmdb/log/setting connector."""

    uid = ""
    _path = "api/v2/cmdb/log/setting"
