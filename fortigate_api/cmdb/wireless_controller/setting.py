"""Cmdb/wireless-controller/setting connector."""

from fortigate_api.connector import Connector


class SettingWcC(Connector):
    """Cmdb/wireless-controller/setting connector."""

    uid = ""
    _path = "api/v2/cmdb/wireless-controller/setting"
