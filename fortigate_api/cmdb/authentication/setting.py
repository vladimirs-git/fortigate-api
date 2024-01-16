"""Cmdb/authentication/setting connector."""

from fortigate_api.connector import Connector


class SettingAC(Connector):
    """Cmdb/authentication/setting connector."""

    uid = ""
    _path = "api/v2/cmdb/authentication/setting"
